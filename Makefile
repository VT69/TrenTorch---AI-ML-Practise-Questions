.PHONY: all clean

all:
	latexmk -pdf -interaction=nonstopmode -output-directory=out main.tex

clean:
	latexmk -c -output-directory=out
	rm -rf out/*.aux out/*.log out/*.out out/*.fls out/*.fdb_latexmk out/*.synctex.gz
