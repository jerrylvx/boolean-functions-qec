# Boolean functions: applications in quantum error correction and beyond

Source for a 45-minute talk by Bohan Lu for a general quantum error-correction audience. The talk presents the native-CCZ construction of the paper *Building codes with transversal CCZ using projective geometry and SAT solvers* (Lu and Brown): the warm-up eight-qubit cube code, the signed-overlap criterion for a native $T/T^\dagger$ CCZ, the 48-qubit code $Q_{48}$ built from the FG48 stabilizer support, the non-native 47-qubit comparison code, the length lower bound $n\le38$, and an all-$T$ family on subspace complements.

This branch (`qec-audience-talk`) replaces the seminar deck. The seminar version, *Boolean functions: applications in quantum error correction and beyond*, remains on `main`. [`abstract.md`](abstract.md), [`speaking_notes.md`](speaking_notes.md), and [`speaking_card.tex`](speaking_card.tex) still describe the seminar version.

## Files

- [`main.tex`](main.tex): Overleaf entry point and Beamer source
- [`slides.pdf`](slides.pdf): last locally verified build
- [`abstract.md`](abstract.md): title and abstract
- [`outline.md`](outline.md): 45-minute running order and backup map for this deck
- [`figures/hypercube6.tex`](figures/hypercube6.tex): the $Q_{48}$ hypercube figure, copied from the paper repository and recolored
- [`speaking_card.pdf`](speaking_card.pdf): one-page, margin-free landscape timing and narration card
- [`speaking_card.tex`](speaking_card.tex): editable source for the cue card
- [`speaking_notes.md`](speaking_notes.md): slide-by-slide narration, prerequisites, transitions, and sequential cold-read findings following Patrick Winston's *How to Speak* principles

## Build locally

The deck uses pdfLaTeX and `latexmk`. It depends on standard TeX Live packages including Beamer, Metropolis, TikZ, `amsmath`, `mathtools`, `stmaryrd`, `booktabs`, `appendixnumberbeamer`, `geometry`, `multicol`, `ragged2e`, and Latin Modern fonts.

```sh
make
```

The build runs in `build/` and refreshes `slides.pdf` and `speaking_card.pdf`. Run `make pdf` for the deck alone or `make speaking-card` for the one-page card. The card uses landscape A4 with zero outer margins and no title; borderless printing or a tablet preserves its full area. The deck has 33 PDF pages: one title page, 23 numbered main slides, 5 additional main reveal pages, and 4 backup frames. Every backup has an anchor question and a clickable return to its anchor slide. An outside-listener rehearsal remains necessary to assess pacing.

## Edit with Overleaf and GitHub

This repository is intended to be imported as a new Overleaf project:

1. Link the GitHub account in Overleaf **Account Settings**.
2. Choose **New Project → Import from GitHub** and select `jerrylvx/boolean-functions-qec`.
3. Use `main.tex` as the main document and pdfLaTeX as the compiler.
4. In **Integrations → GitHub**, pull GitHub changes before editing and push Overleaf changes back when finished.

GitHub synchronization is manual, not continuous. Treat GitHub and Overleaf as two writers: synchronize before starting, avoid editing the same source in both places concurrently, and resolve any synchronization branch before continuing. After pushing an Overleaf edit to GitHub, pull it locally, run `make`, and push the refreshed `slides.pdf`. Until then, the tracked PDF represents the last verified local build rather than the newest Overleaf source.

Overleaf documents the workflow and its limitations in [GitHub synchronization](https://docs.overleaf.com/integrations-and-add-ons/git-integration-and-github-synchronization/github-synchronization).

## License

Copyright 2026 Bohan Lu. The presentation and supporting materials are licensed under the [Creative Commons Attribution 4.0 International License](LICENSE).
