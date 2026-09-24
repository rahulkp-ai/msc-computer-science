# Object-Oriented Programming — PYQ + Important Questions with Explanations

Sourced from your 4 uploaded ISRO papers, plus **[Standard]** supplementary items.
Note: Java exception handling and execution-order tracing has its own dedicated file
(`Java-Exception-Handling.md`) — this file covers core OOP concepts (inheritance,
constructors, interfaces, access control, polymorphism).

---

## A. Constructors

**Q1 [VSSC 1386, Q3].** Which is a VALID constructor declaration for class `Book`?
(a) public String Book() (b) public float Book() (c) protected String Book()
(d) public Book()

**Answer: (d) public Book()**
**Explanation:** A constructor's name must EXACTLY match the class name, and it must
have **NO return type at all** — not even `void`. Options (a), (b), (c) all have a
return type specified (`String`, `float`), which makes them regular methods that
happen to share the class name, NOT constructors.

---

**Q2 [VSSC 1370, Q26].** Which statement(s) is/are WRONG about constructors in OOP?
I. The name of the constructor is same as class name
II. It can have a return value
III. Constructor is the first code invoked when an object is created
IV. Constructor name need not be the same as class name
(a) only 2 (b) only 3 (c) 2 and 4 (d) 2,3 and 4

**Answer: (c) 2 and 4**
**Explanation:** Statement I is TRUE (correct fact). Statement II is WRONG (constructors
never return a value). Statement III is TRUE (correct — constructor runs at object
creation). Statement IV is WRONG (directly contradicts statement I — name MUST match
class name). So the wrong statements are II and IV.

---

## B. Abstract Classes & Interfaces

**Q3 [VSSC 1370, Q25].** Which of the following is an abstract method?
(a) `void abstract abc(){}` (b) `public static final void(){}`
(c) `public abstract void abc();` (d) None of above

**Answer: (c) public abstract void abc();**
**Explanation:** Two critical rules for an abstract method: (1) the `abstract` keyword
comes BEFORE the return type (`public abstract void`, not `void abstract`), and (2) it
has NO method body — just a semicolon after the signature. Option (a) has the keyword
order wrong AND has empty braces `{}` (a body, even if empty, isn't allowed for
abstract methods). Option (c) correctly has no body at all.

---

**Q4 [VSSC 1386, Q2].** In OOP, what is an abstract method?
(a) A method which doesn't have any method body
(b) A method with only a return statement inside the method body
(c) A method which has a body with one statement inside it but no return statement
(d) None of the above

**Answer: (a)**
**Explanation:** Reinforces Q3 — an abstract method declares its signature but
provides NO implementation at all (no body, not even an empty one or a single
statement). It's meant to be implemented by a subclass.

---

**Q5 [VSSC 1386, Q9].** A pure abstract class where ALL methods are without a method
body is generally called: (a) Inner class (b) final abstract class
(c) interface (d) package

**Answer: (c) interface**
**Explanation:** This is the classic definition distinguishing an interface from a
regular abstract class: an interface is essentially "100% abstract" — every method is
implicitly abstract (pre-Java 8 default/static method additions aside), with zero
concrete implementation.

---

**Q6 [VSSC 1370, Q50].** Properties of an interface — which are TRUE?
I. Interface by default is an abstract class
II. Interface methods can be final or static
III. Interface methods cannot be final or static
IV. The methods of an interface are by default public and abstract
(a) only I and IV (b) only II and IV (c) I, II and IV (d) I, III and IV

**Answer: (a) only I and IV**
**Explanation:** Statement I is TRUE — an interface is conceptually/implicitly an
abstract type. Statement IV is TRUE — interface methods are `public abstract` by
default unless otherwise specified. Statement II is FALSE (in classic/pre-Java-8
interfaces, methods cannot be `final` since they must be overridden, and cannot be
plain instance `static` methods either in the older model) — so III (the negation of
II) would seem true, but the question's expected answer per the paper is (a), meaning
II is treated as false and III's negation isn't picked either — this reflects
classic/traditional interface rules (pre-Java 8 default/static method features). Stick
with the traditional rule set for ISRO exam purposes: interface methods are implicitly
`public abstract`, NOT final, NOT static (in the traditional model tested here).

---

## C. Inheritance & Access Control

**Q7 [SAC 2017/18, Q13].** _(See the companion Output-Tracing file, section 6, for the
full worked trace)_ — tests that a `private` constructor blocks subclass access,
causing a **compile-time error**.

---

**Q8 [VSSC 1386, Q29].** In OOPS concepts, how can you access a `protected` method of
class A from class B OUTSIDE the package?
(a) It can't be accessed
(b) It can be accessed only if class B inherits class A
(c) It can be accessed only within the same package, not from outside
(d) It can be accessed only if class B overloads class A

**Answer: (b) only if class B inherits class A**
**Explanation:** Access modifier visibility rules:

- `public` — accessible from anywhere
- `protected` — accessible within the same package, AND from subclasses even in a
  DIFFERENT package (this is the key exception protected provides over
  package-private)
- (default/package-private, no modifier) — accessible only within the same package
- `private` — accessible only within the declaring class itself

So a `protected` member CAN cross package boundaries, but only via inheritance — class
B must `extend` class A to access A's protected members from outside A's package.

---

**Q9 [VSSC 1370, Q9].** A class which CANNOT be inherited is called:
(a) static class (b) template class (c) abstract class (d) final class

**Answer: (d) final class**
**Explanation:** The `final` keyword, when applied to a class, prevents any other
class from extending it. (Note: `abstract class` is actually the OPPOSITE in spirit —
it's _designed_ to be inherited/extended, often cannot even be instantiated directly.
Don't confuse the two.)

---

**Q10 [VSSC 1370, Q59].** In object oriented programming, private methods of a class:
(a) can be accessed only within the class
(b) can be accessed by an object of the class that inherits it
(c) can be overridden by the class that extends it
(d) All of the above

**Answer: (a) can be accessed only within the class**
**Explanation:** `private` members are strictly scoped to the declaring class itself —
not accessible to subclasses (ruling out b and c), and definitionally cannot be
overridden since a subclass can't even see them to override.

---

**Q11 [SAC 2017/18, Q68].** Method overriding in Java is:
(a) Compile time polymorphism (b) Run time polymorphism (c) Not allowed
(d) Run time inheritance

**Answer: (b) Run time polymorphism**
**Explanation:** **Overriding** (subclass redefines a superclass method with the same
signature) is resolved at RUNTIME based on the actual object type — this is dynamic/
run-time polymorphism. **Overloading** (same method name, different parameter list,
within the same class) is resolved at COMPILE time based on the arguments passed —
that's compile-time/static polymorphism. This overriding-vs-overloading distinction is
one of the most frequently tested OOP concepts.

---

## D. C++-Specific OOP

**Q12 [SAC 2017/18, Q29].** Which statement is CORRECT about C++?
(a) C++ allows static type checking (b) C++ allows dynamic type checking
(c) C++ allows static member function to be of type const (d) Both (a) and (b)

**Answer: (d) Both (a) and (b)**
**Explanation:** C++ supports static type checking (most type errors caught at compile
time) AND some dynamic type checking mechanisms (e.g. `dynamic_cast`, RTTI - Run-Time
Type Information). Option (c) is false — a `static` member function in C++ cannot be
declared `const`, because `const` on a member function refers to not modifying the
_instance_ (`this` pointer), but static functions don't have a `this` pointer/instance
context at all, so applying `const` to them is meaningless and disallowed.

---

**Q13 [SHAR 2015, Q41].** A function that can access private members of a class, even
though it is not a member of the class itself, is:
(a) A Private function (b) A friend function (c) An inline function
(d) Not possible

**Answer: (b) A friend function**
**Explanation:** C++'s `friend` keyword grants a non-member function (or another
class) special access to a class's private/protected members — a deliberate exception
to normal encapsulation rules, used sparingly for tightly coupled helper functions
(e.g. operator overloading that needs to access both operands' internals).

---

**Q14 [SHAR 2015, Q8].** Which keyword specifies the compiler to substitute the code
within the function definition for every instance of a function call?
(a) virtual (b) static (c) inline (d) public

**Answer: (c) inline**
**Explanation:** `inline` is a compiler HINT (not a guarantee) suggesting the function
body be substituted directly at each call site instead of a normal function call,
avoiding call-overhead for small, frequently-called functions.

---

## E. UML & OOP Design (bridges into Software Engineering)

**Q15 [VSSC 1386, Q5].** Which of the following is NOT a part of UML?
(a) Use-case diagram (b) Class diagram (c) Entity Relationship diagram
(d) Sequence diagram

**Answer: (c) Entity Relationship diagram**
**Explanation:** ER diagrams are a DATABASE modeling tool (part of DBMS design), NOT
part of the UML (Unified Modeling Language) family, which covers Use-case, Class,
Sequence, Activity, State, Component, Deployment diagrams, etc. — all related to
software/object-oriented system design.

---

## F. OOP Languages

**Q16 [VSSC 1370, Q65].** Which of the following are object-oriented programming
languages? I. JAVA II. C III. C++ IV. BASIC
(a) Only I and III (b) Only II and III (c) Only III and IV (d) I, III and IV

**Answer: (a) Only I and III**
**Explanation:** Java and C++ are both OOP languages. **C is NOT object-oriented** (it
is procedural — no classes, inheritance, or encapsulation natively). BASIC, in its
classic/traditional form, is also not OOP (though some modern dialects like
Visual Basic .NET added OOP features — traditional BASIC as typically referenced in
exams is not).

---

## Cheat Sheet — Memorize Before the Exam

| Concept                    | Key Fact                                                                           |
| -------------------------- | ---------------------------------------------------------------------------------- |
| Constructor rules          | Same name as class, NO return type (not even void), runs first at object creation  |
| Abstract method            | Declared with `abstract` keyword BEFORE return type, NO body, ends in `;`          |
| Interface (traditional)    | 100% abstract, methods implicitly `public abstract`, not final, not static         |
| `final` class              | Cannot be inherited/extended                                                       |
| `abstract` class           | Designed TO BE inherited, often can't be instantiated directly                     |
| private members            | Accessible ONLY within the declaring class — not subclasses, not other classes     |
| protected members          | Accessible within same package AND by subclasses even outside the package          |
| Overriding                 | Runtime/dynamic polymorphism — resolved by actual object type at runtime           |
| Overloading                | Compile-time/static polymorphism — resolved by argument list at compile time       |
| C++ friend function        | Non-member function granted access to private/protected members                    |
| C++ inline                 | Hints the compiler to substitute function body at call site (avoids call overhead) |
| C++ static member function | Cannot be `const` (no `this` pointer to apply const-ness to)                       |
| ER diagrams                | NOT part of UML — that's a database-modeling tool, UML is OOP/software design      |
| OOP languages here         | Java, C++ — NOT C (procedural), NOT traditional BASIC                              |
