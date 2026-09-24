# Software Engineering — PYQ + Important Questions with Explanations

Sourced from your 4 uploaded ISRO papers, plus **[Standard]** supplementary items.

---

## A. SDLC Models

**Q1 [VSSC 1370, Q1].** Which of the following is a Software Development Life Cycle
Model? (a) Data Warehouse (b) Data Model (c) Waterfall Model (d) Data Mart

**Answer: (c) Waterfall Model**
**Explanation:** A warm-up definitional question — Data Warehouse/Data Model/Data Mart
are all DBMS/data-architecture concepts, not SDLC models. Know the standard SDLC model
list: Waterfall, Iterative, Spiral, V-Model, Agile, Prototyping, RAD.

---

**Q2 [SHAR 2015, Q26].** The simplest model in software development is:
(a) Prototyping (b) Iterative (c) Waterfall (d) Spiral

**Answer: (c) Waterfall**
**Explanation:** Waterfall is the original, simplest, strictly sequential model —
each phase (Requirements → Design → Implementation → Testing → Maintenance) completes
fully before the next begins, with no overlap or iteration back to earlier phases.

---

**Q3 [SHAR 2015, Q30].** For a software project, the spiral model was employed. When
will the spiral stop?
(a) When the software product is retired
(b) When the software product is released after Beta testing
(c) When the risk analysis is completed
(d) After completing five loops

**Answer: (a) When the software product is retired**
**Explanation:** The Spiral model is explicitly designed as a CONTINUOUS,
risk-driven, iterative process — it doesn't have a fixed number of cycles built in;
each loop through the spiral (Planning → Risk Analysis → Engineering → Evaluation)
represents a phase of the product's life, continuing indefinitely until the product is
finally retired/discontinued.

---

**Q4 [VSSC 1370, Q14].** In the V model of software development, Integration Test
Plan is prepared during which phase? (a) Coding (b) Design (c) Requirements
(d) Software maintenance

**Answer: (b) Design**
**Explanation:** The V-model pairs each development phase with a corresponding testing
phase planned in parallel (though executed later). Integration Test PLANNING
corresponds to the DESIGN phase (specifically, high-level/architectural design, since
integration testing verifies how modules interact — a design-level concern), even
though the actual integration TESTING happens much later, after coding.

---

## B. Cohesion, Coupling, Modularity

**Q5 [VSSC 1370, Q34].** The degree of intra-dependability within the elements of a
software module is called: (a) Coupling (b) Concurrency (c) Cohesion
(d) Modularisation

**Answer: (c) Cohesion**
**Explanation:** **Cohesion** = how closely related and focused the elements WITHIN a
single module are (internal, "intra"). **Coupling** = how much modules depend on EACH
OTHER (external, "inter"). Good design wants HIGH cohesion + LOW coupling.

---

**Q6 [VSSC 1386, Q16].** In the context of modular software design, which combination
is DESIRABLE?
(a) High cohesion and high coupling (b) High cohesion and low coupling
(c) Low cohesion and high coupling (d) Low cohesion and low coupling

**Answer: (b) High cohesion and low coupling**
**Explanation:** This is THE fundamental software design principle — modules should be
internally focused/self-contained (high cohesion) while being as independent from each
other as possible (low coupling), making the system easier to maintain, test, and
modify without ripple effects.

---

**Q7 [VSSC 1370, Q27].** The number of modules that call a given module is called:
(a) Fan-in (b) Fan-out (c) Cardinality (d) None of these

**Answer: (a) Fan-in**
**Explanation:** **Fan-in** = how many OTHER modules call INTO this module (measures
reuse). **Fan-out** = how many OTHER modules THIS module calls OUT to (measures
complexity/dependency — high fan-out can indicate a module doing too much).

---

## C. Testing — Types & Terminology

**Q8 [VSSC 1370, Q73].** Testing carried out by users at their own locations is called:
(a) Beta Testing (b) Alpha Testing (c) Regression Testing (d) Monkey Testing

**Answer: (a) Beta Testing**
**Explanation:** **Alpha testing** happens at the DEVELOPER's site (often by internal
staff/QA). **Beta testing** happens at the USER's/customer's own site, with real users,
before final release. This pairing (alpha=developer site, beta=user site) is tested
constantly.

---

**Q9 [SHAR 2015, Q43].** The testing method generally used as an ACCEPTANCE test for a
software system is: (a) Unit testing (b) Integration testing (c) System testing
(d) Regression testing

**Answer: (c) System testing**
**Explanation:** Acceptance testing is typically performed as (or closely follows) full
SYSTEM testing — testing the complete, integrated system against the full requirements
specification, as the final validation gate before delivery/acceptance by the customer.

---

**Q10 [VSSC 1386, Q15].** Which statement(s) is/are FALSE about software testing?
S1: White-box tests are based on specifications
S2: Black-box tests are based on code
S3: Alpha testing is conducted at the developer's site
(a) Only S1 and S2 (b) Only S1 and S3 (c) Only S2 and S3 (d) All of S1,S2,S3

**Answer: (a) Only S1 and S2 are FALSE**
**Explanation:** These two statements are SWAPPED/reversed from the truth:
- **White-box testing** is based on internal CODE/structure knowledge (not
  specifications) — so S1 is false.
- **Black-box testing** is based on SPECIFICATIONS/requirements, with no knowledge of
  internal code — so S2 is false (it says the opposite).
- S3 is TRUE (matches Q8's alpha=developer-site fact above), so it's correctly listed
  as NOT false.

---

**Q11 [VSSC 1386, Q40].** An integration testing approach where all modules are
individually tested, then integrated and tested as a whole, is called:
(a) Sandwich testing (b) Big bang testing (c) Bottom Up testing (d) Top Down testing

**Answer: (b) Big bang testing**
**Explanation:** "Big bang" integration tests each module independently first, then
combines ALL of them together at once (a single "big bang" integration) rather than
incrementally. Compare with Top-Down (start with high-level modules, integrate
downward, using stubs for lower modules not yet built) and Bottom-Up (start with
low-level modules, integrate upward, using drivers to simulate higher modules).

---

**Q12 [VSSC 1386, Q60].** Choose the CORRECT statement about Top-down vs Bottom-up
testing.
(a) Stubs essential in Top-down; Test Drivers essential in Bottom-up
(b) Test Drivers essential in Top-down; Stubs essential in Bottom-up
(c) Stubs and test drivers both essential in Top-down
(d) None of the above statements is correct

**Answer: (a)**
**Explanation:** ⚠️ Memorize this pairing carefully, it's easy to reverse:
- **Top-Down** testing starts with high-level modules; the LOWER modules they call
  don't exist yet, so you need **STUBS** (dummy placeholder implementations of the
  not-yet-built lower modules).
- **Bottom-Up** testing starts with low-level modules; there's no higher-level caller
  yet, so you need a **DRIVER** (a dummy program that calls/tests the low-level module
  directly).

---

**Q13 [VSSC 1386, Q41].** Which is NOT a performance testing method?
(a) Load testing (b) Penetration testing (c) Stress testing (d) Volume testing

**Answer: (b) Penetration testing**
**Explanation:** Load, Stress, and Volume testing are all *performance*-related
(how the system behaves under various load/data conditions). Penetration testing is a
SECURITY testing technique (simulating an attack to find vulnerabilities) — a
completely different testing category.

---

**Q14 [VSSC 1386, Q59].** Technique used to evaluate the QUALITY of test cases
themselves is called: (a) Mutation Testing (b) Regression Testing (c) Alpha testing
(d) Debugging

**Answer: (a) Mutation Testing**
**Explanation:** Mutation testing deliberately introduces small artificial bugs
("mutants") into the code, then checks whether your existing test suite catches them —
if a mutant survives (tests still pass despite the injected bug), it reveals a
weakness in your test cases' coverage/quality.

---

## D. Software Metrics & Reliability

**Q15 [VSSC 1386, Q34].** Probability of failure-free operation of a system over a
specified time within a specified environment for a specified purpose is called:
(a) Robustness (b) Efficiency (c) Reliability (d) Durability

**Answer: (c) Reliability**
**Explanation:** This is the textbook definition of software Reliability — a
probability-based measure of failure-free operation under defined conditions and time.

---

**Q16 [VSSC 1386, Q50 — worked example].**
What is the availability of software given: Mean Time Between Failure (MTBF) = 25
days, Mean Time To Repair (MTTR) = 6 hours?

**Working:**
- Availability = MTBF / (MTBF + MTTR) — both must be in the SAME units
- Convert MTBF to hours: 25 days × 24 = 600 hours
- Availability = 600 / (600 + 6) = 600/606 ≈ **0.9901** = **99.009%**

**Answer: (d) 99.009%**
**Explanation:** The Availability formula (`MTBF / (MTBF + MTTR)`) is a reusable
pattern — always convert both quantities to the same unit BEFORE plugging into the
formula; unit mismatches (days vs hours) are the most common source of error here.

---

## E. Decision Tables & Requirements

**Q17 [SAC 2017/18, Q43].** A decision table consists of two parts:
(a) Sub and Entry (b) Pros and Cons (c) Condition and result (d) None of the above

**Answer: (c) Condition and result**
**Explanation:** A decision table has a **Condition stub/entries** section (the
various input conditions and their possible combinations) and an **Action
stub/entries** section (the resulting action to take for each combination) — this is
often more precisely described as "condition and action," matching option (c)'s intent.

---

## Cheat Sheet — Memorize Before the Exam

| Concept | Key Fact |
|---|---|
| Waterfall model | Simplest, strictly sequential, no phase overlap |
| Spiral model | Continuous risk-driven iteration; stops only at product retirement |
| Cohesion vs Coupling | Cohesion = internal focus (want HIGH); Coupling = inter-module dependency (want LOW) |
| Fan-in vs Fan-out | Fan-in = modules calling INTO this one; Fan-out = modules THIS one calls OUT to |
| Alpha vs Beta testing | Alpha = developer's site; Beta = user's/customer's site |
| White-box vs Black-box | White-box = based on code/internal structure; Black-box = based on specifications, no code knowledge |
| Top-down vs Bottom-up testing | Top-down needs STUBS (for missing lower modules); Bottom-up needs DRIVERS (for missing higher callers) |
| Availability formula | MTBF / (MTBF + MTTR), same units for both |
| Mutation testing | Tests the QUALITY of your test cases themselves, via injected artificial bugs |
| Reliability (definition) | Probability of failure-free operation over a specified time/environment |
