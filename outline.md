# Virginia Tech Applied Algebra Seminar, October 22, 2026

**Aim:** explain how a transversal CCZ condition becomes a problem about binary row overlaps, then use projective geometry and Boolean equations to construct Q48.

**Audience:** coding theorists, mathematicians, and QEC researchers. Introduce the quantum notation first. Keep the [[8,3,2]] cube as the worked example for encoding, phases, and overlaps. Reuse the same 48-point support throughout the larger construction.

**Timing:** 40 minutes including the title and outline, followed by discussion within the one-hour slot. This is a planned delivery budget, not a measured rehearsal. There are 30 numbered slides, five unnumbered transition outlines, and one unnumbered title frame, with no backups. The same six-theme outline appears at the start of every theme. The current theme is bright teal and bold. All other themes are shaded in the same fixed positions. Overlay states are separate PDF pages but share one slide number.

## Narrative and checkpoints

| Part | Clock | Purpose |
|---|---|---|
| Introduction | 0:00–6:00 | State the route, define CSS codes and transversal gates, pose the construction question. |
| Cube example | 6:00–14:00 | Explain logical CCZ with one code, then derive the signed overlap conditions. |
| Gate conditions | 14:00–17:30 | Place the conditions in context and separate parity completion from sign feasibility. |
| Geometric construction | 17:30–25:00 | State Q48, fix S geometrically, prove the Z-distance floor and divisibility. |
| Column picture and completion | 25:00–33:00 | Translate overlaps into Boolean moments, find K, certify dZ=3, and solve for signs. |
| Bounds and questions | 33:00–40:00 | Explain the Reed–Muller reduction, scope the exclusions, and finish with open questions. |

## Slide-by-slide plan

Slide numbers below are the displayed frame numbers, not PDF page numbers. The title gets 0:00–0:15. Each later outline transition has a ten-second budget within its theme. All other content keeps its existing slide number.

| Slide | Clock | Topic | Essential point |
|---|---|---|---|
| 1 | 0:15–1:00 | Outline | Cube example, gate conditions, geometry, completion, bounds. |
| 2 | 1:00–2:00 | Quantum error correction: qubits and checks | Binary basis labels. X flips, Z signs. Checks and distance. |
| 3 | 2:00–3:30 | CSS codes | S gives X checks. K labels cosets. Distance d is min(dX,dZ). |
| 4 | 3:30–4:45 | Transversal gates and their limits | Independent physical gates contain a gate fault. Universality needs more. |
| 5 | 4:45–6:00 | Codes with different transversal gates | Steane: Clifford. 15 qubits: T. Cube: CCZ. State the target. |
| – | 6:00–6:10 | Outline: The cube code: a worked example of logical CCZ | Current theme bright and bold. All others shaded. |
| 6 | 6:10–7:15 | Qubits indexed by the points of F₂³ | Rows are truth tables. Coordinate faces and the constant span RM(1,3). |
| 7 | 7:15–8:00 | The cube code [[8,3,2]] | S is all ones. K is the three coordinates. Logical states are complement pairs. |
| 8 | 8:00–9:00 | Distances of the cube code | An edge gives a weight-two Z logical. Affine codewords give dX=4. |
| 9 | 9:00–10:00 | Codeword weight, physical phase, and logical phase | A coset needs one common phase. Signed weight determines it modulo eight. |
| 10 | 10:00–11:30 | Choosing the signs on the cube | Put T-dagger on the parity codeword. Only its logical coset gets phase -1. |
| 11 | 11:30–13:15 | Reading the cube phase from overlaps | Face, edge, vertex signed weights are 0, 0, -1. |
| 12 | 13:15–14:00 | The gate condition becomes conditions on generator rows | Singles mod 8, pairs mod 4, triples mod 2. Only the logical triple is odd. |
| – | 14:00–14:10 | Outline: Triorthogonality and the CCZ conditions | Current theme bright and bold. All others shaded. |
| 13 | 14:10–14:45 | Historical context | Distillation, row constraints, parent spaces, and CSS diagonal gates. |
| 14 | 14:45–16:00 | Triorthogonal matrix and triorthogonal space | Distinct matrix rows versus all triples in a space, including repeats. |
| 15 | 16:00–17:30 | Conditions for quasi-transversal CCZ | Nine parity families give quasi-transversal CCZ. Signs need stronger congruences. |
| – | 17:30–17:40 | Outline: Projective geometry and the 48-qubit code | Current theme bright and bold. All others shaded. |
| 16 | 17:40–19:00 | Result: a 48-qubit code with a transversal T/T† CCZ | Q48: dX=16, dZ=3. 26 T and 22 T-dagger, without correction. |
| 17 | 19:00–20:00 | Fix S using finite/projective geometry code | Projective columns and 8-divisible codewords fix S. Complete K, then signs. |
| 18 | 20:00–21:00 | Projectivity rules out weight-one and weight-two Z logicals | A Z syndrome is a column or a sum of columns. Projectivity detects weights 1 and 2. |
| 19 | 21:00–22:00 | Complement of a projective subspace | 63 projective points minus 15 leaves three blocks of 16. |
| 20 | 22:00–23:30 | Hyperplane sections and codeword weights | A nonzero u coefficient gives weight 24. A pure w coefficient gives 32. |
| 21 | 23:30–25:00 | More geometric constructions | Subspace complements give 13 lengths. Only the starred fixed-support census is complete. |
| – | 25:00–25:10 | Outline: Column indicators, logical rows, and phase signs | Current theme bright and bold. All others shaded. |
| 22 | 25:10–26:30 | Column indicators from the generator matrix | An indicator records occupied columns. Cube gives y, Q48 support gives w1+w2+w1w2. |
| 23 | 26:30–28:00 | The CH conditions are inner products with monomials | Overlap parity equals an indicator-monomial inner product. One cubic moment is odd. |
| 24 | 28:00–29:30 | Logical rows in the column picture | Each geometric point receives three logical bits. Geometry already handles S1-S3. |
| 25 | 29:30–31:30 | Finding the logical rows | Linear row space, compatible pairs, linear third row. Then a weight-three Z witness. |
| 26 | 31:30–33:00 | Solving for the T/T† pattern | Binary sign variables satisfy mod-4 equations. Q48 has 26 T and 22 T-dagger. |
| – | 33:00–33:10 | Outline: Lower bounds and open questions | Current theme bright and bold. All others shaded. |
| 27 | 33:10–35:00 | Stabilizer supports are Reed--Muller codewords | S1-S3 give zero moments through degree 3. Adding the origin fixes weight parity. |
| 28 | 35:00–36:30 | Our exclusion argument covers every length through 38 | Rank reduction, classified supports, complete remaining enumeration: n<=38 excluded. |
| 29 | 36:30–38:30 | Existence of a valid code at different block lengths | Our floor 38. WJS excludes 39-46. Specified 47 code needs correction. Q48 has signs. |
| 30 | 38:30–40:00 | Takeaways and open questions | Geometry fixes S, Boolean constraints complete K, signs certify the physical layer. |

## Delivery choices

Explain the cube phase once through distance to the parity codeword, then use the overlap view to derive the general conditions. On the history slide, give the progression rather than reading the references. On the construction-family slide, interpret one entry and qualify the census counts. On the search slide, spend time on why the third row becomes linear. Show the explicit sign polynomial as a specification, without reading its terms aloud.

If behind, shorten the historical recap, family table, and final indicator-coset formula. Preserve the distinction between parity conditions and physical signs, the projective distance proof, the Q48 gate pattern, and the scope of the lower bound. The detailed notes give specific cuts at the checkpoints.

Keep these qualifications explicit: projectivity proves dZ≥3, while dX is checked for the completed code. Eight-divisibility is a construction choice. Only the starred fixed-support census is complete. The n≤38 theorem assumes the nine CH conditions. The sign infeasibility of the specified 47-qubit comparison code does not prove 48 minimal for an uncorrected T/T† layer.

Sources and their updated slide locations are in references.md. The full transcript is in speaking_notes.md, built with the slide images into transcript.pdf, with a matching one-page speaking card.
