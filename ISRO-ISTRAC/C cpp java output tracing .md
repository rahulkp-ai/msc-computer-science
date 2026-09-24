# C / C++ / Java — Trace-the-Output Worked Examples

Built from ISRO SAC/VSSC/SHAR PYQs (2015–2019). This is the single highest-frequency
question _type_ across all four papers (8–10 per 80Q paper) — worth more prep time per
mark than almost anything else in the syllabus.

**How to use this file:** Cover the "Trace" column, predict the output yourself, then
check. Speed matters as much as accuracy — aim to trace these in under 20 seconds each
by exam time.

---

## 1. Pre-increment vs Post-increment

### PYQ (SAC 2017/18, Q70)

```c
int main() {
  int a = 10;
  int b, c;
  b = a++;
  c = a;
  cout << b << a << c;
  return 0;
}
```

**Trace:**
| Step | Statement | a | b | c |
|---|---|---|---|---|
| 1 | `int a = 10;` | 10 | – | – |
| 2 | `b = a++;` → b gets OLD value of a, THEN a increments | 11 | 10 | – |
| 3 | `c = a;` | 11 | 10 | 11 |

**Output: `101111`** (concatenated, not spaced — cout has no separator here)

**Answer key given in paper:** (a) 101111 ✅

---

### PYQ (SAC 2017/18, Q63)

```c
int main() {
  int c1, c2;
  int a = -8;
  int b = 3;
  c1 = --a + b;
  c2 = a-- + b;
  cout << "c1=" << c1 << ", c2=" << c2 << endl;
  return 0;
}
```

**Trace:**
| Step | Statement | a | c1 | c2 |
|---|---|---|---|---|
| 1 | `a = -8, b = 3` | -8 | – | – |
| 2 | `c1 = --a + b;` → a decrements FIRST to -9, then -9+3 | -9 | -4 | – |
| 3 | `c2 = a-- + b;` → uses CURRENT a (-9) first, THEN decrements a to -10 | -10 | -4 | -6 |

**Output: `c1=-4, c2=-6`**

⚠️ **Gotcha:** the paper's answer options don't include -4,-6 exactly as computed above in
this worked form — always re-derive by hand rather than pattern-matching to a memorized
answer. The rule that matters: `--a` changes `a` _before_ it's used in the expression;
`a--` changes `a` _after_.

---

## 2. Loop Accumulation (Sum Series)

### PYQ (VSSC 1386, 2019, Q1)

```c
int i = 0;
int sum = 0;
for (i = 1; i < 11; i++) {
  sum = sum + i;
}
print(sum);
```

**Trace:** Loop runs i = 1,2,3,...,10 (stops before 11, since condition is `i < 11`)

Sum = 1+2+...+10 = **55**

**Answer: (a) 55**

⚠️ **Gotcha:** watch the loop bound carefully. `i < 11` with `i++` means the loop
includes i=10 but NOT i=11. If the question had said `i <= 11`, the sum would be 66.
ISRO papers deliberately test this off-by-one boundary.

---

### PYQ (VSSC 1370, 2018, Q45)

```c
int myFunction(int x) {
  int sum = 0;
  for (int i = 1; i <= x; i++) {
    sum = sum + i;
  }
  printf("%d", sum);
}
```

Called as `myFunction(5)`:

Sum = 1+2+3+4+5 = **15**

**Answer: (c) 15**

---

## 3. if-else Value Tracing

### PYQ (VSSC 1370, 2018, Q31)

```c
int main() {
  int a = 100, b = 30;
  if (a < 25) {
    a = a - 50;
  } else {
    b = b + 50;
  }
  printf("a=%d, b=%d ", a, b);
  return 0;
}
```

**Trace:** `a < 25` → `100 < 25` is FALSE → else branch runs → `b = 30 + 50 = 80`, `a`
unchanged at 100.

**Output: `a=100, b=80`**

**Answer: (a) a=100, b=80**

---

## 4. switch-case Fallthrough (no `break`)

### PYQ (VSSC 1370, 2018, Q36)

```c
int main() {
  char myChar = 'A';
  switch (myChar) {
    case 'A': printf("Chemistry, ");
    case 'B':
    case 'C': printf("Math, ");
    case 'D':
    case 'E':
    default: printf("Physics ");
  }
  return 0;
}
```

**Trace:** `myChar == 'A'` matches `case 'A'` → prints "Chemistry, " → **no break**, so
execution FALLS THROUGH every subsequent case (B does nothing itself, C prints "Math, ",
D/E do nothing, default prints "Physics ")

**Output: `Chemistry, Math, Physics`**

**Answer: (d) Chemistry, Math, Physics**

⚠️ **Gotcha:** this is the #1 switch-case trap in every exam that tests C. Without
`break`, control doesn't stop at the matched case — it keeps executing every line below
it, including `default`, regardless of whether their own case label matched.

---

## 5. Macro Expansion Trap

### PYQ (SHAR Sci. Asst. 2015, Q29)

```c
#include <stdio.h>
#define SQR(x) (x*x)
int main() {
  int a;
  int b = 4;
  a = SQR(b+2);
  printf("%d\n", a);
  return 0;
}
```

**Trace — do NOT compute this as `(4+2)² = 36`.** A macro is pure _textual substitution_,
not a function call. `SQR(b+2)` literally expands to:

```c
a = (b+2*b+2);   // NOT (b+2)*(b+2) !
```

With b=4: `a = (4 + 2*4 + 2) = 4 + 8 + 2 = 14`

**Output: 14**

**Answer: (a) 14**

This exact pattern (`#define SQR(x) (x*x)` without parenthesizing `x` inside the macro
body) is a classic ISRO trap — see the dedicated gotcha file for the general rule.

---

## 6. Java Program — Constructor Chaining & Inheritance

### PYQ (SAC 2017/18, Q13)

```java
class A {
  private A() {
    System.out.print("ISRO");
  }
}
class B extends A {
  B() {
    System.out.print(" India");
  }
}
class main1 {
  public static void main(String args[]) {
    B b = new B();
  }
}
```

**Trace:** `A()` is declared `private`, which means it is **not accessible/inheritable**
from class `B` even though `B extends A`. Java requires every subclass constructor to
implicitly (or explicitly) call a superclass constructor via `super()` — but `A()` is
private, so `B` cannot call it at all.

**Output: Compile time error**

**Answer: (c) Compile time error**

⚠️ **Gotcha:** a private constructor blocks subclassing from using it — this is a very
common "does it compile" trap distinct from access-modifier questions about fields/methods.

---

## 7. Java — Access Modifiers Don't Block Access Within the Same Class

### PYQ (VSSC 1386, 2019, Q77)

```java
class TEST {
  public static void main(String args[]) {
    public int x = 3;
    protected int y = 6;
    private int z = 9;
    System.out.println(x + y + z);
  }
}
```

**Trace:** Inside `main`, all three variables are local to the _same class_ — access
modifiers (`public`/`protected`/`private`) only restrict access from _outside_ the class
or package; they don't stop code within the same class from reading its own fields.

Sum = 3 + 6 + 9 = **18**

**Answer: (b) prints 18**

⚠️ Note: local variables inside a method technically cannot be declared `public`/
`protected`/`private` in real Java (this would be a compile error in a strict sense) —
but as an MCQ-logic question, ISRO is testing whether you understand that these
modifiers govern _external_ visibility, not internal computation. Answer the intent of
the question, not the strict compiler nuance, unless the options explicitly include a
"compile error" choice.

---

## 8. C++ Precedence — No Surprises, Just Careful Arithmetic

### PYQ (VSSC 1386, 2019, Q11)

```cpp
int main() {
  int sal;
  sal = 4 + 2 * 15;
  cout << sal;
  return 0;
}
```

**Trace:** Standard precedence: `*` before `+`. `2*15=30`, then `4+30=34`.

**Output: 34**

**Answer: (b) 34**

⚠️ **Gotcha:** ISRO includes these "obvious" precedence questions to catch candidates
who are rushing. Never skip the mental precedence check even on questions that look
trivial — they're free marks if you slow down for 5 seconds.

---

## 9. String Comparison with `==` in C (Pointer Comparison, Not Content Comparison)

### PYQ (VSSC 1386, 2019, Q46)

```c
#include <stdio.h>
void main() {
  char str1[] = "ISRO", str2[] = "ISRO";
  if (str1 == str2) {
    printf("both are same");
  } else {
    printf("both are NOT same");
  }
}
```

**Trace:** `str1` and `str2` are two _separate arrays_ with the same content — in C,
`==` on arrays/pointers compares their **memory addresses**, not their contents.
Since they are different arrays, their addresses differ.

**Output: `both are NOT same`**

**Answer: (b) both are NOT same**

⚠️ **Gotcha:** to compare string _content_ in C you must use `strcmp()`, never `==`.
This trap appears in some form in almost every ISRO paper.

---

## 10. Pointer Arithmetic on char Arrays

### PYQ (VSSC 1370, 2018, Q44)

```c
#include <stdio.h>
int main() {
  char myChar[7] = "Hanger", *ptr;
  ptr = myChar + 4;
  *ptr = 'a';
  printf("%s", myChar);
  return 0;
}
```

**Trace:** `myChar = "Hanger"` → indices: H(0) a(1) n(2) g(3) e(4) r(5) \0(6)

`ptr = myChar + 4` → points to index 4, which is `'e'`

`*ptr = 'a';` → overwrites index 4 from `'e'` to `'a'`

New string: H-a-n-g-**a**-r → **"Hangar"**

**Output: Hangar**

**Answer: (c) Hangar**

(Full breakdown of this pattern is in the companion gotcha file, section 1.)

---

### PYQ (VSSC 1386, 2019, Q55)

```c
char c[] = "LAKEVIEW";
char *p = c;
printf("%s", p + p[3] - p[1]);
```

**Trace:** This one is dense — work it in two parts.

`p[3]` = the char at index 3 of "LAKEVIEW" = `'E'` → but in the arithmetic
`p[3] - p[1]`, these are **char values being subtracted as integers** (ASCII), not
printed as characters.

`p[1]` = `'A'`

`p[3] - p[1]` = `'E' - 'A'` = ASCII(69) - ASCII(65) = **4**

So the full expression is `p + 4`, i.e. pointer arithmetic: start at `p` (index 0, 'L')
and move 4 positions forward → index 4 = `'V'`

Printing `%s` from that pointer prints from index 4 to the end: **"VIEW"**

**Answer: (b) EVIEW... wait — re-check:** L(0) A(1) K(2) E(3) V(4) I(5) E(6) W(7).
Index 4 = 'V', so the substring from index 4 onward is "VIEW".

**Output: VIEW**

⚠️ **Gotcha:** when you see `char - char` inside a pointer-arithmetic expression, it's
almost always an ASCII-difference trick used to compute an integer offset — not a
character being printed. Separate the two operations mentally: resolve the arithmetic to
a number FIRST, then apply it as an offset to the pointer SECOND.

---

## 11. Call by Reference in C++

### PYQ (VSSC 1386, 2019, Q65)

```cpp
void check(int &arg1) {
  arg1 = 550;
}
int main() {
  int arg = 10;
  check(arg);
  cout << "New value of arg is " << arg;
  return 0;
}
```

**Trace:** `int &arg1` is a **reference parameter** — `arg1` is not a copy, it's another
name for the same memory as `arg`. Modifying `arg1` inside `check()` directly modifies
`arg` in `main()`.

**Output: New value of arg is 550**

**Answer: (b) New value of arg is 550**

⚠️ **Gotcha:** the opposite trap (pass-by-value, where the caller's variable does NOT
change) is equally common — always check whether the parameter has `&` before assuming
either direction.

---

## Quick Self-Test Set (no answers shown — trace these cold, then verify against the

patterns above)

```c
// A
int x = 5;
int y = x++ + ++x;
printf("%d %d", x, y);

// B
int a = 2, b = 3;
a = a++ + b++;
printf("%d", a);

// C — macro trap
#define DOUBLE(x) x+x
int r = 3 * DOUBLE(4);   // NOT 24 — apply the same rule as SQR() above

// D — Java
class P {
  static int x = 10;
}
class Q extends P {
  public static void main(String[] a) {
    P.x = 20;
    System.out.println(x);   // static field access via subclass
  }
}
```

Work through each using the traced patterns above before checking a compiler — the goal
is to be able to do this reliably by hand under exam time pressure (no compiler/IDE
allowed in the hall).
