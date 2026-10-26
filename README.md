# VTQ Seminar version (Virginia Tech, October 29, 2026)

This branch, `vtq-2026-10-29`, adapts the Applied Algebra talk on `main` for the VTQ seminar: a 60-minute talk, then a separate 30 minutes of questions. The script runs about 43 minutes. It adds an opening slide with the fault-tolerance goal and the result, the Clifford hierarchy, the paper's definition of quasi-transversal CCZ, a final part on using Q48 in a CCZ factory, and a fifth backup slide on the 47-qubit comparison. The Applied Algebra version stays on `main`, and its delivered snapshot on `vt-applied-algebra-2026-10-22`.

Build with `make`. `main.tex` is the Overleaf entry point. `slides.pdf` is the verified slide build. `speaking_card.pdf` is the one-page cue card, and `transcript.pdf` is the rehearsal transcript. There are 31 numbered main slides, six unnumbered transition outlines and one unnumbered title frame, then five backup slides, B1 to B5. Overlay states occupy separate PDF pages and share a slide number. Every theme begins with the same seven-part outline: the current theme is bright blue and bold, and the other themes are shaded.

The signed-weight criterion, geometric support, and 48-qubit code follow Lu and Brown, https://arxiv.org/abs/2610.09341. Literature context includes https://arxiv.org/abs/2609.30860 and https://arxiv.org/abs/2608.23460. The length-47 comparison is https://arxiv.org/abs/2606.07734. Generalized-triorthogonal output equivalence, code length, circuit footprint, and physical sign feasibility are kept distinct.

`speaking_notes.md` is the full talk transcript: a word-for-word script for every frame with clock times, slide numbers, overlay cues, pacing checkpoints, and background notes for the introduction. `make transcript` builds `transcript.pdf`, which shows each slide beside its script. The one-page speaking card follows the same clock. The timing is a planned narration budget. A live rehearsal has not been performed. No expensive searches or numerical hardware benchmarks are part of preparing this deck.

The existing 16:9 Metropolis design is retained. The paper's actual gate-pattern grids are used. Source code and licensed paper figures are editable/reusable under the repository's CC BY 4.0 license.

Historical context: slide 13 places the Bravyi–Haah triorthogonal matrix, the Nezami–Haah classification, and the generalized CCZ constraints. `references.md` records sources and slide locations.

## Edit in Overleaf

Pull the GitHub changes into the linked Overleaf project before editing. Use `main.tex` as the main document and pdfLaTeX as the compiler. If Overleaf has unpublished edits, preserve and reconcile those edits before pulling. GitHub synchronization is manual: push Overleaf edits back to GitHub, then pull locally and rebuild the PDFs. The tracked `slides.pdf` and `speaking_card.pdf` represent the last verified local build.
