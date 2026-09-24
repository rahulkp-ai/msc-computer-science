# Computer Networks — PYQ + Important Questions with Explanations

Sourced from your 4 uploaded ISRO papers, plus **[Standard]** supplementary items for
high-yield concepts.

---

## A. OSI / TCP-IP Model & Protocols

**Q1 [VSSC 1386, Q14].** Which layer is NOT part of the TCP/IP model?
(a) Transport Layer (b) Session Layer (c) Application Layer (d) Network Layer

**Answer: (b) Session Layer**
**Explanation:** ⚠️ Classic trap. The OSI model has **7 layers** (including Session and
Presentation), but the TCP/IP model has only **4 layers**: Application, Transport,
Internet (Network), and Link/Network Access. Session and Presentation layer
_functionality_ still happens, but it's folded into the Application layer in TCP/IP —
they aren't separate layers there.

---

**Q2 [VSSC 1370, Q11].** What is the default port number for HTTP?
(a) 25 (b) 22 (c) 80 (d) 53

**Answer: (c) 80**
**Explanation:** Memorize the standard port table (see cheat sheet at the bottom of
this file) — this exact question style (protocol → port, or port → protocol) appears
in nearly every ISRO paper.

---

**Q3 [SHAR 2015, Q27].** Which of the following uses UDP as the transport protocol?
(a) Telnet (b) HTTP (c) DNS (d) SMTP

**Answer: (c) DNS**
**Explanation:** DNS primarily uses UDP (fast, connectionless, small queries) though it
can fall back to TCP for larger responses (like zone transfers). Telnet, HTTP, and SMTP
all require TCP's reliable, ordered delivery.

---

**Q4 [VSSC 1370, Q62].** Which protocol is used in Email?
(a) FTP (b) SMB (c) TELNET (d) SMTP

**Answer: (d) SMTP**
**Explanation:** SMTP (Simple Mail Transfer Protocol) is used for _sending_ email.
(Receiving/retrieving mail uses POP3 or IMAP — a distinction ISRO sometimes tests
separately.)

---

**Q5 [VSSC 1386, Q18].** Which of the following uses Simplex mode of data transfer?
(a) Print from Computer to Printer (b) Internet Browsing (c) Telephone Communication
(d) None of the above

**Answer: (a) Print from Computer to Printer**
**Explanation:** **Simplex** = one-direction only (printer never sends data back in
this model). **Half-duplex** = both directions, but only one at a time (e.g. walkie-
talkie). **Full-duplex** = both directions simultaneously (e.g. telephone call,
internet browsing which sends requests and receives data concurrently).

---

**Q6 [VSSC 1386, Q76].** Suppose you are browsing the World Wide Web and trying to
access web servers. What is the underlying protocol and port number being used?
(a) UDP, 80 (b) TCP, 80 (c) TCP, 25 (d) UDP, 25

**Answer: (b) TCP, 80**
**Explanation:** HTTP requires TCP's reliability guarantees (ordered, error-checked
delivery) for web page loading, on the well-known port 80 (443 for HTTPS).

---

**Q7 [VSSC 1370, Q63].** Which of the following establishes a secure communication
between the client and the server? (a) HTTP and FTP (b) Only HTTPS (c) Only SSH
(d) HTTPS and SSH

**Answer: (d) HTTPS and SSH**
**Explanation:** Both HTTPS (secure web browsing, uses TLS/SSL) and SSH (secure remote
shell/login) provide encrypted, authenticated communication channels. HTTP and FTP are
both plaintext/unencrypted by default.

---

**Q8 [SAC 2017/18, Q41].** Systematic procedure and rule governing data exchange
between communicating devices is called: (a) Protocol (b) Message (c) Format
(d) Exchange

**Answer: (a) Protocol**
**Explanation:** A protocol defines the rules, syntax, semantics, and timing of
communication — this is essentially the textbook definition, a common early-paper
warm-up question.

---

## B. IP Addressing & Subnetting

**Q9 [SAC 2017/18, Q26 — worked example].**
Your router has IP address 172.16.2.1/23 on Ethernet 0. Which of the following can be
valid host IDs on the LAN interface attached to the router?
(1) 172.16.1.100 (2) 172.16.2.198 (3) 172.16.1.198 (4) 172.16.3.16

**Working:**

- `/23` subnet mask = 255.255.**254**.0 (23 bits of network, so the 3rd octet's last
  bit is part of the host portion)
- Network address for 172.16.2.1/23: the 3rd octet in binary, with /23 meaning the
  network boundary falls mid-byte. 172.16.**2**.0 → in binary, octet 3 = 00000010.
  With /23, the network portion covers all but the last 9 bits, so valid host range for
  this network spans octet-3 values **2 and 3** together (172.16.2.0 – 172.16.3.255,
  minus network/broadcast addresses).
- So valid hosts: anything in 172.16.**2.x** or 172.16.**3.x** (excluding
  172.16.2.0 as network address and 172.16.3.255 as broadcast address)
- Checking options: (2) 172.16.2.198 ✓ valid. (4) 172.16.3.16 ✓ valid. (1) and (3) are
  in the 172.16.1.x range — NOT part of this /23 network.

**Answer: (b) 2 and 4 only**
**Explanation:** This is the single most important _skill_, not just fact, in the
Networks section — being able to compute network ranges from CIDR notation quickly.
Always convert the prefix length to understand exactly which bits are "network" vs
"host," especially for non-byte-aligned prefixes like /23 (as opposed to the simpler
/24).

---

**Q10 [SHAR 2015, Q35 — worked example].**
IP address of one node is 172.16.100.11. Subnet mask is 255.255.255.0. What is the
network address? (a) 172.16.0.0 (b) 172.0.0.0 (c) 172.16.100.0 (d) 172.0.0.10

**Working:** Network address = IP address **bitwise AND** subnet mask.
`255.255.255.0` keeps the first 3 octets unchanged and zeroes the last octet.
172.16.100.11 AND 255.255.255.0 = **172.16.100.0**

**Answer: (c) 172.16.100.0**

---

**Q11 [VSSC 1386, Q52 — worked example].**
Maximum number of host addresses possible for a network with subnet mask
255.255.240.0? (a) 256 (b) 1024 (c) 4094 (d) 4096

**Working:**

- `255.255.240.0` in binary: last two octets = `11110000.00000000`
- That's 4 network bits borrowed from the 3rd octet + all 8 bits of the 4th octet
  reserved for hosts = 4 + 8 = **12 host bits**
- Max addresses = 2¹² = 4096; usable HOST addresses = 4096 - 2 (subtract network
  address and broadcast address) = **4094**

**Answer: (c) 4094**
**Explanation:** ⚠️ Always check whether the question asks for total addresses (2^n) or
_usable host_ addresses (2^n - 2, subtracting network & broadcast). ISRO tests this
exact distinction repeatedly.

---

**Q12 [SAC 2017/18, Q67].** Which class of IP address provides a maximum of only 254
host addresses per network ID? (a) Class A (b) Class B (c) Class C (d) Class D

**Answer: (c) Class C**
**Explanation:** Class C uses a default /24 mask → 8 host bits → 2⁸-2 = 254 usable
hosts. (Class A: /8 → ~16 million hosts. Class B: /16 → ~65,000 hosts. Class D is
reserved for multicast, not host addressing at all.)

---

**Q13 [SAC 2017/18, Q47].** Local host — what does 127.0.0.1 represent?
_(from VSSC 1370, Q67, same concept)_: In Computer Networks, which represents local
host? (a) 127.0.0.1 (b) 255.255.255.254 (c) 10.41.7.102 (d) 127.255.255.255

**Answer: (a) 127.0.0.1**
**Explanation:** The entire 127.0.0.0/8 range is reserved as the **loopback** address
block, used by a machine to refer to itself. 127.0.0.1 is the conventional default.

---

## C. Switching & Physical Layer Concepts

**Q14 [SHAR 2015, Q47].** Which method provides a dedicated communication channel
between two stations? (a) Switch based network (b) Packet switching
(c) Circuit Switching (d) Hub based network

**Answer: (c) Circuit Switching**
**Explanation:** Circuit switching (e.g. traditional telephone networks) reserves a
fixed, dedicated path for the entire duration of the communication. Packet switching
(used by the Internet) shares bandwidth dynamically — packets from many
conversations interleave on the same links.

---

**Q15 [VSSC 1386, Q42].** Choose the WRONG statement about packet switching.
(a) uses store and forward transmission
(b) all packets follow the same route
(c) bandwidth is not wasted compared to circuit switching
(d) packets may arrive out of order

**Answer: (b) all packets follow the same route**
**Explanation:** This is the FALSE statement (i.e. the correct answer to "which is
WRONG"). Packets in packet switching can take _different_ routes to the destination —
that's precisely why they may arrive out of order (option d is TRUE) and why
efficiency/bandwidth usage is better than reserving a fixed circuit (option c is TRUE).

---

**Q16 [VSSC 1386, Q20 — worked example].**
Four channels are multiplexed using TDM. If each channel sends 100 bytes/second, what
is the bit rate for the link? (a) 400 bps (b) 800 bps (c) 1600 bps (d) 3200 bps

**Working:**

- 4 channels × 100 bytes/sec = 400 bytes/sec total
- 400 bytes/sec × 8 bits/byte = **3200 bits/sec**

**Answer: (d) 3200 bps**
**Explanation:** Easy to lose marks here by forgetting the bytes→bits conversion
(×8). Always check the units requested (bps = bits per second) vs given (bytes/sec).

---

**Q17 [SAC 2017/18, Q16].** Which multiple access technique is used by IEEE 802.11
standard for wireless LAN? (a) CDMA (b) CSMA/CA (c) ALOHA (d) None of the mentioned

**Answer: (b) CSMA/CA**
**Explanation:** Wired Ethernet (IEEE 802.3) uses CSMA/**CD** (Collision _Detection_) —
it can detect collisions on the wire. Wireless (IEEE 802.11) uses CSMA/**CA**
(Collision _Avoidance_) instead, since wireless devices generally can't reliably detect
collisions while transmitting (the "hidden terminal" problem), so they try to avoid
collisions proactively.

---

## D. Addressing at Different Layers, ARP, MAC

**Q18 [VSSC 1370, Q66].** ARP (Address Resolution Protocol) is used for resolving:
(a) Network address to broadcast address (b) IP address to MAC address
(c) Network frame to packet (d) Subnet mask address to a machine IP address

**Answer: (b) IP address to MAC address**
**Explanation:** ARP maps a known IP address (Layer 3) to the corresponding physical
MAC address (Layer 2) on a local network segment — necessary because Ethernet frames
are addressed by MAC, not IP.

---

**Q19 [VSSC 1386, Q47].** Which address is used to determine the process on a host
system? (a) Logical address (b) Physical address (c) MAC address (d) Port address

**Answer: (d) Port address**
**Explanation:** IP address identifies the _host_; port number identifies the specific
_process/application_ on that host (e.g. port 80 for the web server process, port 25
for the mail server process).

---

**Q20 [VSSC 1386, Q66].** What does VLAN do?
(a) Acts as the fastest port to all servers
(b) Provides multiple collision domains on one switch port
(c) Breaks up broadcast domains in a layer 2 switch internetwork
(d) Provides multiple broadcast domains within a single collision domain

**Answer: (c) Breaks up broadcast domains in a layer 2 switch internetwork**
**Explanation:** A VLAN (Virtual LAN) logically segments a single physical switch into
multiple separate broadcast domains, as if they were on physically different switches
— improving security and reducing unnecessary broadcast traffic.

---

## E. Security-Adjacent Networking Concepts

**Q21 [SAC 2017/18, Q18].** What is the purpose of a Denial of Service attack?
(a) To execute a Trojan on a system (b) Exploit a weakness in the TCP/IP stack
(c) To shutdown services by turning them off
(d) To overload a system so it is no longer operational

**Answer: (d)**
**Explanation:** DoS attacks aim to make a service _unavailable_ to legitimate users,
typically by overwhelming it with traffic/requests so it can't respond to real users —
not by shutting it down directly or exploiting a specific vulnerability (though some
DoS variants do exploit protocol weaknesses as the _mechanism_, the _goal_ is
unavailability).

---

**Q22 [VSSC 1386, Q44].** When an attempt is made to make a machine or network service
unavailable to its intended users, the attack is called:
(a) Denial-Of-Service attack (b) Slow Read Attack (c) Cross-site scripting attack
(d) Zero Day attack

**Answer: (a) Denial-Of-Service attack**
**Explanation:** Direct definitional match — the general term for this class of attack.
(Slow Read is a _specific technique_ to cause DoS; XSS is an entirely different
vulnerability class involving script injection; Zero-day refers to an unpatched,
unknown vulnerability, not a specific attack type.)

---

**Q23 [VSSC 1386, Q45].** Which malicious program can spread by itself without any
human intervention? (a) Worm (b) Trojan (c) Spyware (d) Virus

**Answer: (a) Worm**
**Explanation:** ⚠️ A very commonly confused pair: a **Virus** needs a _host program_
and typically requires some user action (running an infected file) to spread. A
**Worm** is self-contained and self-propagating — it can spread across networks
entirely on its own, exploiting vulnerabilities, with zero user interaction needed.

---

## Cheat Sheet — Memorize Before the Exam

| Protocol             | Port    | Transport    |
| -------------------- | ------- | ------------ |
| FTP (data / control) | 20 / 21 | TCP          |
| SSH                  | 22      | TCP          |
| Telnet               | 23      | TCP          |
| SMTP                 | 25      | TCP          |
| DNS                  | 53      | UDP (mostly) |
| HTTP                 | 80      | TCP          |
| HTTPS                | 443     | TCP          |
| POP3                 | 110     | TCP          |
| IMAP                 | 143     | TCP          |

| Concept                              | One-line distinguisher                                                          |
| ------------------------------------ | ------------------------------------------------------------------------------- |
| Virus vs Worm                        | Virus needs a host + user action; Worm self-propagates                          |
| Simplex/Half-duplex/Full-duplex      | 1-way / 2-way-alternating / 2-way-simultaneous                                  |
| Circuit vs Packet switching          | Dedicated fixed path vs shared dynamic routing                                  |
| CSMA/CD vs CSMA/CA                   | Wired collision _detection_ vs Wireless collision _avoidance_                   |
| OSI (7 layers) vs TCP/IP (4 layers)  | TCP/IP merges Session+Presentation into Application                             |
| Network address vs Broadcast address | First address in subnet vs last address in subnet (both unusable as hosts)      |
| Seek/Access/Response time            | (These are OS-adjacent but often confused with network latency — keep separate) |
