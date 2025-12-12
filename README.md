# Label printing script for Zebra EPL2 label printers

Use this script to print sick text labels on your label printer using the [Eltron Programming Language 2 (EPL2)](https://support.zebra.com/cpws/docs/eltron/epl2/EPL2_Prog_revF_old.pdf).

## Setup

1. Ensure an interpreter for the Python programming language is available on your personal computer. Most Macintosh computers provide a suitable version of Python. Ensure that running `python` on your command line succeeds.

  If Python is not available, [uv](https://github.com/astral-sh/uv?tab=readme-ov-file#installation) is the recommended way to manage it.
1. Add your EPL2 label printer as a printer to your Macintosh. Select the CUPS EPL2 driver. See https://youtu.be/DT6gnpzzU60 for guidance.

  Name the printer `type2` to match the current script
1. Clone this repository

## Usage

Navigate to this repository, then run

```
./print.sh "my first label"
```

This will print one label.

```
./print.sh "a label
with multiple lines"
```

will print a multi-line label.

```
./print.sh "stick this everywhere" 2
```

will print 2 copies of the label.

```
./print.sh ":uno-reverse:" 1 r
```

will print the label in reverse-color mode, where the text is highlighted in black and the text is white.

