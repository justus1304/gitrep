all: build/v70.pdf

# hier Python-Skripte:
build/plot.pdf: plot.py ../matplotlibrc ../header-matplotlib.tex | build
	# so that matplotlib can find the tex header when running
	# LaTeX in the tmp directory
	# and set the matplotlibrc
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python plot.py

#build/plot2.pdf: plot2.py ../matplotlibrc ../header-matplotlib.tex | build
#	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python plot2.py
#
#build/plot3.pdf: plot3.py ../matplotlibrc ../header-matplotlib.tex | build
#	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python plot3.py
#
#build/plot4.pdf: plot4.py ../matplotlibrc ../header-matplotlib.tex | build
#	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python plot4.py
#
#build/plot5.pdf: plot5.py ../matplotlibrc ../header-matplotlib.tex | build
#	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python plot5.py
# hier weitere Abhängigkeiten für build/v70.pdf deklarieren:
build/v70.pdf: #build/plot.pdf build/plot2.pdf build/plot3.pdf build/plot4.pdf build/plot5.pdf

build/v70.pdf: FORCE | build
	# to find header and bib files in the main directory
	TEXINPUTS=..: \
	BIBINPUTS=..: \
	max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	v70.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
