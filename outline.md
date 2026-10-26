# VTQ Seminar, Virginia Tech, October 29, 2026

**Aim:** show that a single layer of $T$ and $T^\dagger$ gates can act as logical CCZ on a distance-3 code, explain how the condition becomes a problem about binary row overlaps, construct Q48 with projective geometry and Boolean equations, and state what is and is not known about using it in a CCZ factory.

**Audience:** the Virginia Tech Center for Quantum Information Science and Engineering. Mostly physicists and quantum computer scientists who work on error correction and fault tolerance, plus coding theorists from Mathematics. State the fault-tolerance goal and the result first. Keep the cube background brisk, since stabilizer codes are familiar. Keep the algebraic core, and end with the factory protocol and the open practical questions.

**Timing:** the slot is 60 minutes, then a separate 30 minutes of questions. The script runs about 43 minutes including the title and outlines. The remaining time covers slower live delivery and questions during the talk. This is a planned delivery budget, not a measured rehearsal. There are 31 numbered slides, six unnumbered transition outlines, and one unnumbered title frame, followed by five backup slides, B1 to B5. The same seven-theme outline appears at the start of every theme. The current theme is bright blue and bold. All other themes are shaded in the same fixed positions. Overlay states are separate PDF pages but share one slide number.

## Narrative and checkpoints

| Part | Clock | Purpose |
|---|---|---|
| Goal and result | 0:15–2:15 | Fault tolerance needs T or CCZ. Distillation overhead. One layer of T/T† as logical CCZ. State Q48. |
| CSS codes and transversal gates | 2:15–10:05 | Generator rows on the cube, Pauli strings, CSS codes, the [[8,3,2]] code, the Clifford hierarchy, transversal gates, and a table of three codes. |
| [[8,3,2]] example | 10:05–14:00 | Explain logical CCZ with one code, then derive the signed overlap conditions. |
| Gate conditions | 14:00–16:55 | Place the conditions in context and separate quasi-transversal CCZ from a T/T† pattern. |
| Geometric construction | 16:55–23:55 | State Q48, fix S geometrically, prove the Z-distance floor and divisibility. |
| Column picture and completion | 23:55–31:55 | Translate overlaps into Boolean moments, find K, certify dZ=3, and solve for signs. |
| Lower bounds | 31:55–37:25 | Explain the Reed–Muller reduction and scope the exclusions by length. |
| CCZ factory and questions | 37:25–42:35 | The distillation protocol, n against footprint, known parameters, open practical questions. |

## Slide-by-slide plan

Slide numbers below are the displayed frame numbers, not PDF page numbers. The title gets 0:00–0:15. Each later outline transition has a ten-second budget.

| Slide | Clock | Topic | Essential point |
|---|---|---|---|
| 1 | 0:15–2:15 | Logical CCZ from one layer of T and T† gates | Need T or CCZ. Distillation has overhead. [[8,3,2]] pattern has dZ=2 and has run on hardware. Q48 is the answer. |
| 2 | 2:15–2:45 | Outline | Seven parts. |
| 3 | 2:45–3:45 | Generator rows on the cube | Columns are points of F₂³. Rows u1, u2, their overlap (an edge) and their XOR. |
| 4 | 3:45–4:30 | Pauli strings | X(a), Z(b) on basis states. Overlap 2 commutes, overlap 1 anticommutes. |
| 5 | 4:30–5:30 | Stabilizer and CSS codes | Stabilizers, syndrome, [[n,k,d]]. X(a) for a in C2, Z(b) for b in the dual of C1. G=[K;S], logical basis. |
| 6 | 5:30–7:00 | The [[8,3,2]] code | Complement pairs. Z on 000 has syndrome 1. An edge is a weight-2 logical: dX=4, dZ=2. |
| 7 | 7:00–8:15 | Clifford and non-Clifford gates | Gates on basis states. Clifford hierarchy: T and CCZ in level 3. |
| 8 | 8:15–9:00 | Transversal gates and distillation | Eastin–Knill. Distillation needs transversal T or CCZ. |
| 9 | 9:00–10:05 | Codes with different transversal gates | Steane, [[15,1,3]], [[8,3,2]]. State the target. |
| – | 10:05–10:15 | Outline | |
| 10 | 10:15–11:15 | Signed weight and the gate condition | A coset needs one common phase, set by the signed weight mod 8. |
| 11 | 11:15–13:15 | A T/T† pattern for logical CCZ | Ask where T† goes. Face, edge, vertex signed weights are 0, 0, -1. |
| 12 | 13:15–14:00 | The gate condition becomes conditions on generator rows | Singles mod 8, pairs mod 4, triples mod 2. |
| – | 14:00–14:10 | Outline | |
| 13 | 14:10–15:10 | Triorthogonal codes and CCZ | Timeline. CCZ needs one odd triple. |
| 14 | 15:10–16:55 | Conditions for quasi-transversal CCZ | Nine parities give a diagonal Clifford correction, possibly with CZ. A T/T† pattern is S† on the T† qubits and needs the signed congruences. |
| – | 16:55–17:05 | Outline | |
| 15 | 17:05–18:25 | Result | Q48: dX=16, dZ=3. 26 T and 22 T†, no correction. |
| 16 | 18:25–19:25 | Fix S from finite projective geometry | Projective columns, 8-divisible span, complete K, then signs. |
| 17 | 19:25–20:25 | Projectivity | Projective S detects Z errors of weight 1 and 2. |
| 18 | 20:25–21:25 | Complement of a projective subspace | 63 points minus 15 leaves three blocks of 16. |
| 19 | 21:25–22:55 | Hyperplane sections and codeword weights | 60 codewords of weight 24, 3 of weight 32. |
| 20 | 22:55–23:55 | More geometric constructions | 13 lengths. Only the starred census is complete. |
| – | 23:55–24:05 | Outline | |
| 21 | 24:05–25:25 | Column indicators | [[8,3,2]] gives y, Q48 gives w1+w2+w1w2. |
| 22 | 25:25–26:55 | CH conditions as inner products | One cubic moment is odd. |
| 23 | 26:55–28:25 | Logical rows in the column picture | Three label bits per point. |
| 24 | 28:25–30:25 | Finding the logical rows | Linear row space, compatible pairs, linear third row, weight-3 Z witness. |
| 25 | 30:25–31:55 | Solving for the T/T† pattern | Binary signs in mod-4 equations. 26 T and 22 T†. |
| – | 31:55–32:05 | Outline | |
| 26 | 32:05–33:55 | Stabilizer supports are Reed–Muller codewords | Zero moments through degree 3. |
| 27 | 33:55–35:25 | Exclusion through 38 | Rank reduction and complete enumeration. |
| 28 | 35:25–37:25 | Existence by block length | Our floor 38. WJS excludes 39–46. The specified 47 code needs a correction. |
| – | 37:25–37:35 | Outline | |
| 29 | 37:35–39:35 | Distilling CCZ states with Q48 | Protocol from the paper. JVB 47-to-1 with footprint 9 needs a CZ correction. n is not footprint. |
| 30 | 39:35–41:05 | What is known about Q48, and what is not | Ranks, weights, logical basis. Open: preparation, noise, costs, biased noise. |
| 31 | 41:05–42:35 | Takeaways and open questions | Geometry, labels, signs. Factory circuits and biased noise. |

## Delivery choices

Explain the [[8,3,2]] phase through the overlap view only, and use it to derive the general conditions. On the timeline slide, give the progression rather than reading the references. On the construction-family slide, interpret one entry and qualify the census counts. On the search slide, spend time on why the third row becomes linear. Show the explicit sign polynomial as a specification, without reading its terms aloud.

If behind, shorten the historical recap, family table, final indicator-coset formula, and the right column of slide 30. Preserve the distinction between parity conditions and physical signs, the projective distance proof, the Q48 gate pattern, and the scope of the lower bound. The detailed notes give specific cuts at the checkpoints.

Keep these qualifications explicit: projectivity proves dZ≥3, while dX is checked for the completed code. Eight-divisibility is a construction choice. Only the starred fixed-support census is complete. The n≤38 theorem assumes the nine CH conditions. The sign infeasibility of the specified 47-qubit comparison code does not prove 48 minimal for an uncorrected T/T† pattern.

Sources and their updated slide locations are in references.md. The full transcript is in speaking_notes.md, built with the slide images into transcript.pdf, with a matching one-page speaking card.
