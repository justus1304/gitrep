all: build/v51.pdf

# hier Python-Skripte:
build/plot.pdf: plot.py ../matplotlibrc ../header-matplotlib.tex | build
	# so that matplotlib can find the tex header when running
	# LaTeX in the tmp directory
	# and set the matplotlibrc
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python plot.py

build/L1_f_fb.pdf: L1_f_fb.py ../matplotlibrc ../header-matplotlib.tex | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python L1_f_fb.py
build/L2_f_fb.pdf: L2_f_fb.py ../matplotlibrc ../header-matplotlib.tex | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python L2_f_fb.py
build/L3_f_fb.pdf: L3_f_fb.py ../matplotlibrc ../header-matplotlib.tex | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python L3_f_fb.py
build/L4_f_fb.pdf: L4_f_fb.py ../matplotlibrc ../header-matplotlib.tex | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python L4_f_fb.py


# hier weitere Abhängigkeiten für build/v51.pdf deklarieren:
build/v51.pdf: build/plot.pdf
build/v51.pdf: build/L1_f_fb.pdf
build/v51.pdf: build/L2_f_fb.pdf
build/v51.pdf: build/L3_f_fb.pdf
build/v51.pdf: build/L4_f_fb.pdf

build/v51.pdf: FORCE | build
	# to find header and bib files in the main directory
	TEXINPUTS=..: \
	BIBINPUTS=..: \
	max_print_line=1048576 \
	latexmk \
	  -pvc \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	v51.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
