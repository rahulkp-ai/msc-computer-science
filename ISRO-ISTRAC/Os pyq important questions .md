# Operating Systems — PYQ + Important Questions with Explanations

Sourced from your 4 uploaded ISRO papers (SAC 2017/18, SHAR Sci. Asst. 2015, VSSC 1370
2018, VSSC 1386 2019) plus supplementary high-yield questions marked **[Standard]** for
concepts that ISRO tests often but weren't in this particular 4-paper sample.

---

## A. Process States & Scheduling

**Q1 [SHAR 2015].** The state of a process after it encounters an I/O instruction is:
(a) Ready (b) Blocked (c) Idle (d) Running

**Answer: (b) Blocked**
**Explanation:** When a process requests I/O, it cannot continue executing until the
I/O completes, so the OS moves it out of the CPU and into the _blocked/waiting_ state.
It only returns to _ready_ once the I/O finishes.

---

**Q2 [VSSC 1386, Q80].** The switching of the CPU from one process or thread to another
is called: (a) process switch (b) task switch (c) context switch (d) none

**Answer: (c) context switch**
**Explanation:** A context switch saves the state (registers, program counter, etc.) of
the currently running process and loads the saved state of the next process to run.

---

**Q3 [VSSC 1386, Q30].** In operating system, Response time is:
(a) total time from submission to completion
(b) time from submission till the first response is produced
(c) total time from submission to final output
(d) none of these

**Answer: (b)**
**Explanation:** Don't confuse this with **turnaround time** (submission→completion, =
option a) or **waiting time**. Response time specifically measures how quickly the
system starts responding — critical for interactive/time-sharing systems.

---

**Q4 [VSSC 1386, Q75].** Which scheduling algorithm is ALWAYS preemptive?
(a) FCFS (b) SJF (c) Priority scheduling (d) Round Robin

**Answer: (d) Round Robin**
**Explanation:** FCFS is inherently non-preemptive. SJF and Priority scheduling each
have both preemptive and non-preemptive _variants_ — so they're not "always" one or the
other. Round Robin, by definition (fixed time quantum, forced context switch when the
quantum expires), is always preemptive.

---

**Q5 [VSSC 1370, Q23].** For a given set of tasks with known durations queued on a
single processor, which is the BEST scheduling algorithm?
(a) FCFS (b) Shortest Job First (c) Round Robin (d) Priority Scheduling

**Answer: (b) Shortest Job First**
**Explanation:** SJF minimizes average waiting time when all job lengths are known in
advance — this is a well-known optimality result. It's provably optimal for average
waiting time among non-preemptive algorithms when durations are known upfront.

---

**Q6 [VSSC 1370, Q56].** A scenario in priority-based scheduling where a higher-priority
task waits for a lower-priority task to complete, when both share the same resource, is
called: (a) Priority ceiling (b) Priority sharing (c) Priority Inheritance
(d) Priority inversion

**Answer: (d) Priority inversion**
**Explanation:** Priority inversion is the _problem_; **priority inheritance** (option
c) is one common _solution_ to it — the low-priority task temporarily "inherits" the
higher priority so it finishes faster and releases the resource. Don't mix these two up.

---

**Q7 [VSSC 1386, Q69].** Which of the following is a solution for Starvation in
Priority-based Scheduling?
(a) Caching (b) Aging (c) Paging (d) Thrashing

**Answer: (b) Aging**
**Explanation:** Aging gradually increases the priority of processes that have been
waiting a long time, guaranteeing they eventually get scheduled and preventing
indefinite starvation.

---

**Q8 [Standard].** In a system with 16 CPUs, what is the maximum number of processes
that can be in the "Running" state at once? _(compare with VSSC 1386 Q49's "Ready
state" question below)_

**Answer: 16**
**Explanation:** Only one process can run per CPU at a time, so with 16 CPUs, at most
16 processes can be simultaneously _running_.

---

**Q9 [VSSC 1370, Q49].** The maximum number of processes that can be in Ready state for
a computer system with 16 CPUs is: (a) 16 (b) 256 (c) independent of number of CPUs
(d) 65536

**Answer: (c) independent of the number of CPUs**
**Explanation:** This is the trap version of Q8 above — the number of CPUs limits how
many processes can be _running_ simultaneously, but the _ready queue_ has no such
limit; any number of processes can be waiting for a turn on the CPU regardless of how
many CPUs exist.

---

## B. Deadlock

**Q10 [VSSC 1370, Q61].** Which of the following is NOT a necessary condition for a
deadlock? (a) Hold & wait (b) No pre-emption (c) Starvation (d) Circular Wait

**Answer: (c) Starvation**
**Explanation:** The four Coffman conditions for deadlock are: **Mutual exclusion,
Hold and wait, No pre-emption, Circular wait.** Starvation is a related-but-distinct
phenomenon (a process waiting indefinitely) — it is NOT one of the four deadlock
conditions.

---

**Q11 [SAC 2017/18, Q56].** Dijkstra's banking algorithm in an operating system solves
the problem of: (a) Deadlock avoidance (b) Deadlock prevention (c) Deadlock detection
(d) All of above

**Answer: (a) Deadlock avoidance**
**Explanation:** The **Banker's Algorithm** is the classic example of deadlock
_avoidance_ — it checks, before granting a resource request, whether the system would
remain in a "safe state" afterward. This is different from _prevention_ (structurally
ruling out one of the four Coffman conditions) and _detection_ (finding a deadlock
after it has already occurred, e.g. via a wait-for graph).

---

**Q12 [VSSC 1386, Q21].** A system has 2 processes and 3 shared identical resources.
Each process needs a maximum of 2 of those resources. Which is TRUE?
(a) Deadlock may occur (b) Deadlock NEVER occurs (c) Starvation always occurs
(d) None of the above

**Answer: (b) Deadlock NEVER occurs**
**Explanation:** Worst case: both processes each hold 1 resource (using up 2 of the 3
available) and both wait for a 2nd. But there's still 1 resource left unallocated, so at
least one process can get its 2nd resource and complete, freeing its resources for the
other. General rule: with `n` processes each needing a max of `m` resources, and total
resources `R ≥ n(m-1)+1`, deadlock is impossible. Here: 2(2-1)+1 = 3 = R exactly →
deadlock-free by this formula.

---

**Q13 [Standard].** What are the 4 necessary conditions for deadlock (the Coffman
conditions)?

**Answer:**

1. **Mutual Exclusion** — at least one resource must be held in a non-shareable mode
2. **Hold and Wait** — a process holding at least one resource is waiting to acquire
   additional resources held by others
3. **No Pre-emption** — a resource can only be released voluntarily by the process
   holding it
4. **Circular Wait** — a set of processes are waiting for each other in a circular
   chain

All four must hold simultaneously for deadlock to occur — breaking even one prevents
it.

---

## C. Memory Management, Paging, Fragmentation

**Q14 [SAC 2017/18, Q10].** Dirty bit is used for:
(a) wrong page in memory (b) page that is modified after being loaded in cache memory
(c) page less frequently accessed (d) page with corrupt data

**Answer: (b)**
**Explanation:** The dirty bit (also called the modified bit) marks whether a page has
been written to since it was loaded into memory/cache. When that page is later evicted,
the dirty bit tells the OS whether it needs to be written back to disk (dirty = yes,
must write back) or can simply be discarded (clean = no changes, safe to discard).

---

**Q15 [SHAR 2015, Q16].** If the page size is 'n' bytes, the maximum number of bytes
unutilized due to internal fragmentation is:
(a) n bytes (b) n/2 bytes (c) n-1 bytes (d) 2n bytes

**Answer: (c) n-1 bytes**
**Explanation:** Internal fragmentation happens within the LAST page allocated to a
process, when the process's data doesn't perfectly fill that page. In the worst case,
the process uses only 1 byte of the last page, wasting `n-1` bytes.

---

**Q16 [VSSC 1370, Q20].** The Physical Address Space is conceptually divided into a
number of fixed-size blocks, called: (a) Frames (b) Segments (c) Pages (d) None

**Answer: (a) Frames**
**Explanation:** Classic terminology trap: **logical/virtual** address space is divided
into **pages**; **physical** memory is divided into **frames** of the same size. Pages
map onto frames via the page table.

---

**Q17 [SHAR 2015, Q46].** A page fault occurs when:
(a) a program crashes during execution
(b) there is an error in the accessed page
(c) a program accesses a page of a different program
(d) a program accesses a page not currently available in memory

**Answer: (d)**
**Explanation:** A page fault is simply the OS's mechanism for detecting that a
requested page isn't currently resident in physical memory — it then triggers loading
that page from disk (demand paging). It is a normal, expected part of virtual memory
operation, not necessarily an error.

---

**Q18 [SHAR 2015, Q31].** Which of the following are likely causes of thrashing?
(a) Page size was very small (b) Too many users connected to the system
(c) LRU used for page replacement (d) FIFO used for page replacement

**Answer: (b) Too many users connected to the system**
**Explanation:** Thrashing occurs when the system spends more time swapping pages
in/out than doing actual useful work — typically because the combined working sets of
all active processes exceed available physical memory (high degree of
multiprogramming). LRU/FIFO are just replacement _policies_, not causes of thrashing by
themselves.

---

**Q19 [VSSC 1370, Q2].** Which of the following is NOT a criterion for page replacement
from main memory? (a) FIFO (b) LRU (c) LIFO (d) None of these

**Answer: (c) LIFO**
**Explanation:** FIFO and LRU (and Optimal) are standard page replacement algorithms.
LIFO (Last In First Out) is a stack discipline, not used as a page-replacement policy —
it would be a poor choice since it would always evict the most recently loaded page,
the one most likely to be needed again soon.

---

**Q20 [SHAR 2015, Q39 style — numeric page table calc, worked example].**
If the page size in a 32-bit machine is 4K bytes, what is the size of the page table?

**Working:**

- 32-bit address space → total addressable memory = 2³² bytes
- Page size = 4K = 2¹² bytes → number of pages = 2³²/2¹² = 2²⁰ pages
- Each page table entry typically needs to store a frame number — assuming standard
  ISRO convention that each entry occupies enough bits to be effectively "1 word" or a
  known size (paper-dependent; check the exact options given)
- With 2²⁰ entries: if each entry is 1 byte, total = 2²⁰ bytes = 1 MB

**Answer pattern:** matches option "1 Mbytes" style answers seen in these papers.
**Explanation:** This numeric-page-table-size pattern (given: address bits + page size,
find: page table size or number of entries) is one of the most reliable recurring
question types — always work it as: `total address space ÷ page size = number of
pages/entries`, then multiply by entry size if asked for table size in bytes.

---

**Q21 [VSSC 1386, Q53 — worked example].**
A machine has 128 MB physical memory and a 32-bit virtual address space. If the page
size is 8 KB, how many entries will be in the page table?

**Working:**

- Virtual address space = 2³² bytes (this determines the NUMBER of pages, i.e. entries
  in the page table — physical memory size is a distractor here, it affects frame
  count, not page table entry count)
- Page size = 8 KB = 2¹³ bytes
- Number of entries = 2³² / 2¹³ = 2¹⁹

**Answer: 2 power 19**
**Explanation:** ⚠️ Common trap: the physical memory size (128 MB) is IRRELEVANT to
this particular question — the number of page table entries is determined by the
_virtual/logical_ address space divided by page size, not by how much physical RAM
exists. Don't let the physical memory number distract you into the wrong calculation.

---

## D. Threads & Synchronization

**Q22 [SHAR 2015, Q4].** Which of the following is TRUE with respect to threads?
(a) shares instruction space of other threads in the process
(b) shares data space of other threads in the process
(c) shares instruction space of kernel
(d) shares data space of kernel

**Answer: (b)**
**Explanation:** Threads within the SAME process share the process's data segment,
heap, and open files — but each thread has its own stack and (usually) its own
registers/program counter. Threads do NOT share space with the kernel; that's a
separate protection domain.

---

**Q23 [SAC 2017/18, Q17].** At a particular time, the value of a counting semaphore is 10. It will become 7 after: (a) 3 V operations (b) 3 P operations (c) 5 V operations
(d) None of the above

**Answer: (b) 3 P operations**
**Explanation:** In semaphore terminology: **P (wait/down)** _decrements_ the value;
**V (signal/up)** _increments_ it. To go from 10 → 7, you need a net decrease of 3,
which requires 3 P operations (assuming no V operations in between).

---

**Q24 [VSSC 1386, Q22].** A process executes:

```
for (i=0; i<p; i++) { fork(); }
```

What is the total number of child processes created?
(a) 1 (b) p (c) 2^p - 1 (d) 2^p

**Answer: (c) 2^p - 1**
**Explanation:** Each `fork()` call doubles the total number of processes in existence
at that point (parent + all children created so far each independently execute the
remaining loop iterations). After `p` iterations, total processes = 2^p. Subtracting
the 1 original process gives 2^p - 1 _children_ created.

---

## E. File Systems, Disks, Linux/UNIX

**Q25 [VSSC 1386, Q10].** The time required to move the read/write head to the desired
track of a disk is called: (a) Latency (b) Access time (c) Seek time (d) Page fault

**Answer: (c) Seek time**
**Explanation:** Don't confuse: **Seek time** = moving the head to the correct track.
**Rotational latency** = waiting for the correct sector to rotate under the head.
**Access time** = seek time + rotational latency + transfer time (the total).

---

**Q26 [SHAR 2015, Q49].** The smallest amount of information that can be read from or
written to the disk is called: (a) block (b) sector (c) track (d) cylinder

**Answer: (b) sector**
**Explanation:** Standard disk hierarchy: platter → track (a ring on the platter) →
sector (a segment of a track, the smallest addressable unit) → cylinder (same track
across all platters, stacked).

---

**Q27 [SHAR 2015, Q38].** Which UNIX command allows scheduling a program to be executed
at a specified time? (a) cron (b) nice (c) vmstat (d) 'date' and 'time'

**Answer: (a) cron**
**Explanation:** `cron` is the standard UNIX/Linux daemon for scheduling recurring or
future tasks. `nice` adjusts process _priority_ (not scheduling time), `vmstat` reports
virtual memory statistics.

---

**Q28 [SHAR 2015, Q48].** What is the command used to attach a new file system to the
existing directory structure in UNIX? (a) attach (b) link (c) mount (d) move

**Answer: (c) mount**
**Explanation:** `mount` attaches a filesystem (e.g. a new disk, partition, or network
share) into the existing UNIX directory tree at a specified mount point.

---

**Q29 [VSSC 1386, Q63].** UNIX-based OS stores passwords in which form?
(a) Hashed (b) Encrypted (c) Plain text (d) Decrypted

**Answer: (a) Hashed**
**Explanation:** UNIX/Linux systems store password _hashes_ (traditionally in
`/etc/shadow`), not the plaintext or a reversibly-encrypted form. Hashing is one-way —
the system verifies a login by hashing the entered password and comparing hashes, never
by decrypting a stored value.

---

**Q30 [VSSC 1370, Q4].** Which mode of I/O operation keeps the processor MOST busy?
(a) Programmed I/O (b) Interrupt Initiated I/O (c) DMA (d) None of these

**Answer: (a) Programmed I/O**
**Explanation:** In Programmed I/O, the CPU actively polls the device status in a busy-
wait loop until the I/O completes — this wastes the most CPU cycles. Interrupt-driven
I/O frees the CPU to do other work until interrupted. DMA (Direct Memory Access) is the
most CPU-efficient, transferring data directly between device and memory with minimal
CPU involvement.

---

## F. Standard concepts likely to appear (not in this paper sample, but high-yield)

**Q31 [Standard].** What is Belady's Anomaly?
**Answer:** The counter-intuitive phenomenon where increasing the number of page frames
available to a process can _increase_ the number of page faults, when using the FIFO
page replacement algorithm. It does NOT occur with LRU or Optimal replacement.

**Q32 [Standard].** What are the main RAID levels and their key trade-off?
**Answer:**

- RAID 0 — striping, no redundancy, best performance, zero fault tolerance
- RAID 1 — mirroring, full redundancy, halves usable capacity
- RAID 5 — striping with distributed parity, tolerates 1 disk failure
- RAID 6 — like RAID 5 but with double distributed parity, tolerates 2 disk failures
- RAID 10 (1+0) — mirrored pairs, then striped — good performance + redundancy, costly
  (This connects to VSSC 1386 Q4, "which RAID type doesn't use parity" → RAID 1, since it
  uses mirroring, not parity.)

**Q33 [Standard].** Difference between Preemptive and Non-preemptive scheduling?
**Answer:** In preemptive scheduling, the OS can forcibly take the CPU away from a
running process (e.g. when a higher-priority process arrives, or a time quantum
expires). In non-preemptive scheduling, once a process starts running, it keeps the CPU
until it voluntarily yields (completes or blocks on I/O).
