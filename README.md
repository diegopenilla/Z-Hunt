# Z-Hunt

Open the Notebook using this link [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/diegopenilla/Z-Hunt/master) and open *Tutorial.ipynb* or *Execute.ipynb*.


## Z Hunt Tutorial

This program was written in Python 3.6 using Jupyter Notebooks and displays a graphical interface for analyzing the data produced by [Z-Hunt II](http://www.jbc.org/content/267/17/11846.full.pdf), an updated version of [Z-Hunt](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1167176/pdf/emboj00173-0317.pdf) that analyzes a given DNA sequence and looks up for regions with potential to form Z-DNA. As mentioned by the authors:

> " The computer program (Z-Hunt-II) developed for this study uses a rigorous thermodynamic search strategy to map the occurrence of left-handed Z-DNA in genomic sequences. The search algorithm has been optimized to search large sequences for the potential occurrence of Z-DNA, taking into account sequence type, length, and cooperativity for a given stretch of potential Z-DNA-forming nucleotides."

To do this the program computes for each base pair of the given DNA sequence, a value called **Z-Score**.
> "In practical terms, the Z-Score relates the ability for a given sequence to adopt the Z conformation relative to a random sequence. We can also interpret the Z-Score as the number of random sequences that must be searched to find a nucleotide sequence that is as good or better at forming Z-DNA than the sequence in question."

Z-Hunt II accepts 5 arguments to run:

- *DNA*: as a sequence made up A, T, G and C.
- *windowsize*: the length of the search window.
- *minsize*
- *maxsize*
- *filename*: the name of the text file with the results.

Using the user interface, these arguments are defined by changing the values inside of text windows. **The default values of: *windowsize, minsize* and *maxsize* don't need to be necessarily changed by the user** (they replicate correctly the results shown by the published articles). In the end, the  program is very simple to use and requires the user to only input a DNA sequence and a name (for the results). The results can be explored in different ways by using buttons to call upon various functions. 


