# ISRO ISTRAC / SAC / VSSC — Technical Assistant & Scientific Assistant (CS)

## Selection Strategy Report — Rahul KP

**Papers analyzed:** SAC:03:2017 TA (CS/IT, Ahmedabad, 2018 exam), SDSC-SHAR Scientific Assistant (CS & Maths, 2015), VSSC TA Post 1370 (2018), VSSC TA Post 1386 (2019) — 4 papers, ~280 questions, spanning 2015–2019.

---

## STEP 1 — Question Classification (representative sample)

A full 280-row table isn't useful to study from — the signal is in topic frequency, not individual question IDs. Here's the method applied, shown on a representative slice; the full tagging fed directly into the Pareto table in Step 2.

| Paper         | Q No | Topic                        | Subtopic                                  | Difficulty  | Freq Pattern                              | Your Note Location                             |
| ------------- | ---- | ---------------------------- | ----------------------------------------- | ----------- | ----------------------------------------- | ---------------------------------------------- |
| 1386 (2019)   | Q80  | Operating Systems            | Context Switch                            | Easy        | Appeared 4/4 papers (concept)             | 05-Operating-Systems/Process.md                |
| 1386 (2019)   | Q21  | Operating Systems            | Deadlock (necessary conditions)           | Medium      | Appeared 4/4 papers                       | 05-Operating-Systems/Deadlocks.md              |
| 1370 (2018)   | Q54  | DBMS                         | Normalization / DBMS statements           | Medium      | Appeared 4/4 papers                       | 06-Database-Management-System/Normalization.md |
| 1370 (2018)   | Q44  | Programming                  | C pointer arithmetic, output tracing      | Medium      | Appeared 4/4 papers (C/C++/Java tracing)  | **Not in repo — see Category C**               |
| SAC-2018      | Q39  | Digital Logic                | Boolean truth table → gate                | Easy        | Appeared 4/4 papers                       | **Not in repo — see Category C**               |
| Sci Asst 2015 | Q17  | Computer Architecture        | Memory address lines                      | Medium      | Appeared 3/4 papers                       | 04-Computer-Architecture/Memory.md             |
| 1386 (2019)   | Q76  | Computer Networks            | HTTP/TCP port + protocol                  | Easy        | Appeared 4/4 papers                       | 07-Computer-Networks/HTTP.md, TCP-IP.md        |
| Sci Asst 2015 | Q75  | Mathematics                  | Calculus (differentiation)                | Easy        | Appeared 4/4 papers                       | 01-Mathematics/Calculus.md                     |
| 1370 (2018)   | Q65  | OOP                          | Constructor / abstract / interface theory | Easy–Medium | Appeared 4/4 papers                       | **Partially covered — see Category B**         |
| SAC-2018      | Q35  | Microprocessor / Electronics | 8085 architecture, RS232/RS485            | Medium–Hard | Appeared 2/4 papers (heavier in SAC 2018) | **Not in repo — see Category C, LOW priority** |

---

## STEP 2 — 80/20 Pareto Analysis

### Top ~20% of topics producing ~80% of questions (across all 4 papers)

**Priority 1 (Must Master) — ~65% of total marks**

| Topic                                                                                                         | Expected Questions (per 80Q paper) | Probability of Appearing | Reason                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------- | ---------------------------------- | ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| C/C++/Java code-tracing (output prediction)                                                                   | 8–10                               | ~95%                     | Every single paper has 6–10 "what will this program print" questions. Highest-yield single skill in the whole exam.                                                           |
| Operating Systems (scheduling, deadlock, memory mgmt, paging, threads, process states)                        | 8–10                               | ~95%                     | OS is the single largest conceptual block in every paper — CPU scheduling, deadlock conditions, page replacement, thrashing, context switch all repeat verbatim across years. |
| Computer Networks (TCP/IP, HTTP/HTTPS, OSI layers, addressing/subnetting, protocols by port)                  | 7–9                                | ~90%                     | Subnetting/IP-address arithmetic appears in 3 of 4 papers; protocol-to-port mapping in all 4.                                                                                 |
| DBMS (SQL queries, normalization, keys, ACID, locking, normal forms)                                          | 6–8                                | ~90%                     | Present in all 4 papers; SQL query-reading questions are a fixed feature.                                                                                                     |
| Digital Logic & Number Systems (K-maps, Boolean algebra, flip-flops, gates, base conversions)                 | 7–9                                | ~90%                     | Strongest in the SAC and Sci. Assistant papers, still solid in VSSC papers.                                                                                                   |
| Computer Architecture (registers, addressing modes, cache, memory addressing math, CPU basics)                | 5–7                                | ~85%                     | Recurs every year, esp. "how many address lines / bits" style numeric questions.                                                                                              |
| Mathematics & Aptitude (calculus, algebra, trigonometry, numerical methods, probability, quant word problems) | 8–10                               | ~95%                     | ISRO always carries a dedicated math/aptitude block (~10 Q) separate from CS — don't skip this, it's free marks if drilled.                                                   |

**Priority 2 (Important) — ~20% of total marks**

| Topic                                                                               | Expected Questions | Probability | Reason                                                                                      |
| ----------------------------------------------------------------------------------- | ------------------ | ----------- | ------------------------------------------------------------------------------------------- |
| OOP theory (constructors, inheritance, interface, abstract class, access modifiers) | 3–5                | ~85%        | Consistently 3–5 per paper, mostly conceptual/definitional, low prep cost per mark.         |
| Software Engineering (SDLC models, testing types, cohesion/coupling, UML, metrics)  | 3–5                | ~80%        | Recurs but is largely definitional — high ROI for low effort.                               |
| Security fundamentals (cryptography basics, malware types, DoS, HTTPS/SSH)          | 2–4                | ~75%        | Growing presence in the more recent (2018/2019) papers — worth tracking as an upward trend. |
| DSA (stack/queue/linked list properties, complexity, hashing basics)                | 3–4                | ~75%        | Mostly conceptual ("which DS is best suited for X"), rarely deep coding — cheap marks.      |

**Priority 3 (Low ROI) — ~15% of total marks, long tail**

| Topic                                                                                                                          | Expected Questions | Probability                      | Reason                                                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------ | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Electronics/Microprocessor hardware specifics (8085 instruction-level detail, RS232/RS485 electrical specs, amplifier classes) | 1–3                | ~50% (concentrated in SAC paper) | This is EC-adjacent content bleeding into a CS/IT-labeled paper — likely because SAC posts sometimes combine CS/IT with instrumentation roles. Skim only; don't build deep new notes here. |
| Pure general knowledge/trivia (latest Android version, "Father of Linux", DVD transfer speed)                                  | 1–2                | ~40%                             | Unpredictable, low prep value, can't be systematically prepared.                                                                                                                           |
| Cloud/Big Data terms (PaaS, Hadoop, data warehouse use-cases)                                                                  | 1–2                | ~50%, rising in later papers     | Small but growing — matches ISRO's general drift toward modern infra topics. Light-touch prep only.                                                                                        |

---

## STEP 3 & 4 — Knowledge Tree Mapping + Intersection Detection

### Category A: Already Covered (revise + PYQ drill only)

```
INTERSECTION FOUND ✅
Exam Topic: Operating System Scheduling & Deadlocks
Matched Existing Knowledge: 05-Operating-Systems/CPU-Scheduling.md, Deadlocks.md, Synchronization.md, Thread.md
Required Action: Revise + solve 60 MCQs across scheduling algorithms, deadlock necessary conditions, semaphores

INTERSECTION FOUND ✅
Exam Topic: DBMS Normalization, SQL, Keys, Transactions
Matched Existing Knowledge: 06-Database-Management-System/Normalization.md, SQL.md, Transactions.md, ER-Diagrams.md
Required Action: Revise + drill SQL query-reading (SELECT/DELETE with WHERE/subqueries) — this exact question style repeats

INTERSECTION FOUND ✅
Exam Topic: Computer Networks — TCP/IP, HTTP, OSI, Addressing
Matched Existing Knowledge: 07-Computer-Networks/TCP-IP.md, HTTP.md, OSI-Model.md, Routing.md
Required Action: Revise + drill subnetting/IP arithmetic numerically (timed, no calculator — matches exam conditions)

INTERSECTION FOUND ✅
Exam Topic: Computer Architecture — Cache, Memory, CPU registers
Matched Existing Knowledge: 04-Computer-Architecture/Cache.md, Memory.md, CPU.md
Required Action: Revise + drill "N address lines / page table size" style arithmetic

INTERSECTION FOUND ✅
Exam Topic: Software Engineering — SDLC models, Testing, UML
Matched Existing Knowledge: 08-Software-Engineering/SDLC.md, Testing.md, UML.md, Agile.md
Required Action: Revise definitions; these are high-yield, low-effort marks

INTERSECTION FOUND ✅
Exam Topic: Mathematics — Calculus, Algebra, Probability, Trigonometry
Matched Existing Knowledge: 01-Mathematics/Calculus.md, Linear-Algebra.md, Probability.md, Statistics.md
Required Action: Revise + timed drill — ISRO math questions are formula-application, not derivation

INTERSECTION FOUND ✅
Exam Topic: DSA fundamentals — Stack, Queue, Linked List, Hashing, Complexity
Matched Existing Knowledge: 02-Data-Structures-and-Algorithms/Stack.md, Queue.md, Linked-Lists.md, Hashing.md, Complexity.md
Required Action: Revise properties/complexity tables; PYQs test conceptual recall, not implementation

INTERSECTION FOUND ✅
Exam Topic: Security fundamentals — Cryptography, Malware, DoS
Matched Existing Knowledge: 07-Computer-Networks/Security.md, 14-Professional-Knowledge/Security.md
Required Action: Revise + build a malware-types comparison table (worm vs trojan vs spyware vs ransomware — directly tested)
```

### Category B: Partially Covered (update existing files)

```
UPDATE EXISTING FILE
Path: 02-Data-Structures-and-Algorithms/Complexity.md
Add Sections:
1. C/C++/Java "trace the output" worked examples (pointers, pre/post increment, static, loops)
2. Common gotcha patterns: pointer arithmetic on char arrays, macro expansion pitfalls (#define SQR(x) (x*x))
3. Java exception hierarchy + try/catch/finally execution order edge cases
Reason: This is your #1 PYQ frequency topic (8–10 Q/paper) and your repo has DSA concepts but not this "code output prediction" question style, which is a distinct exam skill from writing algorithms.

UPDATE EXISTING FILE DONE ✅
Path: 05-Operating-Systems/Memory-Management.md
Add Sections:
1. Page replacement algorithms (FIFO, LRU, Optimal) with worked numeric examples
2. Page table size / address bits calculations (recurring numeric question type)
3. Internal vs external fragmentation with formula for max wasted bytes
Reason: Your file covers memory management conceptually but the exam tests numeric page-table/address-bit computation specifically — appeared in 3/4 papers.

UPDATE EXISTING FILE DONE ✅
Path: 07-Computer-Networks/TCP-IP.md
Add Sections:
1. Subnet mask → network address / valid host ID worked problems
2. TCP vs UDP — which protocols use which (Telnet/HTTP/DNS/SMTP mapping)
3. Well-known port numbers table (HTTP 80, HTTPS 443, FTP 21, SMTP 25, Telnet 23, DNS 53)
Reason: Numeric subnetting and protocol-port mapping are tested almost every paper; your file likely covers TCP mechanics but not this applied/numeric layer.

UPDATE EXISTING FILE
Path: 08-Software-Engineering/Testing.md
Add Sections:
1. Testing types comparison table: Unit/Integration/System/Acceptance/Regression/Alpha/Beta/Mutation
2. Top-down vs Bottom-up integration testing — stub vs driver requirement (directly tested, easy to mix up)
3. White-box vs Black-box — what each is based on
Reason: 3–5 Q/paper are pure definitional testing-terminology questions; a comparison table converts this into a 2-minute revision.

UPDATE EXISTING FILE
Path: 04-Computer-Architecture/Instruction-Set.md
Add Sections:
1. Addressing modes (immediate, direct, indirect, indexed) with one-line identifiers
2. CISC vs RISC key differences
Reason: Appears as a recurring 1–2 Q/paper conceptual item; your file likely covers instruction sets generally but not this specific compare/contrast framing.
```

### Category C: Completely Missing (new files required)

```
NEW CONTENT REQUIRED ⚠️
Topic: Digital Logic Design (K-Maps, Boolean Algebra, Flip-Flops, Counters, Gates)
Reason: Appeared in all 4 papers, 7–9 Q/paper — your repo has NO dedicated digital logic folder at all. This is a major gap given how heavily ISRO weights it.
Create New Note:
  Folder: 04-Computer-Architecture (or a new 04b-Digital-Logic folder)
  Files: Boolean-Algebra.md, K-Maps.md, Flip-Flops-and-Counters.md, Number-Systems.md
Priority: HIGH

NEW CONTENT REQUIRED ⚠️
Topic: C/C++ Program Tracing & Output Prediction
Reason: This is the single highest-frequency question TYPE across all papers (not covered by your DSA notes, which focus on algorithms not language-semantics tracing)
Create New Note:
  Folder: 02-Data-Structures-and-Algorithms (or new 15-Programming-Languages folder)
  Files: C-Output-Tracing.md, CPP-OOP-Gotchas.md, Java-Output-Tracing.md
Priority: HIGH

NEW CONTENT REQUIRED ⚠️
Topic: Number Systems & Data Representation (binary/octal/hex/BCD/Gray code conversions, signed representations, ASCII)
Reason: Appeared in every paper, 3–5 Q/paper — foundational and currently absent
Create New Note:
  Folder: 04-Computer-Architecture
  File: Number-Systems-and-Representation.md
Priority: HIGH

NEW CONTENT REQUIRED ⚠️
Topic: Aptitude & Quantitative Reasoning (train/speed/distance, probability word problems, time-and-work style)
Reason: A fixed ~8-10 Q block in every paper; distinct from your theoretical Probability/Statistics notes which are proof/formula-oriented, not word-problem-drill oriented
Create New Note:
  Folder: 01-Mathematics
  File: Aptitude-Quant-PYQs.md
Priority: MEDIUM-HIGH

NEW CONTENT REQUIRED ⚠️
Topic: Microprocessor Basics (8085 architecture, registers, addressing modes, RS232/RS485 basics)
Reason: Concentrated mainly in the SAC 2017/18 paper (2–4 Q), lighter in VSSC papers
Create New Note:
  Folder: 04-Computer-Architecture
  File: Microprocessor-8085-Basics.md
Priority: LOW (only if targeting SAC-style posts specifically; skip if focusing purely on VSSC/general CS posts)

NEW CONTENT REQUIRED ⚠️
Topic: Cloud/Big Data terminology (PaaS/IaaS/SaaS, Hadoop, Data Warehousing use-cases)
Reason: Small but present, growing in 2018/2019 papers vs. 2015
Create New Note:
  Folder: 14-Professional-Knowledge/Cloud.md (extend existing file rather than new one)
Priority: LOW
```

---

## STEP 5 — ISRO-Focused Syllabus (not GATE-generic)

**Tier 1 — Must Complete**

- OS: CPU scheduling algorithms, deadlock (conditions + avoidance/detection), paging/segmentation, page replacement, semaphores/synchronization, threads, context switching
- DBMS: SQL (SELECT/DELETE/UPDATE with WHERE/subqueries), normalization (1NF–BCNF), keys, ACID, locking granularity
- Networks: OSI/TCP-IP layers, subnetting arithmetic, protocol-port mapping, HTTP/HTTPS/DNS/SMTP basics
- Digital Logic: Boolean algebra simplification, K-maps (3–4 variable), flip-flops, counters, gate truth tables, number system conversions
- C/C++/Java: output-tracing (loops, pointers, increment operators, OOP constructs, exception handling)
- Computer Architecture: cache, memory addressing math, addressing modes, CISC/RISC, registers
- Math/Aptitude: differentiation/integration basics, linear algebra (matrix rank, determinants), probability, trigonometric identities, quantitative word problems

**Tier 2 — Should Complete**

- OOP theory (constructors, interfaces, abstract classes, access modifiers, polymorphism)
- Software Engineering (SDLC models, testing taxonomy, cohesion/coupling, UML basics)
- Security fundamentals (malware types, cryptography basics, HTTPS/SSH, DoS)
- DSA conceptual (stack/queue/linked-list properties, complexity classes, hashing)

**Tier 3 — Only if time available**

- Microprocessor 8085 hardware specifics, RS232/RS485 electrical parameters, amplifier classes (only relevant to SAC-style postings)
- Cloud/Big Data terminology
- General trivia (OS version history, "father of X")

---

## STEP 7 — Question Prediction Engine

**Very High Probability Topics**

- Topic: OS Scheduling & Deadlock — Why: appeared in all 4 papers, multiple sub-variants each time — Expected Q type: numeric (turnaround/waiting time) + conceptual (necessary conditions) — Example: "2 processes, 3 shared resources, max 2 each — deadlock possible?" (verbatim style in 1386-2019)
- Topic: C/C++ output tracing — Why: highest raw frequency of any single question style — Expected Q type: "what does this program print" — Example: pointer arithmetic, pre/post-increment combos
- Topic: SQL query reading — Why: present in every paper — Expected Q type: "what does this query do/return" — Example: DELETE with subquery on average
- Topic: Subnetting/IP addressing — Why: present in 3/4 papers, numeric and unambiguous — Expected Q type: "given IP + subnet mask, find network address / valid host"

**Medium Probability Topics**

- Digital Logic (K-maps, flip-flops) — solid presence but slightly more paper-dependent (heavier in SAC/Sci.Asst than VSSC)
- Software Engineering testing taxonomy — steady 3–5 Q but easy to under-revise since it feels "soft"
- Security (malware types, HTTPS/SSH) — rising trend 2018→2019, worth tracking

**Surprise Topics**

- General trivia (Android version, "Father of Linux") — impossible to reliably prepare, treat as free/skip
- Electronics/hardware (RS232/RS485, amplifier classes) — concentrated almost entirely in the SAC paper; if you're not applying to SAC-Ahmedabad-style instrumentation-adjacent posts, deprioritize
- Cloud/Big Data — small but appearing more in later papers, could grow

---

## STEP 8 — Practice System

**Daily**

- Technical MCQs: 30–40 (mixed Tier 1 topics, weighted toward OS/DBMS/Networks/Digital-Logic/Programming)
- Aptitude: 10–15 quant word problems, timed
- Revision: 30 min flashcard-style pass over previously flagged weak topics
- PYQ: 10–15 questions/day from the 4 papers (rotate through all of them, don't front-load one)

**Weekly**

- Mock test: 1 full 80Q paper under real time constraints (2 hrs, no notes/calculator — matches actual exam rules)
- Error analysis: log every wrong answer by topic in a simple tracker (topic, question, why you got it wrong: knowledge gap / silly mistake / time pressure)
- Weak topic improvement: pick the lowest-accuracy topic from that week's error log, spend one focused session rebuilding it

---

## STEP 9 — Notes Improvement Strategy Summary

(Full detail already given in Step 4 above — consolidated action list:)

1. **UPDATE**: 02-DSA/Complexity.md → add C/C++/Java output-tracing worked examples
2. **UPDATE**: 05-OS/Memory-Management.md → add page replacement + page-table numeric problems
3. **UPDATE**: 07-Networks/TCP-IP.md → add subnetting worked problems + port-number table
4. **UPDATE**: 08-SE/Testing.md → add testing-types comparison table
5. **UPDATE**: 04-Architecture/Instruction-Set.md → add addressing modes + CISC/RISC compare
6. **CREATE**: 04-Architecture/Number-Systems-and-Representation.md
7. **CREATE**: (new folder or under DSA) C-Output-Tracing.md, CPP-OOP-Gotchas.md, Java-Output-Tracing.md
8. **CREATE**: (new folder or under Architecture) Boolean-Algebra.md, K-Maps.md, Flip-Flops-and-Counters.md
9. **CREATE**: 01-Mathematics/Aptitude-Quant-PYQs.md
10. **CREATE** (low priority): 04-Architecture/Microprocessor-8085-Basics.md
11. **EXTEND** (low priority): 14-Professional-Knowledge/Cloud.md with PaaS/Hadoop/Data-Warehouse terms

---

## STEP 10 — Final ISRO Selection Strategy Report

**1. Exam Pattern Analysis:** 80 objective MCQs, 2 hrs (except the 2015 Sci. Asst. paper: 60Q/1.5hrs), negative marking of -1 in the VSSC papers (SAC paper also -1), no negative marking in the 2015 Sci. Asst. paper. Bilingual (Hindi/English) papers are common — don't let translation slow you down, the English is always authoritative when in doubt.

**2. Highest ROI Topics:** C/C++/Java output-tracing, OS (scheduling+deadlock+memory), DBMS (SQL+normalization), Networks (subnetting+protocols), Digital Logic (K-maps+Boolean algebra), Math/Aptitude — these six clusters are ~65-70% of every paper.

**3. Existing Knowledge Coverage:** Roughly 60–65% of tested topics have some corresponding file in your repo already (OS, DBMS, Networks, Architecture, Math, DSA, SE all exist at folder level) — but several of those need worked-numeric-example upgrades (Category B), not just revision.

**4. Missing Knowledge:** ~25-30% — primarily Digital Logic (a whole folder gap), C/C++/Java output-tracing as a distinct skill, and structured number-systems content.

**5. New Files Required:** 7 high/medium priority new files (Digital Logic ×3, Output-Tracing ×3, Number-Systems ×1, Aptitude ×1), 2 low-priority optional ones.

**6. 12-Week Plan:** Weeks 1–4 foundation/gap-filling, 5–8 high-frequency deepening, 9–10 PYQ mocks, 11–12 final revision.

**7. Daily Routine:** ~3–4 hrs/day: 30–40 MCQs technical + 10–15 aptitude + 30 min revision + 10–15 PYQ questions.

**8. Mock Test Strategy:** One full timed 80Q paper weekly starting Week 5, ramping to every 2–3 days in Weeks 9–10; always followed by topic-tagged error analysis, never just a raw score check.

**9. Final 30-Day Revision Plan:** Days 1–10: Priority 1 topics only, condensed formula/definition sheets. Days 11–20: full mixed mock every other day + targeted weak-topic sprints. Days 21–27: light revision only, 2 hrs/day max, protect sleep. Days 28–30: no new content — skim your own notes, rest, stay calm.

---

_Note: This analysis is based on 4 papers spanning 2015–2019. If you can source 1–2 more recent papers (2021 onward), it's worth re-running this Pareto pass — ISRO's topic mix has been drifting slightly toward cloud/security content in the later years, and a newer paper would sharpen that trend read._
