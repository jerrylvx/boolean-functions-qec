BUILD_DIR := build
SOURCE_DATE_EPOCH := 0
export SOURCE_DATE_EPOCH
export FORCE_SOURCE_DATE := 1

.PHONY: all pdf speaking-card transcript clean

all: pdf speaking-card transcript

pdf:
	latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=$(BUILD_DIR) main.tex
	cp $(BUILD_DIR)/main.pdf slides.pdf

speaking-card:
	latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=$(BUILD_DIR) speaking_card.tex
	cp $(BUILD_DIR)/speaking_card.pdf speaking_card.pdf

transcript: pdf
	python3 -I scripts/transcript_pdf.py speaking_notes.md $(BUILD_DIR)/main.nav $(BUILD_DIR)/transcript.tex
	latexmk -lualatex -interaction=nonstopmode -halt-on-error -outdir=$(BUILD_DIR) $(BUILD_DIR)/transcript.tex
	cp $(BUILD_DIR)/transcript.pdf transcript.pdf

clean:
	latexmk -C -outdir=$(BUILD_DIR) main.tex
	latexmk -C -outdir=$(BUILD_DIR) speaking_card.tex
	latexmk -C -outdir=$(BUILD_DIR) $(BUILD_DIR)/transcript.tex
