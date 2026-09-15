BUILD_DIR := build
SOURCE_DATE_EPOCH := 0
export SOURCE_DATE_EPOCH
export FORCE_SOURCE_DATE := 1

.PHONY: all pdf clean

all: pdf

pdf:
	latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=$(BUILD_DIR) main.tex
	cp $(BUILD_DIR)/main.pdf slides.pdf

clean:
	latexmk -C -outdir=$(BUILD_DIR) main.tex
