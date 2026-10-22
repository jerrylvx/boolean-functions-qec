# Virginia Tech Applied Algebra Seminar, October 22, 2026

**Aim:** explain how a transversal CCZ condition becomes a problem about binary row overlaps, then use projective geometry and Boolean equations to construct Q48.

**Audience:** coding theorists, mathematicians, and QEC researchers. Introduce the quantum notation first. Draw the code of the first half on the cube F₂³: the [[8,3,2]] code introduces CSS codes and transversal gates, and is the worked example for encoding, phases, and overlaps. Reuse the same 48-point support throughout the larger construction.

**Timing:** about 37 minutes including the title and outline, followed by discussion within the one-hour slot. This is a planned delivery budget, not a measured rehearsal. There are 28 numbered slides, five unnumbered transition outlines, and one unnumbered title frame, followed by four backup slides, B1 to B4, for questions on the lower bound and the [CLM+26] framework. The same six-theme outline appears at the start of every theme. The current theme is bright blue and bold. All other themes are shaded in the same fixed positions. Overlay states are separate PDF pages but share one slide number.

## Narrative and checkpoints

| Part | Clock | Purpose |
|---|---|---|
| CSS codes and transversal gates | 0:00–8:35 | Define generator rows on the cube, Pauli strings, CSS codes and transversal gates, with the [[8,3,2]] code as the example and a table of three codes. Pose the construction question. |
| [[8,3,2]] example | 8:35–12:30 | Explain logical CCZ with one code, then derive the signed overlap conditions. |
| Gate conditions | 12:30–15:10 | Place the conditions in context and separate parity completion from sign feasibility. |
| Geometric construction | 15:10–22:10 | State Q48, fix S geometrically, prove the Z-distance floor and divisibility. |
| Column picture and completion | 22:10–30:10 | Translate overlaps into Boolean moments, find K, certify dZ=3, and solve for signs. |
| Bounds and questions | 30:10–37:10 | Explain the Reed–Muller reduction, scope the exclusions, and finish with open questions. |

## Slide-by-slide plan

Slide numbers below are the displayed frame numbers, not PDF page numbers. The title gets 0:00–0:15. Each later outline transition has a ten-second budget within its theme. All other content keeps its existing slide number.

| Slide | Clock | Topic | Essential point |
|---|---|---|---|
| 1 | 0:15–1:00 | Outline | The [[8,3,2]] example, gate conditions, geometry, completion, bounds. |
| 2 | 1:00–2:00 | Generator rows on the cube | Columns labelled by the points of F₂³. Rows u1, u2, their overlap (an edge) and their XOR, as 0/1 strings and on the cube. |
| 3 | 2:00–3:00 | Pauli strings | X(a), Z(b) on basis states. Overlap 2 commutes, overlap 1 anticommutes. |
| 4 | 3:00–4:15 | Stabilizer and CSS codes | Stabilizers, syndrome, [[n,k,d]] with d = min(dX, dZ). X(a) for a in C2, Z(b) for b in the dual of C1. G=[K;S], logical basis. |
| 5 | 4:15–5:45 | The [[8,3,2]] code | Rows K1, K2, K3 = u1, u2, u3 and S = 1, columns labelled by points. Logical states are complement pairs. Z on 000 has syndrome 1. An edge gives a weight-2 logical: dX=4, dZ=2, d=2. |
| 6 | 5:45–6:45 | Clifford and non-Clifford gates | Every gate on basis states. Clifford gates alone are not universal. Add T or CCZ. |
| 7 | 6:45–7:30 | Transversal gates and distillation | One gate per qubit. Eastin–Knill rules out a universal transversal set. Distillation needs transversal T or CCZ. |
| 8 | 7:30–8:35 | Codes with different transversal gates | Steane (H, S), [[15,1,3]] (T is logical T†), [[8,3,2]] (T/T† pattern gives CCZ). State the target. |
| – | 8:35–8:45 | Outline: The [[8,3,2]] code: a worked example of logical CCZ | Current theme bright and bold. All others shaded. |
| 9 | 8:45–9:45 | Signed weight and the gate condition | A coset needs one common phase. Signed weight determines it modulo eight. |
| 10 | 9:45–11:45 | A T/T† pattern for logical CCZ | Ask where T-dagger goes. Face, edge, vertex signed weights are 0, 0, -1. |
| 11 | 11:45–12:30 | The gate condition becomes conditions on generator rows | Singles mod 8, pairs mod 4, triples mod 2. Only the logical triple is odd. |
| – | 12:30–12:40 | Outline: Triorthogonality and the CCZ conditions | Current theme bright and bold. All others shaded. |
| 12 | 12:40–13:40 | Triorthogonal codes and CCZ | Timeline. Triorthogonal matrices have even overlaps, CCZ needs one odd triple. |
| 13 | 13:40–15:10 | Conditions for quasi-transversal CCZ | Nine parity families give quasi-transversal CCZ. Signs need stronger congruences. |
| – | 15:10–15:20 | Outline: Projective geometry and the 48-qubit code | Current theme bright and bold. All others shaded. |
| 14 | 15:20–16:40 | Result: a 48-qubit code with a transversal T/T† CCZ | Q48: dX=16, dZ=3. 26 T and 22 T-dagger, without correction. |
| 15 | 16:40–17:40 | Fix S from finite projective geometry | Projective columns and 8-divisible codewords fix S. Complete K, then signs. |
| 16 | 17:40–18:40 | Projectivity rules out weight-one and weight-two Z logicals | A Z syndrome is a column or a sum of columns. Projectivity detects weights 1 and 2. |
| 17 | 18:40–19:40 | Complement of a projective subspace | 63 projective points minus 15 leaves three blocks of 16. |
| 18 | 19:40–21:10 | Hyperplane sections and codeword weights | A nonzero u coefficient gives weight 24. A pure w coefficient gives 32. |
| 19 | 21:10–22:10 | More geometric constructions | Subspace complements give 13 lengths. Only the starred fixed-support census is complete. |
| – | 22:10–22:20 | Outline: Column indicators, logical rows, and phase signs | Current theme bright and bold. All others shaded. |
| 20 | 22:20–23:40 | Column indicators from the generator matrix | An indicator records occupied columns. [[8,3,2]] gives y, Q48 support gives w1+w2+w1w2. |
| 21 | 23:40–25:10 | The CH conditions are inner products with monomials | Overlap parity equals an indicator-monomial inner product. One cubic moment is odd. |
| 22 | 25:10–26:40 | Logical rows in the column picture | Each geometric point receives three logical bits. Geometry already handles S1-S3. |
| 23 | 26:40–28:40 | Finding the logical rows | Linear row space, compatible pairs, linear third row. Then a weight-three Z witness. |
| 24 | 28:40–30:10 | Solving for the T/T† pattern | Binary sign variables satisfy mod-4 equations. Q48 has 26 T and 22 T-dagger. |
| – | 30:10–30:20 | Outline: Lower bounds and open questions | Current theme bright and bold. All others shaded. |
| 25 | 30:20–32:10 | Stabilizer supports are Reed--Muller codewords | S1-S3 give zero moments through degree 3. Adding the origin fixes weight parity. |
| 26 | 32:10–33:40 | Our exclusion argument covers every length through 38 | Rank reduction, classified supports, complete remaining enumeration: n<=38 excluded. |
| 27 | 33:40–35:40 | Existence of a valid code at different block lengths | Our floor 38. WJS excludes 39-46. Specified 47 code needs correction. Q48 has signs. |
| 28 | 35:40–37:10 | Takeaways and open questions | Geometry fixes S, Boolean constraints complete K, signs certify the T/T† pattern. |

## Delivery choices

Explain the [[8,3,2]] phase through the overlap view only, and use it to derive the general conditions. On the timeline slide, give the progression rather than reading the references. On the construction-family slide, interpret one entry and qualify the census counts. On the search slide, spend time on why the third row becomes linear. Show the explicit sign polynomial as a specification, without reading its terms aloud.

If behind, shorten the historical recap, family table, and final indicator-coset formula. Preserve the distinction between parity conditions and physical signs, the projective distance proof, the Q48 gate pattern, and the scope of the lower bound. The detailed notes give specific cuts at the checkpoints.

Keep these qualifications explicit: projectivity proves dZ≥3, while dX is checked for the completed code. Eight-divisibility is a construction choice. Only the starred fixed-support census is complete. The n≤38 theorem assumes the nine CH conditions. The sign infeasibility of the specified 47-qubit comparison code does not prove 48 minimal for an uncorrected T/T† pattern.

Sources and their updated slide locations are in references.md. The full transcript is in speaking_notes.md, built with the slide images into transcript.pdf, with a matching one-page speaking card.
