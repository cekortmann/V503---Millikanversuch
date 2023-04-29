all: build/v503.pdf

build/v503.pdf: v503.tex aufbau.tex auswertung.tex diskussion.tex durchfuehrung.tex fehlerrechnung.tex lit.bib theorie.tex ziel.tex | build
	lualatex  --output-directory=build v503.tex
	lualatex  --output-directory=build v503.tex
	biber build/v503.bcf
	lualatex  --output-directory=build v503.tex


build: 
	mkdir -p build

clean:
	rm -rf build

.PHONY: clean all
