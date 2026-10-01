# A 48-qubit code with native CCZ

## Structure and timing

Audience: general quantum error correction. The talk assumes stabilizer and CSS codes, Clifford+T, magic-state distillation, and transversal gates.
Content follows the paper *Building codes with transversal CCZ using projective geometry and SAT solvers* (Lu and Brown).

The deck has **25 numbered main slides, 8 backup frames, and 39 PDF pages**.
Four main frames use overlays (slides 9, 13, 19, 20).

| Portion | Time | Duration |
| --- | --- | ---: |
| Title and 1–2: problem and roadmap | 00:00–03:30 | 3:30 |
| 3–10: Boolean functions as a language for codes, cube code | 03:30–19:00 | 15:30 |
| 11–16: gate criterion | 19:00–27:30 | 8:30 |
| 17–24: construction of Q48 | 27:30–42:00 | 14:30 |
| 25: summary | 42:00–45:00 | 3:00 |

## Running order

| Slide | Time | Focus and notation |
| --- | --- | --- |
| Title | 00:00–00:30 | Promise |
| 1. Why a native CCZ gate | 00:30–02:30 | Distillation versus transversal gates, native implementation |
| 2. This talk | 02:30–03:30 | Result and four-part roadmap |
| 3. Codewords are truth tables | 03:30–06:00 | Truth table, f_{a,b}, RM(1,3), columns as points |
| 4. Truth tables are polynomials | 06:00–07:30 | Algebraic normal form, degree, f ∧ g, RM(ℓ,m) |
| 5. Overlaps count shared ones | 07:30–09:30 | Weight, overlap, \|f ⊕ g\| = \|f\| + \|g\| − 2\|f ∧ g\| |
| 6. Nonconstant affine functions are balanced | 09:30–11:00 | Weight 2^{m−1} |
| 7. Degree controls divisibility | 11:00–13:30 | McEliece bound, 15-qubit code, PG(3,2) |
| 8. Why Boolean functions, for QEC and for this project | 13:30–15:30 | Dictionary and project payoffs |
| 9. Warm-up: the eight-qubit cube code | 15:30–18:00 | f_a, parity p, signed weight sw, ω |
| 10. The cube code has distance two | 18:00–19:00 | Z_u, d_Z = 2 |
| 11. A CSS code as a binary matrix | 19:00–20:30 | G = [K; S], coset sum, d_X, d_Z |
| 12. The logical gate becomes a phase condition | 20:30–22:00 | Pattern Γ, sw_Γ, native CCZ condition |
| 13. XOR turns the phase into overlap counts | 22:00–23:00 | Triple identity, truncation mod 8 |
| 14. Signed overlaps decide the native gate | 23:00–24:30 | Native criterion |
| 15. Quasi-transversal versus native | 24:30–26:00 | Nine conditions, phase gate P |
| 16. One Boolean function packages every overlap | 26:00–27:30 | Column indicator χ_G |
| 17. The construction runs in three steps | 27:30–28:30 | S, then K, then signs |
| 18. Distinct nonzero columns give d_Z ≥ 3 | 28:30–30:00 | Syndrome, PG(s−1,2) |
| 19. Weights are read from hyperplane sections | 30:00–31:30 | 8-divisible, H_a |
| 20. FG48: projective space minus a solid | 31:30–34:00 | Weights 24 and 32, uniqueness |
| 21. Logical rows by SAT | 34:00–36:00 | 144 variables, 88 constraints |
| 22. The logical rows of Q48 | 36:00–37:30 | K₁, K₂, K₃ per block |
| 23. Signs from a linear system over Z₄ | 37:30–39:30 | γ, Q₁, Q₂, 26 T + 22 T† |
| 24. The code Q48 = [[48,3,3]] | 39:30–42:00 | d_X = 16, weight-3 Z logical |
| 25. Summary: known and open lengths | 42:00–45:00 | Lengths table, open problems |

## Backups

| Backup | Anchor | Question |
| --- | --- | --- |
| The nine conditions with index ranges | Slide 15 | Which rows enter each condition? |
| Why FG48 has only weights 24 and 32 | Slide 20 | Why two weights, and why unique? |
| The nine conditions do not imply native | Slide 25 | Why is the 47-qubit code not native? |
| Stabilizer conditions restrict the length | Slide 25 | How does the lower bound work? (step 1) |
| No code below length 39 | Previous backup | How does the lower bound work? (step 2) |
| A family with all-T CCZ | Slide 25 | Which longer codes need no T†? |
| Affine changes of coordinates preserve everything | Lower-bound proof | Why one support per affine class? |
| Sources | Slide 25 | Where can I read more? |
