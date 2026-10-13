# Speaker notes — 40-minute version

Timing is a planned narration budget, not a measured live rehearsal. The deck has 22 main slides plus a title and six backups. No overlays add hidden timing.

## 1. A code can protect information and implement a gate
Time: 0–1.5 minutes.
Lead with the result. Logical means encoded, physical means the individual systems carrying the block. Single-qubit gates cannot spread a single gate fault across the block. No hardware performance improvement is claimed. CCZ will be defined on slide 5.

## 2. Binary codes describe a quantum encoding
Time: 1.5–3 minutes.
Assume binary linear codes, introduce only the required quantum notation. Ket c is the computational basis vector labelled by the binary word c. The normalization follows from orthogonality of distinct words. Two nested codes specify this CSS code. Do not recite the stabilizer formalism beyond X flips and Z signs.

## 3. The eight-qubit cube starts with affine functions
Time: 3–5 minutes.
The picture labels vertices by u and shows the parity truth table, not a noisy readout. The code is all affine truth tables. The constant row is the one stabilizer generator. The three coordinate rows will label three logical qubits. Keep the same example until slide 6.

## 4. Complementary words encode three logical qubits
Time: 5–7 minutes.
Explain relative phase on the pair: changing the sign of only one word leaves the encoding subspace. The logical gate is defined by the phase common to each pair. The all-X check is exactly the complement swap.

## 5. Single-qubit phases can produce a three-qubit CCZ
Time: 7–8.5 minutes.
T is a phase rotation on physical basis bit 1. Define CCZ before using its resource implications. W is an ordinary integer sum, unlike Boolean XOR. There are four gates of each sign in the cube. Every physical site contributes independently.

## 6. The toy gate works, but its distance is two
Time: 8.5–10 minutes.
For an affine function other than p and p+1, the Hamming distance to p is four. The two exceptional functions have distances zero and eight. Plus and minus four both produce phase minus one. The cube has dX four and dZ two. A single Z has odd parity syndrome, but two Zs can cancel; this explains why the toy is inadequate for the target.

## 7. Overlap counts control weights of sums
Time: 10–11.5 minutes.
Use the face/edge intuition from the cube, but avoid a second running example. Verify the identity at one physical position where all three bits are one: three minus six plus four equals one. Signed weights obey the same pointwise identity.

## 8. The general gate condition is a signed-weight congruence
Time: 11.5–13.5 minutes.
This is the quantum-to-classical bridge. Each summand in a logical coset must have the same phase, so y must disappear. Physical signs are unknowns, not the signs of stabilizer eigenvalues. A global phase is fixed by the zero word.

## 9. Only single, pair, and triple overlaps are needed
Time: 13.5–15.5 minutes.
Derive the coefficients from the previous slide rather than reading a condition list. Minus two forces pair divisibility by four. Four times an odd logical triple supplies the CCZ sign. Gamma is odd, so signed and unsigned triple weights agree modulo two. Parity conditions are necessary for signed implementation but are not sufficient. Explain the term quasi-transversal on this slide only.

## 10. Geometry fixes the stabilizers before the search
Time: 15.5–17 minutes.
Separate design assumptions from necessary conditions. Eight-divisibility is our stabilizer construction choice, not the definition of generalized triorthogonality. The target is dZ at least three and the completed code has dX at least three too. Transition from abstract criteria to explicit geometry.

## 11. Projectivity rules out weight-one and weight-two Z logicals
Time: 17–19 minutes.
Give the short proof. Classical coding theorists recognize the parity-check columns of a distance-three code. In CSS language S is the X check matrix, hence a Z syndrome. This is Z-distance, not a proof of gate-gadget performance or dX.

## 12. The support is projective space minus a subspace
Time: 19–21 minutes.
Recall a point in binary projective space is simply a nonzero vector. The removed subspace is a four-dimensional vector subspace, projective dimension three. The three remaining values of w give three cosets of F2 to the fourth. Dot positions are a coordinate display, not a physical layout.

## 13. Hyperplane sections give the two nonzero weights
Time: 21–23 minutes.
Show the two cases, which prove both rank six and eight-divisibility. All nonzero coordinate combinations have positive weight, so rows are independent. This is the classical coding-theory engine. The classification uniqueness of this support is useful but not needed for construction; reserve it for a question.

## 14. SAT assigns three logical bits to each geometric point
Time: 23–25 minutes.
The count is parity constraints, not the number of ordinary CNF clauses; solver auxiliary variables depend on encoding. SAT finds a candidate, which is then independently checked. Not every compatible labeling has signs. Q48 came from enumeration retaining a labeling with a feasible sign pattern, rather than assuming the first SAT model works.

## 15. The published pattern is a layer of 48 phase gates
Time: 25–26.5 minutes.
Show the actual paper figure, not an independently invented pattern. Counts of inverse gates are six, six, ten. These are coordinate arrangements, not nearest-neighbor hardware requirements. The polynomial form and all-codeword check certify the gate action algebraically.

## 16. A three-point witness makes the Z-distance exact
Time: 26.5–28 minutes.
No X check sees the three sites because the columns sum to zero. The label sum is nonzero, so it is not a stabilizer. The dX value is separately verified for the supplied code; the simple witness only proves dZ. Do not confuse the asymmetry with a completed biased-noise hardware analysis.

## 17. The lower bound turns supports into Reed--Muller words
Time: 28–30.5 minutes.
Give the mechanism, not the full classification. A polynomial indicator records which columns occur. Orthogonality against degree-at-most-three tests comes from the stabilizer overlap parities. The origin does not affect those positive-degree tests, hence n is weight minus c zero. The rank reduction is part of the proof, not an arbitrary rank cutoff.

## 18. Our exclusion argument covers every length through 38
Time: 30.5–33 minutes.
Describe analytic reductions plus finite enumeration honestly. The rank-eight orbit coverage and logical-row exclusions must be complete for the theorem, unlike a sampled SAT search. Cite the existing classifications rather than attributing every normal form to this work. The theorem is scoped to nine CH conditions and does not rule out all imaginable CCZ architectures.

## 19. Concurrent classification closes the 39--46 gap
Time: 33–35 minutes.
The original preprint left 39 through 46 open; the seminar reflects the concurrent classification. The output equivalence is CNOT and S, not arbitrary Clifford operations. Forty-seven is minimal in the quasi-transversal CH class. Do not conclude the forty-seven code is unique or forty-eight minimal for T/T-dagger only. Our infeasibility test refers to the Jacinto comparison code.

## 20. The geometric construction produces a family
Time: 35–37 minutes.
This is a family of finite constructions, not an asymptotic threshold claim. Only the marked fixed-support census is complete; other counts are lower bounds on inequivalent codes found. Use the formula to recover forty-eight at p four q two. Higher dX and dZ construction questions remain meaningful after the short-length gap closes.

## 21. Gate-aware search complements general SAT code design
Time: 37–38.5 minutes.
Keep the comparison factual, not a novelty competition. SAT as a tool is shared; prescribed logical gate constraints are our focus. Their paper explicitly identifies logical-operation fault tolerance as not guaranteed by its current error-detection formulation. Our transversal gate result also does not by itself cost the entire architecture.

## 22. Open questions connect algebra to implementation
Time: 38.5–40 minutes.
Return to the promised bridge between classical codes and logical quantum gates. Forty-seven quasi-transversal minimality is settled, while sign feasibility is a distinct question. Invite classical ideas about divisible codes and completions. Reserve twenty minutes for questions and discussion; do not start a backup without a question.

