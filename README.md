# Boolean functions: applications in quantum error correction and beyond

Source and presentation materials for a 45-minute talk by Bohan Lu. The talk develops an explicit eight-bit classical encoder, carries its Boolean functions into an eight-qubit gate calculation, and explains a 48-qubit quantum error-correction construction. Reed–Muller codes, erasure capacity, and Fourier prediction follow the quantum result.

## Abstract

Boolean functions serve as a meeting ground for algebra, geometry, and Fourier analysis, with applications in computation, communication, and cryptography. Their algebraic and spectral properties help determine how reliably messages can be recovered from noise, how changing individual inputs affects a computation, and how predictable a cryptographic output is from combinations of its inputs. The talk culminates in my work in quantum error correction, where Boolean-function methods help design codes that protect quantum information while implementing logical gates through single-qubit phase rotations.

## Files

- [`main.tex`](main.tex): Overleaf entry point and Beamer source
- [`slides.pdf`](slides.pdf): last locally verified build
- [`abstract.md`](abstract.md): title and abstract
- [`outline.md`](outline.md): slide outline, timing, calculations, and source grounding
- [`speaking_notes.md`](speaking_notes.md): delivery notes following Patrick Winston's *How to Speak* principles

## Build locally

The deck uses pdfLaTeX and `latexmk`. It depends on standard TeX Live packages including Beamer, Metropolis, TikZ, `amsmath`, `mathtools`, `stmaryrd`, `booktabs`, `appendixnumberbeamer`, and Latin Modern fonts.

```sh
make
```

The build runs in `build/` and copies the completed document to `slides.pdf`. The verified deck has 35 PDF pages: one title page, 21 numbered main slides, seven additional overlay pages, and six backup slides. Six main slides use staged reveals. The 45-minute timing includes two seven-second audience pauses. An outside-listener rehearsal remains necessary to assess pacing and comprehension.

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
