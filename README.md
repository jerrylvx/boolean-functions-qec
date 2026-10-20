# Virginia Tech Applied Algebra Seminar, third talk version

October 22, 2026. Target: 40 minutes with time for questions within the one-hour seminar. The latest Virginia Tech version is on `main`. The previous broad seminar is preserved on `seminar-broad-2026-09`. The earlier QEC audience deck remains on `qec-audience-talk`, and the prepared Virginia Tech snapshot remains on `vt-applied-algebra-2026-10-22`.

Build with `make`. `main.tex` is the Overleaf entry point. `slides.pdf` is the verified slide build. `speaking_card.pdf` is the one-page cue card, and `transcript.pdf` is the rehearsal transcript. `outline.md`, `speaking_notes.md`, `abstract.md`, and `questions.md` belong to this version. There are 30 numbered main slides, including the opening outline, plus five unnumbered transition outlines and one unnumbered title frame. There are no backup slides. Overlay states occupy separate PDF pages and share a slide number. Every theme begins with the same outline: the current theme is bright teal and bold, and the other themes are shaded. The 40-minute plan includes the title and all six outline appearances.

The signed-weight criterion, geometric support, and 48-qubit code follow Lu and Brown, https://arxiv.org/abs/2610.09341. Literature context includes https://arxiv.org/abs/2609.30860 and https://arxiv.org/abs/2608.23460. The length-47 comparison is https://arxiv.org/abs/2606.07734. Generalized-triorthogonal output equivalence, code length, circuit footprint, and physical sign feasibility are kept distinct.

`speaking_notes.md` is the full talk transcript: a word-for-word script for every frame with clock times, slide numbers, overlay cues, pacing checkpoints, and background notes for the introduction. `make transcript` builds `transcript.pdf`, which shows each slide beside its script. The one-page speaking card follows the same clock. The timing is a planned narration budget. A live rehearsal has not been performed. No expensive searches or numerical hardware benchmarks are part of preparing this deck.

The existing 16:9 Metropolis design is retained. The paper's actual gate-pattern grids are used. Source code and licensed paper figures are editable/reusable under the repository's CC BY 4.0 license.

Historical context: slides 13–14 distinguish the Bravyi–Haah matrix, Nezami–Haah unital space, and the generalized CCZ constraints. `references.md` records sources and slide locations.

## Edit in Overleaf

Pull the GitHub changes into the linked Overleaf project before editing. Use `main.tex` as the main document and pdfLaTeX as the compiler. If Overleaf has unpublished edits, preserve and reconcile those edits before pulling. GitHub synchronization is manual: push Overleaf edits back to GitHub, then pull locally and rebuild the PDFs. The tracked `slides.pdf` and `speaking_card.pdf` represent the last verified local build.
