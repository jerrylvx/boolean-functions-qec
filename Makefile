BUILD_DIR := build
SOURCE_DATE_EPOCH := 0
export SOURCE_DATE_EPOCH
export FORCE_SOURCE_DATE := 1

.PHONY: all pdf speaking-card clean

all: pdf speaking-card

pdf:
	latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=$(BUILD_DIR) main.tex
	cp $(BUILD_DIR)/main.pdf slides.pdf

speaking-card:
	latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=$(BUILD_DIR) speaking_card.tex
	cp $(BUILD_DIR)/speaking_card.pdf speaking_card.pdf

clean:
	latexmk -C -outdir=$(BUILD_DIR) main.tex
	latexmk -C -outdir=$(BUILD_DIR) speaking_card.tex
