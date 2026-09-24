# Java Exception Hierarchy & try/catch/finally Execution Order

Built from ISRO PYQs. Exception-handling questions appear in every paper in one of two
forms: (1) hierarchy/terminology questions, (2) execution-order tracing questions. Both
are covered here.

---

## PART 1 — The Exception Class Hierarchy

### PYQ (SAC 2017/18, Q9)

> "In Java, the class at the top of the exception classes hierarchy is called **\_\_**."
> (a) Common (b) Throwable (c) Null (d) Catch

**Answer: (b) Throwable**

### The hierarchy you must memorize

```
                    Object
                      |
                  Throwable
                   /      \
                Error      Exception
               /              |    \
       (OutOfMemoryError,   RuntimeException   (IOException,
        StackOverflowError,  /    |    \        SQLException,
        etc. — JVM-level,   /     |     \       ClassNotFoundException,
        NOT meant to be    /      |      \      — "checked" exceptions,
        caught in normal  /       |       \     MUST be declared/caught)
        app code)    NullPointer  ArrayIndex  ArithmeticException
                      Exception   OutOfBounds  (e.g. divide by zero)
                                  Exception
```

**Key facts to lock in:**

- `Throwable` is the root of BOTH branches — this is what Q9 above is testing.
- `Error` and `Exception` are the two direct children of `Throwable`.
- `Exception` splits into **checked** exceptions (must be declared with `throws` or
  caught — e.g. `IOException`) and **unchecked** exceptions, which all extend
  `RuntimeException` (do NOT need to be declared — e.g. `NullPointerException`,
  `ArithmeticException`, `ArrayIndexOutOfBoundsException`).
- `Error` types (like `OutOfMemoryError`, `StackOverflowError`) represent serious JVM-
  level problems — conventionally NOT caught by application code, even though it's
  technically possible.

**Common MCQ trap:** being asked "which of these is NOT a subclass of Exception" and
having `OutOfMemoryError` in the options — it's a subclass of `Error`, not `Exception`.

---

## PART 2 — What Happens When No `catch` Block Matches

### PYQ (SHAR Sci. Asst. 2015, Q40)

> "If an exception is thrown and no catch block matches the type of the thrown
> parameter, then **\_\_**."
> (a) The program terminates
> (b) The first catch block is executed
> (c) The last catch block is executed
> (d) The program proceeds with the code following the catch blocks

**Answer: (a) The program terminates**

**Rule:** Java catch blocks are checked **in order, top to bottom**, and only the FIRST
one whose type matches (or is a superclass of) the thrown exception's type gets
executed. If NONE of them match, the exception propagates up the call stack — if it
reaches `main()` unhandled, the JVM terminates the program and prints a stack trace.

---

## PART 3 — try/catch/finally Execution Order

### The core rules to memorize

1. `finally` runs **no matter what** — whether an exception was thrown or not, and even
   if the `try` or `catch` block contains a `return` statement.
2. If both `catch` and `finally` have `return` statements, the `finally` block's
   `return` **wins** (overrides the one from `try`/`catch`) — this is a classic trap.
3. Catch blocks are evaluated top-to-bottom; put more SPECIFIC exception types before
   more GENERAL ones (e.g. `ArithmeticException` before `Exception`), or the general one
   will always match first and the specific one becomes unreachable (compile error in
   Java for exact hierarchy mismatches).
4. `finally` does NOT run only in extreme cases: `System.exit()` called inside `try`/
   `catch`, or if the JVM itself crashes.

### C++ comparison (also appears in ISRO papers — "finally" behavior across languages)

### PYQ (VSSC 1386, 2019, Q66)

> "In the context of Error handling in C++ and Java, which of the following is true
> about 'finally'?"
> (a) finally block is mandatory
> (b) It will be executed only if exception occurs
> (c) It will be executed only if NO exception occurs
> (d) It will be executed irrespective of exception occurrence

**Answer: (d) It will be executed irrespective of exception occurrence**

⚠️ **Note the framing trap:** this question is phrased about "C++ and Java" together,
but standard C++ does NOT actually have a `finally` keyword (that's Java/C#-specific
terminology; C++ uses RAII/destructors for similar guarantees). Treat this as a
conceptual question about the _general finally-block guarantee_ rather than literal C++
syntax — answer based on Java's behavior, which is what's actually being tested.

---

## Worked Execution-Order Traces

### Trace A — finally always runs, even after a return in try

```java
public class Test {
  static int test() {
    try {
      return 1;
    } finally {
      System.out.println("finally ran");
    }
  }
  public static void main(String[] args) {
    System.out.println(test());
  }
}
```

**Trace:**

1. `try` block executes `return 1` — but before the method actually returns, Java
   ensures `finally` runs FIRST.
2. `finally` prints "finally ran".
3. THEN the method returns the value 1 (which was already computed/queued in step 1).

**Output:**

```
finally ran
1
```

---

### Trace B — finally's return OVERRIDES try's return (classic trap)

```java
public class Test {
  static int test() {
    try {
      return 1;
    } finally {
      return 2;
    }
  }
  public static void main(String[] args) {
    System.out.println(test());
  }
}
```

**Trace:** `try` queues up `return 1`, but before it actually exits, `finally` runs —
and `finally` ALSO has a `return` statement (`return 2`). When `finally` has its own
`return`, it **completely discards** the pending return value from `try`/`catch` and
returns its own value instead.

**Output: `2`** (NOT 1 — this is one of the most commonly tested Java gotchas)

⚠️ **Rule to memorize:** if `finally` contains a `return`, it always wins, no matter
what `try` or `catch` were about to return. (This is considered bad practice in real
code, which is exactly why exams love testing whether you know the rule.)

---

### Trace C — Exception inside try, caught, then finally

```java
public class Test {
  public static void main(String[] args) {
    try {
      int x = 5 / 0;
      System.out.println("This won't print");
    } catch (ArithmeticException e) {
      System.out.println("Caught: " + e.getMessage());
    } finally {
      System.out.println("Finally block");
    }
    System.out.println("After try-catch-finally");
  }
}
```

**Trace:**

1. `5 / 0` throws `ArithmeticException` immediately — the line after it inside `try`
   ("This won't print") never executes.
2. Control jumps straight to the matching `catch` block → prints "Caught: / by zero"
3. `finally` always runs next → prints "Finally block"
4. Normal execution resumes after the whole try-catch-finally → prints "After
   try-catch-finally"

**Output:**

```
Caught: / by zero
Finally block
After try-catch-finally
```

---

### Trace D — Multiple catch blocks, order matters

```java
public class Test {
  public static void main(String[] args) {
    try {
      int[] arr = new int[3];
      arr[5] = 10;
    } catch (Exception e) {
      System.out.println("Generic exception caught");
    } catch (ArrayIndexOutOfBoundsException e) {
      System.out.println("Array index exception caught");
    }
  }
}
```

**Trace:** `ArrayIndexOutOfBoundsException` IS-A `Exception` (it's further down the
hierarchy chain). Since the general `catch (Exception e)` comes FIRST, it matches and
catches the exception before the more specific catch block ever gets a chance.

**Output: `Generic exception caught`**

⚠️ **This exact ordering is actually a COMPILE ERROR in real Java** ("exception
`ArrayIndexOutOfBoundsException` has already been caught") — Java's compiler detects
that the second catch block is unreachable and refuses to compile. If an MCQ presents
this exact code and asks "what is the output," the strictly correct technical answer
may be "compile-time error," not the printed text. **Always check whether the answer
options include a compile-error choice before assuming the code runs at all** — this is
a very common ISRO trap pattern (seen in the constructor/private-access question too,
see the companion output-tracing file, section 6).

---

## Quick Self-Test (trace these cold before checking against the rules above)

```java
// A — does finally override try's return?
static String test() {
  try {
    return "try";
  } finally {
    System.out.println("in finally");
  }
}
// What prints, and what does test() return?

// B — exception thrown INSIDE finally itself
public static void main(String[] args) {
  try {
    try {
      throw new RuntimeException("first");
    } finally {
      throw new RuntimeException("second");
    }
  } catch (RuntimeException e) {
    System.out.println("Caught: " + e.getMessage());
  }
}
// Which exception message actually gets caught — "first" or "second"?

// C — nested try, no matching catch at inner level
public static void main(String[] args) {
  try {
    try {
      int x = 10 / 0;
    } catch (NullPointerException e) {
      System.out.println("Inner catch");
    }
  } catch (ArithmeticException e) {
    System.out.println("Outer catch");
  }
}
// Which catch block runs, inner or outer?
```

**Answers (check after attempting):**

- **A:** prints "in finally", then returns "try" (finally has no `return` of its own
  here, so it doesn't override — it just runs and lets the original return proceed)
- **B:** "second" — when `finally` itself throws, that new exception **replaces** the
  one from `try`, exactly like a `return` in `finally` overriding a pending one
- **C:** "Outer catch" — the inner `catch` only matches `NullPointerException`, which
  doesn't match `ArithmeticException`, so the exception propagates up and out of the
  inner try-catch entirely, where the OUTER catch (correct type) finally catches it
