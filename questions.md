# Anticipated technical questions

* **Why does projectivity give Z-distance three?** Nonzero distinct columns of S give nonzero syndromes for all Z errors of weight one or two. The argument concerns Z-distance; dX is checked separately.
* **Why 8-divisibility?** It is a sufficient stabilizer design assumption yielding the stabilizer overlap parities, stronger than those parities alone. The logical rows and physical signs still require tests.
* **Is the cube a [[8,3,3]] code?** No. The cube is [[8,3,2]], with dX=4 and dZ=2. The phase mechanism works, but the code fails the target distance.
* **What exactly is SAT solving?** 144 logical-label bits subject to 88 parity constraints for the fixed 48-point support. Auxiliary encoding variables and CNF clause counts differ. Binary physical signs are tested separately.
* **Was the first SAT model the published code?** No. Enumeration retained a compatible labeling with feasible signs; a compatible labeling alone does not establish a physical T/T-dagger implementation.
* **Does the new classification prove 48 minimal?** No. It establishes 47 as the shortest quasi-transversal CCZ length in the stated class. The sign obstruction applies to the Jacinto comparison code, not automatically every code at length 47.
* **Why trust the lower bound?** The theorem combines cited classifications, analytic reductions, exhaustive rank-eight orbit coverage, and exact logical-row exclusions. The repository distinguishes retained exhaustive evidence from fast checks; no new classification is run for this talk.
* **Is code length the number of factory qubits?** No. n counts code positions or noisy T inputs; N counts the circuit footprint in the cited distillation description. A 47-input protocol can have footprint 9.
* **What hardware benefit is demonstrated?** The paper establishes code and gate properties. Full noisy circuits and resource comparisons are future work.
* **What do the new citations add?** Wills–Jain–Singh supply the finite classification and short-length exclusion. DalFavero et al. supply general SAT code discovery/extension with prescribed errors; error detection alone does not guarantee fault-tolerant logical operations.

* **Is Q48 an ordinary triorthogonal T code?** No. Its odd logical triple implements CCZ and violates the ordinary distinct-triple even condition. The stabilizer-side unital-space/indicator methods can still be used.
* **What is a triorthogonal space versus a matrix?** A space satisfies the triple condition for every triple, including repeats; a Bravyi–Haah matrix constrains distinct row indices and can contain odd logical rows. Unital adds the all-ones vector.
* **Did we originate the Reed–Muller indicator method?** No. Nezami and Haah provide the indicator representation and its classification connection; our paper applies the stabilizer-support version to the CCZ constraint class.
