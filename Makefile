# StackOverflow suggests this as a general Makefile for latex
# https://tex.stackexchange.com/a/318595/62076
#
# This Makefile depends on the file ./latexmkrc to be able to build the
# glossary, as noted in: https://tex.stackexchange.com/a/1228/62076
#
# Tools
LATEXMK = latexmk
RM = rm -f

# Project-specific settings
DOCNAME = main

# Targets
all: doc
doc: pdf
pdf: $(DOCNAME).pdf

# Rules
%.pdf: %.tex
	$(LATEXMK) -pdf -M -MP -MF $*.d $*
	open main.pdf

mostlyclean:
	$(LATEXMK) -silent -c
	$(RM) *.bbl
	$(RM) *.glg *.glo *.gls *.ist # glossaries

clean: mostlyclean
	$(LATEXMK) -silent -C
	$(RM) *.run.xml *.synctex.gz
	$(RM) *.d

.PHONY: all clean doc mostlyclean pdf

# Include auto-generated dependencies
-include *.d
