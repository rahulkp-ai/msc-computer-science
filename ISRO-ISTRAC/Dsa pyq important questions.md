# Data Structures & Algorithms — PYQ + Important Questions with Explanations

Sourced from your 4 uploaded ISRO papers, plus **[Standard]** supplementary items.
Note: pure "trace the C/C++ code" style DSA questions are covered in the companion
`C-CPP-Java-Output-Tracing.md` file — this file focuses on DSA _concepts and
properties_, which is the more common ISRO question style for this subject.

---

## A. Arrays & Random Access

**Q1 [SHAR 2015, Q2].** The data structure which is best suited for RANDOM ACCESS is:
(a) array (b) linked list (c) queue (d) stack

**Answer: (a) array**
**Explanation:** Arrays provide O(1) constant-time access to any element via direct
index calculation (`base_address + index × element_size`). Linked lists require
O(n) traversal from the head to reach an arbitrary element — no direct indexing.

---

**Q2 [SAC 2017/18, Q58].** If `arr` is a 2D array of 10 rows and 12 columns, then
`arr[5]` logically points to the: (a) sixth row (b) fifth row (c) fifth column
(d) sixth column

**Answer: (a) sixth row**
**Explanation:** ⚠️ Indexing starts at 0 — `arr[5]` refers to the row at INDEX 5,
which is the SIXTH row when counting from 1. This 0-indexing trap is worth
double-checking every time.

---

**Q3 [VSSC 1386, Q25 — worked example].**
`int Data[2][4] = {10,20,30,40,50,60,70,80};`
Value 30 can be accessed as \_\_\_ (assume row-major order).
(a) Data[0][3] (b) Data[1][2] (c) Data[2][3] (d) Data[0][2]

**Working:** Row-major means the array fills row by row:
Row 0: [10, 20, 30, 40], Row 1: [50, 60, 70, 80]
30 is the 3rd element of Row 0 → index [0][2]

**Answer: (d) Data[0][2]**
**Explanation:** Always physically lay out the 2D array in a grid based on row-major
fill order before answering — don't try to compute this purely from the linear index
formula unless you're fully comfortable with it.

---

## B. Complexity Analysis

**Q4 [SHAR 2015, Q9].** Which function has the HIGHEST growth?
(a) f(n) = O(n log n) (b) f(n) = O(n²) (c) f(n) = O(n³) (d) f(n) = O(2ⁿ)

**Answer: (d) O(2ⁿ)**
**Explanation:** Standard growth-rate ordering from slowest to fastest:
`O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2ⁿ) < O(n!)`
Exponential growth (2ⁿ) always eventually outpaces any polynomial (n^k, for any fixed
k), no matter how large the polynomial's exponent.

---

**Q5 [VSSC 1370, Q42].** Time complexity of binary search algorithm for N elements is:
(a) O(N²) (b) O(logN) (c) O(N³) (d) O(1)

**Answer: (b) O(logN)**
**Explanation:** Binary search halves the search space with each comparison — this
gives logarithmic time complexity. (Requires the array to be sorted, which is why the
next question matters.)

---

**Q6 [SHAR 2015, Q3].** Binary search is optimal when the elements are:
(a) sorted in ascending order (b) sorted in descending order (c) any of the above
(d) unsorted

**Answer: (c) any of the above (sorted, ascending OR descending)**
**Explanation:** Binary search's core requirement is simply that the array be SORTED
(in either consistent direction) — the algorithm just needs to know which direction to
adjust its comparison logic. It does NOT work on unsorted data.

---

**Q7 [VSSC 1370, Q53].** Time complexity of Bubble sort for N elements is:
(a) O(N²) (b) O(NlogN) (c) O(N³) (d) O(1)

**Answer: (a) O(N²)**
**Explanation:** Bubble sort's nested-loop comparison structure gives worst-case and
average-case O(N²). Memorize the standard sorting complexity table below.

---

**Q8 [SHAR 2015, Q42].** The average successful search time for sequential search of
'n' terms is: (a) n/2 (b) (n+1)/2 (c) log₂n (d) n(n+1)/2

**Answer: (b) (n+1)/2**
**Explanation:** For a successful sequential search across `n` elements (uniformly
likely to be at any position), the average number of comparisons is `(1+2+...+n)/n =
(n+1)/2`. This is subtly different from the simpler-sounding "n/2" — always derive it
from the sum formula rather than guessing.

---

## C. Stacks & Queues

**Q9 [VSSC 1370, Q39].** Consider:
I. LIFO computations are efficiently supported by QUEUE
II. FIFO computations are efficiently supported by STACK
(a) Only I is correct (b) Only II is correct (c) Both are correct
(d) Both are Wrong

**Answer: (d) Both are Wrong**
**Explanation:** This is REVERSED from the truth: **STACK is naturally LIFO** (Last In
First Out — think of a stack of plates), and **QUEUE is naturally FIFO** (First In
First Out — think of a line at a ticket counter). The statements swap these, making
both false.

---

**Q10 [VSSC 1386, Q26].** A stack is useful for:
(a) Breadth First Search (b) Recursion (c) Queue in a ticket counter
(d) Accessing elements using index

**Answer: (b) Recursion**
**Explanation:** Recursive function calls are managed via the **call stack** — each
call pushes a new stack frame, and returning pops it. This is precisely why deep
uncontrolled recursion causes a "stack overflow." (BFS uses a QUEUE, not a stack — DFS
is the one that naturally maps to a stack/recursion.)

---

**Q11 [VSSC 1370, Q46 — worked example].**
Sequence of operations on a stack: `PUSH(32), PUSH(4), POP, PUSH(56), POP, POP`
What is the sequence of values popped out?

**Working (trace the stack, LIFO):**

1. PUSH(32) → stack: [32]
2. PUSH(4) → stack: [32, 4]
3. POP → pops **4** (top of stack) → stack: [32]
4. PUSH(56) → stack: [32, 56]
5. POP → pops **56** → stack: [32]
6. POP → pops **32** → stack: []

**Answer: 4, 56, 32**
**Explanation:** The golden rule for tracing stack operations: always remove from the
TOP (the most recently pushed item) — never the bottom.

---

**Q12 [VSSC 1370, Q40].** The expression `a b c + -` is written in which form?
(a) Infix (b) postfix (c) prefix (d) lastfix

**Answer: (b) postfix**
**Explanation:** Postfix (Reverse Polish Notation) places operators AFTER their
operands. `a b c + -` means: `c+` comes after `b`,`c` → compute `b+c` first, then
subtract that result from `a` → equivalent to infix `a - (b+c)`.

---

**Q13 [VSSC 1370, Q52].** Which data structure is BEST suited to match parentheses in
an arithmetic expression? (a) Linked List (b) List (c) Queue (d) Stack

**Answer: (d) Stack**
**Explanation:** Push each opening bracket; when a closing bracket appears, pop and
check it matches the type. This LIFO matching is the standard, textbook stack
application — memorize it as a fixed pairing (parenthesis-matching = stack, always).

---

**Q14 [VSSC 1386, Q27].** If a Queue is implemented with a linked list with two
pointers `front` and `rear`, what is the time complexity to insert an element?
(a) O(log n) (b) O(n log n) (c) O(n²) (d) O(1)

**Answer: (d) O(1)**
**Explanation:** With a `rear` pointer maintained explicitly, inserting (enqueueing) at
the rear is a direct pointer operation — no traversal needed, hence constant time.
(Without a `rear` pointer, you'd need O(n) to traverse to the end first — this is why
the question specifically states "with two pointers front and rear.")

---

## D. Linked Lists

**Q15 [SHAR 2015, Q45].** What is the minimum number of fields with each node of a
doubly linked list? (a) 2 (b) 3 (c) 4 (d) 5

**Answer: (b) 3**
**Explanation:** A doubly linked list node needs: (1) data field, (2) pointer to next
node, (3) pointer to previous node = 3 minimum fields. (Compare: a singly linked list
node needs only 2 — data + next pointer.)

---

**Q16 [VSSC 1386, Q28].** What is the minimum number of fields with each node of a
double linked list which can store one integer data? (a) 1 (b) 2 (c) 3 (d) 4

**Answer: (c) 3**
**Explanation:** Same underlying fact as Q15 — restated with a slightly different
wording. This exact concept (doubly linked list node = 3 minimum fields) has appeared
in TWO of your four papers — a strong signal it's a reliably recurring question.

---

## E. Hashing

**Q17 [Standard].** What is a collision in hashing, and name two common resolution
techniques.
**Answer:** A collision occurs when two different keys hash to the same
index/bucket. Common resolution techniques:

- **Chaining** — each bucket holds a linked list of all entries hashing to it
- **Open addressing** (linear probing, quadratic probing, double hashing) — on
  collision, probe for the next available slot according to some rule

---

## Sorting Complexity Cheat Sheet — Memorize Before the Exam

| Algorithm         | Best       | Average    | Worst      | Notes                                                     |
| ----------------- | ---------- | ---------- | ---------- | --------------------------------------------------------- |
| Bubble Sort       | O(n)       | O(n²)      | O(n²)      | Simple, rarely used in practice                           |
| Selection Sort    | O(n²)      | O(n²)      | O(n²)      | Always O(n²) regardless of input order                    |
| Insertion Sort    | O(n)       | O(n²)      | O(n²)      | Efficient for nearly-sorted data                          |
| Merge Sort        | O(n log n) | O(n log n) | O(n log n) | Stable, needs O(n) extra space                            |
| Quick Sort        | O(n log n) | O(n log n) | O(n²)      | Worst case on already-sorted input with poor pivot choice |
| Heap Sort         | O(n log n) | O(n log n) | O(n log n) | In-place, not stable                                      |
| Binary Search     | O(1)       | O(log n)   | O(log n)   | Requires sorted array                                     |
| Sequential Search | O(1)       | O(n)       | O(n)       | Average successful search: (n+1)/2                        |

## General Cheat Sheet

| Concept                 | Key Fact                                                                                   |
| ----------------------- | ------------------------------------------------------------------------------------------ |
| Stack                   | LIFO — used for recursion, parenthesis matching, expression evaluation, undo functionality |
| Queue                   | FIFO — used for BFS, scheduling, buffering                                                 |
| Doubly linked list node | Minimum 3 fields: data, next, prev                                                         |
| Singly linked list node | Minimum 2 fields: data, next                                                               |
| Array random access     | O(1) — best data structure when index-based access dominates                               |
| Growth rate ordering    | 1 < log n < n < n log n < n² < n³ < 2ⁿ < n!                                                |
