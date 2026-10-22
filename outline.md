# Virginia Tech Applied Algebra Seminar, October 22, 2026

**Aim:** explain how a transversal CCZ condition becomes a problem about binary row overlaps, then use projective geometry and Boolean equations to construct Q48.

**Audience:** coding theorists, mathematicians, and QEC researchers. Introduce the quantum notation first. Draw every code of the first half on the cube F₂³: the Steane code introduces CSS codes and transversal gates, and the [[8,3,2]] code is the worked example for encoding, phases, and overlaps. Reuse the same 48-point support throughout the larger construction.

**Timing:** about 38 minutes including the title and outline, followed by discussion within the one-hour slot. This is a planned delivery budget, not a measured rehearsal. There are 29 numbered slides, five unnumbered transition outlines, and one unnumbered title frame, followed by four backup slides, B1 to B4, for questions on the lower bound and the [CLM+26] framework. The same six-theme outline appears at the start of every theme. The current theme is bright teal and bold. All other themes are shaded in the same fixed positions. Overlay states are separate PDF pages but share one slide number.

## Narrative and checkpoints

| Part | Clock | Purpose |
|---|---|---|
| CSS codes and transversal gates | 0:00–7:50 | Define binary vectors, Pauli strings, CSS codes and transversal gates on the cube, with the Steane code as the example. Pose the construction question. |
| [[8,3,2]] example | 7:50–13:00 | Explain logical CCZ with one code, then derive the signed overlap conditions. |
| Gate conditions | 13:00–15:40 | Place the conditions in context and separate parity completion from sign feasibility. |
| Geometric construction | 15:40–22:40 | State Q48, fix S geometrically, prove the Z-distance floor and divisibility. |
| Column picture and completion | 22:40–30:40 | Translate overlaps into Boolean moments, find K, certify dZ=3, and solve for signs. |
| Bounds and questions | 30:40–37:40 | Explain the Reed–Muller reduction, scope the exclusions, and finish with open questions. |

## Slide-by-slide plan

Slide numbers below are the displayed frame numbers, not PDF page numbers. The title gets 0:00–0:15. Each later outline transition has a ten-second budget within its theme. All other content keeps its existing slide number.

| Slide | Clock | Topic | Essential point |
|---|---|---|---|
| 1 | 0:15–1:00 | Outline | Steane and [[8,3,2]] examples, gate conditions, geometry, completion, bounds. |
| 2 | 1:00–1:55 | Binary vectors as Boolean functions | Qubits at the points of F₂³. Faces u1, u2, their overlap (an edge) and their XOR. |
| 3 | 1:55–2:55 | Pauli strings | X(a), Z(b) on basis states. Overlap 2 commutes, overlap 1 anticommutes. |
| 4 | 2:55–3:55 | Stabilizer and CSS codes | Stabilizers, syndrome, [[n,k,d]]. X(a) for a in C2, Z(b) for b in the dual of C1. G=[K;S], logical basis. |
| 5 | 3:55–4:35 | The Steane code | Seven nonzero points. S is the three faces, K is all ones. Logical basis with one term of each state on the cube. |
| 6 | 4:35–5:40 | Syndromes and distance | The syndrome of Z on u is u. Distinct nonzero columns detect pairs. A Fano line is a weight-3 logical. |
| 7 | 5:40–6:40 | Clifford and non-Clifford gates | Every gate on basis states. Clifford gates alone are not universal. Add T or CCZ. |
| 8 | 6:40–7:50 | Transversal gates and distillation | S on every Steane qubit gives phase i to the weight, so it is logical S†. Eastin–Knill rules out T. Distillation needs transversal T or CCZ. State the target. |
| – | 7:50–8:00 | Outline: The [[8,3,2]] code: a worked example of logical CCZ | Current theme bright and bold. All others shaded. |
| 9 | 8:00–9:15 | The [[8,3,2]] code | Origin back, roles of S and K swapped. Logical states are complement pairs. An edge gives dZ=2, and dX=4. |
| 10 | 9:15–10:15 | Signed weight and the gate condition | A coset needs one common phase. Signed weight determines it modulo eight. |
| 11 | 10:15–12:15 | A T/T† pattern for logical CCZ | Ask where T-dagger goes. Face, edge, vertex signed weights are 0, 0, -1. |
| 12 | 12:15–13:00 | The gate condition becomes conditions on generator rows | Singles mod 8, pairs mod 4, triples mod 2. Only the logical triple is odd. |
| – | 13:00–13:10 | Outline: Triorthogonality and the CCZ conditions | Current theme bright and bold. All others shaded. |
| 13 | 13:10–14:10 | Triorthogonal codes and CCZ | Timeline. Triorthogonal matrices have even overlaps, CCZ needs one odd triple. |
| 14 | 14:10–15:40 | Conditions for quasi-transversal CCZ | Nine parity families give quasi-transversal CCZ. Signs need stronger congruences. |
| – | 15:40–15:50 | Outline: Projective geometry and the 48-qubit code | Current theme bright and bold. All others shaded. |
| 15 | 15:50–17:10 | Result: a 48-qubit code with a transversal T/T† CCZ | Q48: dX=16, dZ=3. 26 T and 22 T-dagger, without correction. |
| 16 | 17:10–18:10 | Fix S from finite projective geometry | Projective columns and 8-divisible codewords fix S. Complete K, then signs. |
| 17 | 18:10–19:10 | Projectivity rules out weight-one and weight-two Z logicals | A Z syndrome is a column or a sum of columns. Projectivity detects weights 1 and 2. |
| 18 | 19:10–20:10 | Complement of a projective subspace | 63 projective points minus 15 leaves three blocks of 16. |
| 19 | 20:10–21:40 | Hyperplane sections and codeword weights | A nonzero u coefficient gives weight 24. A pure w coefficient gives 32. |
| 20 | 21:40–22:40 | More geometric constructions | Subspace complements give 13 lengths. Only the starred fixed-support census is complete. |
| – | 22:40–22:50 | Outline: Column indicators, logical rows, and phase signs | Current theme bright and bold. All others shaded. |
| 21 | 22:50–24:10 | Column indicators from the generator matrix | An indicator records occupied columns. [[8,3,2]] gives y, Q48 support gives w1+w2+w1w2. |
| 22 | 24:10–25:40 | The CH conditions are inner products with monomials | Overlap parity equals an indicator-monomial inner product. One cubic moment is odd. |
| 23 | 25:40–27:10 | Logical rows in the column picture | Each geometric point receives three logical bits. Geometry already handles S1-S3. |
| 24 | 27:10–29:10 | Finding the logical rows | Linear row space, compatible pairs, linear third row. Then a weight-three Z witness. |
| 25 | 29:10–30:40 | Solving for the T/T† pattern | Binary sign variables satisfy mod-4 equations. Q48 has 26 T and 22 T-dagger. |
| – | 30:40–30:50 | Outline: Lower bounds and open questions | Current theme bright and bold. All others shaded. |
| 26 | 30:50–32:40 | Stabilizer supports are Reed--Muller codewords | S1-S3 give zero moments through degree 3. Adding the origin fixes weight parity. |
| 27 | 32:40–34:10 | Our exclusion argument covers every length through 38 | Rank reduction, classified supports, complete remaining enumeration: n<=38 excluded. |
| 28 | 34:10–36:10 | Existence of a valid code at different block lengths | Our floor 38. WJS excludes 39-46. Specified 47 code needs correction. Q48 has signs. |
| 29 | 36:10–37:40 | Takeaways and open questions | Geometry fixes S, Boolean constraints complete K, signs certify the T/T† pattern. |

## Delivery choices

Explain the [[8,3,2]] phase through the overlap view only, and use it to derive the general conditions. On the timeline slide, give the progression rather than reading the references. On the construction-family slide, interpret one entry and qualify the census counts. On the search slide, spend time on why the third row becomes linear. Show the explicit sign polynomial as a specification, without reading its terms aloud.

If behind, shorten the historical recap, family table, and final indicator-coset formula. Preserve the distinction between parity conditions and physical signs, the projective distance proof, the Q48 gate pattern, and the scope of the lower bound. The detailed notes give specific cuts at the checkpoints.

Keep these qualifications explicit: projectivity proves dZ≥3, while dX is checked for the completed code. Eight-divisibility is a construction choice. Only the starred fixed-support census is complete. The n≤38 theorem assumes the nine CH conditions. The sign infeasibility of the specified 47-qubit comparison code does not prove 48 minimal for an uncorrected T/T† pattern.

Sources and their updated slide locations are in references.md. The full transcript is in speaking_notes.md, built with the slide images into transcript.pdf, with a matching one-page speaking card.
