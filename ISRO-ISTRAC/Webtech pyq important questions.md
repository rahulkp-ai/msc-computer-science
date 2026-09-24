# Web Technologies — PYQ + Important Questions with Explanations

Sourced from your 4 uploaded ISRO papers, plus **[Standard]** supplementary items.
This subject gets the fewest dedicated questions per paper (typically 3–6) compared to
OS/DBMS/Networks, but every one of them is cheap, purely definitional — high ROI for
low prep time.

---

## A. HTML

**Q1 [SAC 2017/18, Q20].** What tag is used to display a picture in an HTML page?
(a) picture (b) image (c) photo (d) img

**Answer: (d) img**
**Explanation:** `<img src="..." alt="...">` is the correct HTML tag. Note it's a
_self-closing/void_ element (no separate closing tag needed in HTML5, though
`<img ... />` XHTML-style is also valid).

---

**Q2 [VSSC 1370, Q24].** The language used to design web pages for a website:
(a) HTML (b) C++ (c) FORTRAN (d) ADA

**Answer: (a) HTML**
**Explanation:** Straightforward, but worth noting the category distinction: HTML is a
**markup language** (structure/content), not a general-purpose programming language
like the other three options.

---

**Q3 [VSSC 1370, Q32 — worked example].**

```html
<table>
  <tr>
    <td>Name</td>
  </tr>
  <tr>
    <td>Class</td>
  </tr>
</table>
```

What does this print?
(a) A table with ONE row and TWO columns
(b) A table with TWO rows and FOUR columns
(c) A table with TWO rows and ONE column in each row
(d) A table with ONE row and ONE column

**Answer: (c) A table with TWO rows and ONE column in each row**
**Explanation:** Count the `<tr>` (table row) tags — there are TWO separate `<tr>...

</tr>` blocks, so TWO rows. Each `<tr>` contains exactly ONE `<td>` (table data/cell),
so ONE column per row. Always count `<tr>` for rows and `<td>` per `<tr>` for columns —
don't confuse total `<td>` count across the table with "columns per row."

---

**Q4 [VSSC 1386, Q72].** Which is the most appropriate HTML tag to create a numbered
list? (a) `<dl>` (b) `<ul>` (c) `<li>` (d) `<ol>`

**Answer: (d) `<ol>`**
**Explanation:** `<ol>` = Ordered List (numbered). `<ul>` = Unordered List (bulleted).
`<li>` = individual List Item (used inside either `<ol>` or `<ul>`, not a list type
itself). `<dl>` = Definition List (term/description pairs).

---

## B. CSS

**Q5 [VSSC 1370, Q10].** Which is NOT true about Cascading Style Sheets (CSS)?
(a) CSS can control the layout of multiple web pages
(b) CSS supplements style formatting in HTML page
(c) Style definitions can be saved in an external CSS file
(d) Only one CSS can be used in a HTML file

**Answer: (d) Only one CSS can be used in a HTML file**
**Explanation:** This is the FALSE statement (answer to "which is NOT true") — an HTML
page can link to MULTIPLE external CSS files simultaneously (via multiple `<link>`
tags), plus have internal `<style>` blocks and inline styles, all layered together with
CSS's cascading priority rules.

---

**Q6 [VSSC 1386, Q73].** Which is an advantage of using a separate CSS file in HTML?
(a) The content becomes easy to manage
(b) Easier to design sites for different devices like mobile
(c) CSS files are cached and decrease server load and network traffic
(d) All of the above

**Answer: (d) All of the above**
**Explanation:** Separating CSS into its own file gives you: maintainability
(change style once, applies everywhere), responsive/device-adaptable design
flexibility, AND performance benefits (the browser caches the CSS file after first
load, so subsequent pages/visits don't re-download it, reducing server load).

---

## C. JavaScript & AJAX

**Q7 [SAC 2017/18, Q28].** AJAX stands for:
(a) asynchronous javascript and xml (b) advanced JSP and xml
(c) asynchronous JSP and xml (d) advanced javascript and xml

**Answer: (a) asynchronous javascript and xml**
**Explanation:** AJAX = **A**synchronous **J**avaScript **A**nd **X**ML. Note: despite
the name, modern AJAX commonly uses JSON instead of XML for data exchange — but the
acronym's literal expansion (as tested here) still refers to XML.

---

**Q8 [VSSC 1370, Q12].** Which of the following is WRONG about AJAX?
(a) AJAX stands for Asynchronous Javascript and HTML
(b) AJAX is a client side script used to get data from server without refreshing the
current page
(c) AJAX is a scripting language
(d) AJAX makes applications faster and more user friendly

**Answer: (a)**
**Explanation:** ⚠️ Combine with Q7 above — AJAX stands for Asynchronous JavaScript
AND **XML**, not HTML. This is the WRONG statement being asked for. Options (b), (c),
(d) are all accurate descriptions of AJAX's purpose and behavior.

---

## D. HTTP & Web Protocols

**Q9 [VSSC 1370, Q17].** The HTTP status code for "requested resource not found" is:
(a) 400 (b) 405 (c) 404 (d) 500

**Answer: (c) 404**
**Explanation:** Standard HTTP status code families: **1xx** = informational, **2xx** =
success (200 OK), **3xx** = redirection, **4xx** = client error (400 Bad Request, 404
Not Found, 403 Forbidden), **5xx** = server error (500 Internal Server Error). Memorize
this family structure even if you can't recall every specific code.

---

**Q10 [SAC 2017/18, Q59].** A web cookie is a small piece of data:
(a) sent from a website and stored in the user's web browser while browsing a website
(b) sent from user and stored in the server while browsing a website
(c) sent from root server to all servers
(d) none of the mentioned

**Answer: (a)**
**Explanation:** Cookies are set by the SERVER but stored CLIENT-side (in the user's
browser), then sent back to the server on subsequent requests to maintain state
(login sessions, preferences, tracking, etc.) — the direction matters, don't reverse it.

---

**Q11 [VSSC 1370, Q55].** Information from a web page stored on the SERVER side is
called: (a) Cookies (b) Session (c) Servlet (d) Credentials

**Answer: (b) Session**
**Explanation:** ⚠️ Pairs directly with Q10 — **Cookies** = client-side (browser)
storage; **Session** = server-side storage, typically identified by a session ID that's
itself often stored in a cookie on the client, but the actual session DATA lives on
the server.

---

## E. XML, RSS, Web Servers

**Q12 [VSSC 1370, Q35].** Closing tag is compulsory in all elements of:
(a) HTML (b) XML (c) Both of the above (d) None of the above

**Answer: (b) XML**
**Explanation:** XML is strict about well-formedness — every opening tag MUST have a
matching closing tag (or be self-closing, `<tag/>`). HTML (especially older/HTML5
"void elements" like `<img>`, `<br>`) is more lenient and allows some tags without
explicit closing tags.

---

**Q13 [VSSC 1370, Q48].** XML stands for:
(a) Extended Middle Language (b) Extended Medium Language
(c) Extensible Markup Language (d) Extensible Model Language

**Answer: (c) Extensible Markup Language**

---

**Q14 [VSSC 1386, Q19].** In RSS Feeds, RSS stands for:
(a) Really Synchronous Syndication (b) Rational Synchronous Service
(c) Really Simple Syndication (d) Rational Simple Syndication

**Answer: (c) Really Simple Syndication**
**Explanation:** RSS is an XML-based format for syndicating frequently updated content
(news feeds, blog updates) so subscribers/readers can be automatically notified of new
content without visiting the site directly.

---

**Q15 [SHAR 2015, Q36].** What is the freely available web server for developing JSP?
(a) WebSphere (b) Tomcat (c) Weblogic (d) Dynamo

**Answer: (b) Tomcat**
**Explanation:** Apache Tomcat is the standard free, open-source servlet
container/web server commonly used for Java/JSP development. WebSphere (IBM) and
WebLogic (Oracle) are commercial, enterprise-grade application servers.

---

## F. PHP / Server-Side Basics

**Q16 [VSSC 1370, Q6].** Which prefix is used to denote a variable in PHP?
(a) $ (b) @ (c) ~ (d) #

**Answer: (a) $**
**Explanation:** PHP variables are always prefixed with `$` (e.g. `$name = "value";`)
— a simple but often-tested syntax fact.

---

## Cheat Sheet — Memorize Before the Exam

| Term                       | Key Fact                                                                        |
| -------------------------- | ------------------------------------------------------------------------------- |
| `<ol>` vs `<ul>`           | Ordered (numbered) vs Unordered (bulleted) list                                 |
| Cookie vs Session          | Cookie = client-side storage; Session = server-side storage                     |
| AJAX                       | Asynchronous JavaScript AND XML (not HTML)                                      |
| HTTP status codes          | 2xx=success, 3xx=redirect, 4xx=client error (404=Not Found), 5xx=server error   |
| XML vs HTML tag strictness | XML requires closing tags for everything; HTML is more lenient                  |
| RSS                        | Really Simple Syndication                                                       |
| Tomcat                     | Free/open-source JSP-capable web server (vs commercial WebSphere/WebLogic)      |
| PHP variable prefix        | `$`                                                                             |
| CSS in separate file       | Benefits: maintainability + caching (less server load) + responsive design ease |
