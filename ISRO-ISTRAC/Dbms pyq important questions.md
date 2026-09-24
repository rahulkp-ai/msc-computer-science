# DBMS — PYQ + Important Questions with Explanations

Sourced from your 4 uploaded ISRO papers, plus **[Standard]** supplementary items.

---

## A. Relational Model, Keys, Schema

**Q1 [SHAR 2015, Q21].** The schema of a table is an example of:
(a) Atomicity (b) Entity (c) Relationship (d) Metadata

**Answer: (d) Metadata**
**Explanation:** A schema describes the _structure_ of the table (column names, types,
constraints) — data about the data — which is precisely what "metadata" means. The
actual rows are the data; the schema is metadata.

---

**Q2 [SAC 2017/18, Q27].** Primary key combined with a foreign key creates:
(a) Parent-Child relationship between the tables that connect them
(b) Many to many relationship between the tables that connect them
(c) Network model between the tables that connect them
(d) None of the above

**Answer: (a) Parent-Child relationship**
**Explanation:** A foreign key in one table (the "child") refers to the primary key of
another table (the "parent"), establishing a referential link — this is the standard
mechanism for representing one-to-many relationships in the relational model.

---

**Q3 [VSSC 1370, Q44].** The purpose of a foreign key in a table is to ensure:
(a) Null integrity (b) Domain integrity (c) Null and Domain Integrity
(d) Referential integrity

**Answer: (d) Referential Integrity**
**Explanation:** Referential integrity means every foreign key value must either match
an existing primary key value in the referenced table, or be NULL (if allowed) —
preventing "orphan" references to non-existent rows.

---

**Q4 [SAC 2017/18, Q74].** Cross Product in DBMS is a:
(a) Unary Operator (b) Ternary Operator (c) Binary Operator (d) Not an operator

**Answer: (c) Binary Operator**
**Explanation:** Cartesian/Cross Product takes exactly TWO relations as input and
produces a combined relation with every possible pairing of rows — a classic binary
relational algebra operation (like Union, Intersection, Join).

---

**Q5 [SAC 2017/18, Q64].** "Row" is synonymous with the term:
(a) record (b) relation (c) column (d) field

**Answer: (a) record**
**Explanation:** Standard relational-model terminology mapping:

- Row = Record = Tuple
- Column = Field = Attribute
- Table = Relation
  Memorize this triple-synonym mapping — ISRO likes to test it from any direction.

---

**Q6 [SAC 2017/18, Q48].** E-R model uses this symbol to represent a WEAK entity set:
(a) Dotted rectangle (b) Diamond (c) Doubly outlined rectangle (d) None

**Answer: (c) Doubly outlined rectangle**
**Explanation:** Standard ER diagram notation: Rectangle = entity, Doubly-outlined
rectangle = weak entity, Diamond = relationship, Doubly-outlined diamond = identifying
relationship (connects a weak entity to its owner).

---

## B. Normalization

**Q7 [SHAR 2015, Q24].** Which normal form is considered ADEQUATE for normal
relational database design? (a) 1NF (b) 2NF (c) 3NF (d) 4NF

**Answer: (c) 3NF**
**Explanation:** 3NF is generally considered the practical sweet spot for most database
designs — it eliminates transitive dependencies while remaining relatively easy to
achieve. BCNF is a stricter form used when specific anomalies from 3NF still exist;
4NF/5NF handle more exotic multi-valued dependency cases, rarely needed in typical
designs.

---

**Q8 [VSSC 1370, Q58].** In DBMS, what is the advantage of Normalization?
(a) Helps in Data Hiding (b) Removes Data Redundancy (c) Encrypts Data
(d) Reduces Number of Tables

**Answer: (b) Removes Data Redundancy**
**Explanation:** The core purpose of normalization is eliminating redundant data
storage (and the update/insert/delete anomalies that come with it) by decomposing
tables based on functional dependencies. Note: normalization typically _increases_ the
number of tables (option d is the opposite of true), doesn't encrypt anything, and
isn't related to access-control "data hiding."

---

**Q9 [VSSC 1386, Q51].** Consider the following statements of RDBMS:
I. Every relation in 3NF is also in BCNF
II. Every relation in BCNF is also in 3NF
Which is/are correct? (a) Only I (b) Both I and II (c) Both I and II are wrong
(d) Only II

**Answer: (d) Only II**
**Explanation:** BCNF is STRICTER than 3NF — so every BCNF relation automatically
satisfies 3NF (statement II, true). But the reverse isn't guaranteed: a relation can
satisfy 3NF while still having anomalies that only BCNF eliminates (statement I,
false). Direction matters: BCNF ⊆ 3NF (as a set of qualifying relations), not the other
way around.

---

## C. SQL Query Reading & Writing

**Q10 [VSSC 1370, Q57 — worked example].**
Table: EMPLOYEE (EmpID, EmpName, EmpCity, EmpDivision)
Query: `SELECT EmpName FROM EMPLOYEE WHERE EmpCity='Mumbai' AND EmpDivision='Accounts'`

What does this query find?
(a) employee IDs from Mumbai AND working in Accounts
(b) employee names from Mumbai AND working in Accounts
(c) employee names NOT from Mumbai AND working in Accounts
(d) employee names from Mumbai OR working in Accounts

**Answer: (b)**
**Explanation:** `SELECT EmpName` → returns names, not IDs (eliminates option a).
`WHERE ... AND ...` → BOTH conditions must be true (eliminates the OR option d, and the
negated option c). Read SQL queries left to right, matching each clause carefully — the
exam deliberately creates near-identical wrong options differing by one word (AND→OR,
NOT inserted, etc.).

---

**Q11 [VSSC 1386, Q17 — worked example].**
Table `student` stores marks for a class. Query:

```sql
DELETE FROM student
WHERE marks < (SELECT avg(marks) FROM student);
```

What does this do?
(a) deletes all records from student
(b) deletes all rows where marks is less than the average mark
(c) deletes the mark column where the value is below average
(d) syntactically wrong, does not execute

**Answer: (b)**
**Explanation:** The subquery `(SELECT avg(marks) FROM student)` computes the average
mark FIRST, then the outer `DELETE` removes every row whose `marks` value is below that
computed average. This is a very common "DELETE with a correlated/scalar subquery"
pattern — always resolve the inner subquery's meaning first, then apply the outer
statement's logic using that result.

---

**Q12 [SHAR 2015, Q22].** To be considered minimally relational, the DBMS should
support which relational functions?
(a) SELECT, PROJECT, JOIN (b) SELECT, UNION, JOIN (c) SELECT, PROJECT, UNION
(d) SELECT, UNION, INTERSECT

**Answer: (a) SELECT, PROJECT, JOIN**
**Explanation:** This is a standard (Codd's rules-adjacent) definitional fact — the
three core operations considered the minimum bar for a system to be called
"relational": SELECT (filter rows), PROJECT (filter columns), JOIN (combine tables).

---

**Q13 [SHAR 2015, Q23].** In SQL, which command(s) is/are used to remove rows from a
table? (a) TRUNCATE (b) REMOVE (c) DELETE (d) Both (a) and (b)

**Answer:** Both TRUNCATE and DELETE remove rows — check the exact options given, but
the conceptually correct set is **TRUNCATE and DELETE** (REMOVE is not a valid SQL
keyword for this purpose). If the paper's options don't include a "both TRUNCATE and
DELETE" choice, the single best answer is **DELETE** (the more general-purpose,
row-by-row, WHERE-clause-capable command), with TRUNCATE being the faster
whole-table-only alternative.

---

**Q14 [VSSC 1386, Q35].** Which is TRUE regarding TRUNCATE and DROP?
(a) TRUNCATE can be rolled back; DROP cannot
(b) DROP can be rolled back; TRUNCATE cannot
(c) Both TRUNCATE and DROP CANNOT be rolled back
(d) Both TRUNCATE and DROP CAN be rolled back

**Answer: (c) Both cannot be rolled back**
**Explanation:** Both TRUNCATE and DROP are **DDL (Data Definition Language)**
commands, and DDL statements auto-commit in most RDBMSs — they cannot be rolled back
the way DML statements (INSERT/UPDATE/DELETE, which support ROLLBACK within a
transaction) can. Note: this behavior can vary slightly by specific RDBMS/settings, but
for exam purposes, memorize DDL = no rollback, DML = supports rollback (until
committed).

---

**Q15 [VSSC 1386, Q74].** Which is NOT a built-in aggregate function in SQL?
(a) avg (b) max (c) total (d) count

**Answer: (c) total**
**Explanation:** Standard SQL aggregate functions: `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`.
`TOTAL` is not a standard SQL aggregate function (though some specific databases like
SQLite have a non-standard `TOTAL()` function — for ISRO's purposes, treat it as NOT
standard SQL).

---

**Q16 [VSSC 1386, Q33].** INSERT operation is fastest in:
(a) Hash file organisation (b) Heap file organisation (c) B+ tree file organisation
(d) Clustered file organisation

**Answer: (b) Heap file organisation**
**Explanation:** Heap (unordered) file organization simply appends new records
wherever there's free space — no sorting, no index restructuring needed, making INSERT
the fastest among these options. B+ tree and clustered organizations must maintain
sort order/index structure on every insert, which is slower.

---

## D. Transactions & ACID

**Q17 [VSSC 1370, Q74].** Which is NOT a part of the ACID properties of a database
transaction? (a) Applicability (b) Consistency (c) Isolation (d) Durability

**Answer: (a) Applicability**
**Explanation:** ACID = **A**tomicity, **C**onsistency, **I**solation, **D**urability.
"Applicability" is not one of the four — this question format (list 3 real ones + 1
fake-sounding one) is a common ISRO trap style; always be ready to spot the impostor
term.

---

**Q18 [VSSC 1370, Q54].** Consider the following statements:
I. The value of an attribute can be NULL
II. Primary key helps to find out all other attributes
Choose the CORRECT answer:
(a) Only I is correct (b) Both I and II are correct (c) Both I and II are wrong
(d) Only II is correct

**Answer: (d) Only II is correct**
**Explanation:** Statement I is FALSE for a **primary key** specifically — primary key
attributes CANNOT be NULL (this is one of the two defining rules of a primary key,
along with uniqueness). Note the question's phrasing carefully: if it's asking about
"an attribute" generally (not specifically the primary key), NULL is allowed for
regular attributes — but the pairing with statement II (about primary keys uniquely
determining other attributes, which is the definition of a candidate/primary key)
signals the intended context is primary-key-related, making I false.

---

**Q19 [VSSC 1370, Q60].** Which locking provides the HIGHEST degree of concurrency in a
relational database management system?
(a) Page locking (b) Row locking (c) Table locking (d) Database locking

**Answer: (b) Row locking**
**Explanation:** The finer-grained the lock, the MORE concurrent transactions can
proceed simultaneously (since fewer resources are blocked per transaction). Row-level
locking is the finest granularity among these options → highest concurrency. Table/
database-level locking blocks the most, reducing concurrency the most.

---

## E. File Organization, Indexing, Hashing

**Q20 [SHAR 2015, Q25 — worked example].**
A hash function is defined as h(i) = i² mod 8. What is the value of h(8)?
(a) 0 (b) 8 (c) 64 (d) 16

**Working:** h(8) = 8² mod 8 = 64 mod 8 = **0**

**Answer: (a) 0**
**Explanation:** Simple substitution + modulo — but a common careless error is
forgetting to apply `mod 8` at the end after squaring. Always finish the FULL formula.

---

## F. Data Warehousing & Modern DB Concepts

**Q21 [VSSC 1386, Q68].** Which is the most suitable Data Warehouse use case?
(a) Online Air ticket booking (b) Online banking transactions
(c) Online Hospital registration system (d) Climate change analysis

**Answer: (d) Climate change analysis**
**Explanation:** Data warehouses are optimized for **OLAP** (Online Analytical
Processing) — large-scale historical analysis, trend detection, reporting over huge
datasets. Options a, b, c are all **OLTP** (Online Transaction Processing) use cases —
frequent, small, real-time read/write transactions — which need a normal operational
database, not a warehouse.

---

## Cheat Sheet — Memorize Before the Exam

| Term                       | Synonym mapping |
| -------------------------- | --------------- |
| Row = Record = Tuple       |                 |
| Column = Field = Attribute |                 |
| Table = Relation           |                 |

| Concept                      | Key Fact                                                                        |
| ---------------------------- | ------------------------------------------------------------------------------- |
| ACID                         | Atomicity, Consistency, Isolation, Durability                                   |
| Minimally relational ops     | SELECT, PROJECT, JOIN                                                           |
| Primary key rules            | Unique + NOT NULL                                                               |
| BCNF vs 3NF                  | BCNF ⊆ 3NF (every BCNF relation is in 3NF, not vice versa)                      |
| TRUNCATE/DROP vs DELETE      | DDL (no rollback) vs DML (rollback-capable within a transaction)                |
| Row locking vs Table locking | Finer granularity = higher concurrency                                          |
| OLTP vs OLAP                 | Frequent small transactions vs large-scale historical analysis (data warehouse) |
| Heap file organization       | Fastest INSERT (no ordering/index maintenance)                                  |
| ER diagram symbols           | Rectangle=entity, Doubly-outlined rectangle=weak entity, Diamond=relationship   |
