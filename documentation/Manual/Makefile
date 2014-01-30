
SOURCES=student.tex trainer.tex tutor.tex admin.tex

all: $(SOURCES:.tex=.html) $(SOURCES:.tex=.pdf) $(SOURCES:.tex=.epub)

.SUFFIXES: .html .tex .epub .pdf

.tex.html:
	pandoc --toc -s $< -o $@

.tex.pdf:
	pandoc --toc -s $< -o $@

.tex.epub:
	pandoc --toc -s $< -o $@

$(SOURCES:.tex=.html) $(SOURCES:.tex=.pdf) $(SOURCES:.tex=.epub): general.tex

