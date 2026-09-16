# Boolean functions: applications in quantum error correction and beyond

Source and presentation materials for a 45-minute talk by Bohan Lu. The talk develops an explicit eight-bit classical encoder, derives its decoder and minimum distance, carries the same Boolean functions into an eight-qubit gate calculation, and explains a 48-qubit quantum error-correction construction. A concrete Reed–Muller coding example and a brief visual overview of erasure capacity, Fourier analysis, learning, and cryptography follow the quantum result.

## Abstract

Boolean functions serve as a meeting ground for algebra, geometry, and Fourier analysis, with applications in computation, communication, and cryptography. Their algebraic and spectral properties help determine how reliably messages can be recovered from noise, how changing individual inputs affects a computation, and how predictable a cryptographic output is from combinations of its inputs. The talk culminates in my work in quantum error correction, where Boolean-function methods help design codes that protect quantum information while implementing logical gates through single-qubit phase rotations.

## Files

- [`main.tex`](main.tex): Overleaf entry point and Beamer source
- [`slides.pdf`](slides.pdf): last locally verified build
- [`abstract.md`](abstract.md): title and abstract
- [`outline.md`](outline.md): complete 45-minute running order, per-slide timing and notation cues, reveals, and backup map
- [`speaking_card.pdf`](speaking_card.pdf): one-page, margin-free landscape timing and narration card
- [`speaking_card.tex`](speaking_card.tex): editable source for the cue card
- [`speaking_notes.md`](speaking_notes.md): slide-by-slide narration, prerequisites, transitions, and sequential cold-read findings following Patrick Winston's *How to Speak* principles

## Build locally

The deck uses pdfLaTeX and `latexmk`. It depends on standard TeX Live packages including Beamer, Metropolis, TikZ, `amsmath`, `mathtools`, `stmaryrd`, `booktabs`, `appendixnumberbeamer`, `geometry`, `multicol`, `ragged2e`, and Latin Modern fonts.

```sh
make
```

The build runs in `build/` and refreshes `slides.pdf` and `speaking_card.pdf`. Run `make pdf` for the deck alone or `make speaking-card` for the one-page card. The card uses landscape A4 with zero outer margins and no title; borderless printing or a tablet preserves its full area. The deck has 61 PDF pages: one title page, 27 numbered main slides, 25 additional main reveal pages, six backup frames, and two additional reveal pages in the logical-function backup. Twenty-one main slides use staged reveals. Every backup has a specific anchor question and a clickable return to the anchor’s final state. The classical section distinguishes a particular Hamming distance from the code's minimum distance, and the quantum section introduces quantum distance separately. The 45-minute timing includes two seven-second audience pauses. An outside-listener rehearsal remains necessary to assess pacing and comprehension.

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
