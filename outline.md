# A 48-qubit code with native CCZ

## Structure and timing

Audience: general quantum error correction. The talk assumes stabilizer and CSS codes, Clifford+T, magic-state distillation, and transversal gates.
Content follows the paper *Building codes with transversal CCZ using projective geometry and SAT solvers* (Lu and Brown).

The deck has **23 numbered main slides, 4 backup frames, and 33 PDF pages**.
Four main frames use overlays (slides 3, 7, 13, 14).

| Portion | Time | Duration |
| --- | --- | ---: |
| Title and 1–4: problem, results, cube code | 00:00–07:30 | 7:30 |
| 5–10: Boolean-function criterion | 07:30–19:00 | 11:30 |
| 11–18: construction of Q48 | 19:00–33:00 | 14:00 |
| 19–22: limits | 33:00–42:00 | 9:00 |
| 23: summary and open problems | 42:00–45:00 | 3:00 |

## Running order

| Slide | Time | Focus and notation |
| --- | --- | --- |
| Title | 00:00–00:30 | Promise |
| 1. Why a native CCZ gate | 00:30–02:30 | Distillation versus transversal gates, native implementation, target |
| 2. Results: known and open lengths | 02:30–04:00 | n ≤ 38 excluded, 39–46 open, 47 not native, 48 native |
| 3. Warm-up: the eight-qubit cube code | 04:00–06:30 | f_a, parity p, signed weight sw, ω = e^{iπ/4} |
| 4. The cube code has distance two | 06:30–07:30 | Z_u, d_Z = 2 |
| 5. A CSS code as a binary matrix | 07:30–09:30 | G = [K; S], C₂ ⊂ C₁, coset sum, d_X, d_Z |
| 6. The logical gate becomes a phase condition | 09:30–11:30 | Pattern Γ, sw_Γ, native CCZ condition |
| 7. XOR turns the phase into overlap counts | 11:30–13:30 | ∧, coefficient (−2)^{t−1}, truncation mod 8 |
| 8. Signed overlaps decide the native gate | 13:30–15:30 | Native criterion |
| 9. Quasi-transversal versus native | 15:30–17:30 | Nine conditions K1–K3, KS1–KS3, S1–S3, phase gate P |
| 10. One Boolean function packages every overlap | 17:30–19:00 | Column indicator χ_G |
| 11. The construction runs in three steps | 19:00–20:00 | S, then K, then signs |
| 12. Distinct nonzero columns give d_Z ≥ 3 | 20:00–21:30 | Syndrome β_j, PG(s−1,2), projective code |
| 13. Weights are read from hyperplane sections | 21:30–23:00 | 8-divisible, hyperplane H_a |
| 14. FG48: projective space minus a solid | 23:00–25:30 | (u, w), weights 24 and 32, uniqueness |
| 15. Logical rows by SAT | 25:30–27:30 | Labels α_j, 144 variables, 88 constraints |
| 16. The logical rows of Q48 | 27:30–29:00 | K₁, K₂, K₃ per block |
| 17. Signs from a linear system over Z₄ | 29:00–31:00 | γ, Q₁, Q₂, 26 T + 22 T† |
| 18. The code Q48 = [[48,3,3]] | 31:00–33:00 | d_X = 16, weight-3 Z logical |
| 19. The nine conditions do not imply native | 33:00–35:00 | Jacinto et al. [[47,3,3]] |
| 20. Stabilizer conditions restrict the length | 35:00–37:30 | χ_S ∈ RM(s−4, s) + ⟨δ₀⟩ |
| 21. No code below length 39 | 37:30–40:00 | Lower-bound proof structure |
| 22. A family with all-T CCZ | 40:00–42:00 | Subspace complements, n = 2^s − 2^p ≥ 64 |
| 23. Summary and open problems | 42:00–45:00 | No new notation |

## Backups

| Backup | Anchor | Question |
| --- | --- | --- |
| The nine conditions with index ranges | Slide 9 | Which rows enter each condition? |
| Why FG48 has only weights 24 and 32 | Slide 14 | Why two weights, and why unique? |
| Affine changes of coordinates preserve everything | Slide 21 | Why one support per affine class? |
| Sources | Slide 23 | Where can I read more? |
