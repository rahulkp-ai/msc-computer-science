# Common Gotcha Patterns — C/C++ Pointer Arithmetic & Macro Traps

These are the two trap-categories ISRO reuses most often in disguised form across
papers. Learn the _pattern_, not just the specific worked question — the exam rarely
repeats the exact same numbers, but it reuses the exact same trap shape every year.

---

## PART 1 — Pointer Arithmetic on char Arrays

### The core rule

When `ptr` is a `char *` pointing into an array, `ptr + n` moves the pointer **n bytes
forward** (since `sizeof(char) == 1`, this is the simplest pointer arithmetic case — no
scaling by element size needed, unlike `int*` or `struct*` pointers).

`*ptr` dereferences to get/set the single character at that position.

`printf("%s", ptr)` prints from wherever `ptr` currently points **to the end of the
string** (up to the null terminator `\0`) — not from the start of the original array.

### Worked pattern (from VSSC 1370, 2018, Q44)

```c
char myChar[7] = "Hanger", *ptr;
ptr = myChar + 4;
*ptr = 'a';
printf("%s", myChar);
```

Index map: `H(0) a(1) n(2) g(3) e(4) r(5) \0(6)`

- `ptr = myChar + 4` → points at index 4 → currently `'e'`
- `*ptr = 'a'` → overwrites index 4 in place → string becomes `Hang**a**r`
- `printf("%s", myChar)` prints from the **start** of the array (because we printed
  `myChar`, not `ptr`) → **"Hangar"**

**Key distinction:** printing `myChar` vs printing `ptr` gives different results after
this operation, even though both point into the same underlying array:

```c
printf("%s", myChar);  // "Hangar"  — from index 0
printf("%s", ptr);     // "ar"      — from index 4 onward (a,r,\0)
```

ISRO likes to swap which variable is printed between similar-looking questions — always
check which pointer/array name is actually inside the `printf`.

### Worked pattern (from VSSC 1386, 2019, Q55)

```c
char c[] = "LAKEVIEW";
char *p = c;
printf("%s", p + p[3] - p[1]);
```

This combines TWO separate operations that look like one:

**Step 1 — resolve `p[3] - p[1]` as a plain integer (ASCII subtraction):**
Index map: `L(0) A(1) K(2) E(3) V(4) I(5) E(6) W(7)`

- `p[3]` = `'E'` (ASCII 69)
- `p[1]` = `'A'` (ASCII 65)
- `p[3] - p[1]` = 69 - 65 = **4** (a plain int, not a character)

**Step 2 — apply that integer as a pointer offset to `p`:**
`p + 4` → points to index 4 → `'V'`

**Step 3 — print from there to the end:**
`%s` from index 4 → **"VIEW"**

### The general trap-detection rule

Whenever you see an expression like:

```
ptr + char_expr - char_expr
```

inside a `printf("%s", ...)`, split it mentally into:

1. **Arithmetic phase** — any `char - char` or `char + char` is integer arithmetic
   (ASCII values), evaluate it to a plain number first.
2. **Pointer phase** — apply that number as an offset (`+`) to the base pointer.
3. **Print phase** — `%s` prints from the resulting address to the next `\0`.

Never try to evaluate the whole expression left-to-right as if it were one operation —
break it into these three phases every time.

### Practice pattern (work this cold)

```c
char word[] = "COMPUTER";
char *ptr = word;
printf("%s", ptr + word[5] - word[1]);
```

Index map: `C(0) O(1) M(2) P(3) U(4) T(5) E(6) R(7)`

- `word[5]` = `'T'` (84), `word[1]` = `'O'` (79) → 84-79 = **5**
- `ptr + 5` → index 5 → `'T'`
- Prints from index 5 onward: **"TER"**

---

## PART 2 — Macro Expansion Pitfalls (`#define`)

### The core rule

A `#define` macro is **pure textual substitution** performed by the preprocessor
_before compilation even begins_. It is NOT a function call, and the argument is NOT
evaluated first — the macro body is substituted **verbatim, token-for-token**, and only
THEN does normal arithmetic evaluate.

### Worked pattern (from SHAR Sci. Asst. 2015, Q29)

```c
#define SQR(x) (x*x)
int b = 4;
int a = SQR(b+2);
```

**WRONG intuition:** "SQR(b+2) means (b+2) squared, so (4+2)² = 36"

**CORRECT mechanics:** the preprocessor performs literal text substitution of `x` with
whatever text was passed — here, the text `b+2` — everywhere `x` appears in the macro
body:

```
(x*x)  →  (b+2*b+2)     [substitute x → b+2, literally, textually]
```

Now apply normal operator precedence to `(b+2*b+2)` with `b=4`:

```
(4 + 2*4 + 2) = (4 + 8 + 2) = 14
```

**Output: 14** — NOT 36.

### Why this happens — the missing-parentheses rule

The macro was written as:

```c
#define SQR(x) (x*x)
```

It should have been written defensively as:

```c
#define SQR(x) ((x)*(x))
```

With the defensive version, `SQR(b+2)` expands to `((b+2)*(b+2))`, which DOES correctly
evaluate to `6*6=36`.

**The exam is specifically testing whether you notice the macro was written WITHOUT the
extra parentheses around `x`.** Always check: does every occurrence of the parameter
inside the macro body have its own parentheses? If not, assume the trap is active.

### General detection rule for macro questions

1. Write out the **literal text substitution** first — copy-paste the argument text into
   every position the parameter appears, exactly as-is, with no evaluation.
2. THEN apply standard C operator precedence to the resulting expression as a whole.
3. If the macro parameter lacks its own parentheses AND the caller passes an expression
   (not a bare variable/literal), expect a mismatch from the "obvious" squared/doubled
   result.

### Practice pattern (work this cold)

```c
#define DOUBLE(x) x+x
int result = 3 * DOUBLE(4);
```

**Step 1 — textual substitution:**

```
3 * DOUBLE(4)  →  3 * 4+4
```

**Step 2 — apply precedence** (`*` binds tighter than `+`):

```
(3*4) + 4 = 12 + 4 = 16
```

**Output: 16** — NOT `3 * (4+4) = 24`, which is what most people guess.

### Practice pattern 2 (work this cold)

```c
#define MIN(a,b) a < b ? a : b
int x = 5, y = 10;
int z = MIN(x, y) + 1;
```

**Step 1 — textual substitution:**

```
x < y ? x : y + 1
```

**Step 2 — apply precedence.** `?:` (ternary) has LOWER precedence than `+`, so this
does NOT group as `(x < y ? x : y) + 1` the way you'd expect from a function call. It
actually parses as:

```
x < y ? x : (y + 1)
```

Since `x < y` is true (5 < 10), the result is `x` = **5**, not `x+1 = 6` and not
`(x<y?x:y)+1 = 6` either.

**Output: 5**

This is one of the nastiest ISRO-style macro traps — unparenthesized macros combined
with operators of differing precedence outside the macro call. Whenever you see a macro
used inside a larger expression, always do the full text substitution first and
re-evaluate precedence from scratch across the _entire_ resulting line, not just within
the macro body.

---

## One-Page Cheat Sheet (memorize before the exam)

| Situation                                 | Rule                                                                                              |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `char *ptr; ptr = arr + n;`               | Pointer now refers to index `n` of `arr`                                                          |
| `*ptr = 'x';`                             | Overwrites the character at that position, in place, in the original array                        |
| `printf("%s", arr)` after a pointer edit  | Prints from index 0 — reflects the edit if it happened inside `arr`'s bounds                      |
| `printf("%s", ptr)` after `ptr = arr + n` | Prints from index `n` onward, NOT from index 0                                                    |
| `char - char` inside any arithmetic       | Evaluates as an ASCII integer difference, not a character                                         |
| `#define F(x) (x*x)` called as `F(a+b)`   | Expands to `(a+b*a+b)` — textual substitution, NOT `(a+b)*(a+b)`                                  |
| Any unparenthesized macro parameter       | Assume a precedence trap is being tested; do full text substitution before evaluating             |
| Macro used inside a larger expression     | Re-derive operator precedence across the WHOLE line after substitution, not just inside the macro |
