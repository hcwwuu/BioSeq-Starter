# BioSeq-Starter

**English | [中文](README.zh-CN.md)**

> A beginner-friendly bioinformatics Python project built around one idea: **learn by building**.

BioSeq-Starter is not intended to be a powerful or production-ready bioinformatics tool.

The final program is intentionally small.

The main value of this repository is the **step-by-step learning process**: starting from an empty Python project, gradually adding biological data input, basic sequence algorithms, Biopython, visualization, error handling, modular design, and finally Git/GitHub project management.

Instead of learning Python syntax, bioinformatics libraries, data formats, and software engineering separately, this project connects them through one small but complete workflow.

---

## What You Will Learn

By completing the project step by step, you will practice:

### Python

* Variables and data types
* Strings
* Lists, sets, and dictionaries
* `if` statements
* `for` loops
* Functions
* Parameters and return values
* Modules
* Exception handling
* `main()` program structure

### Bioinformatics

* FASTA format
* DNA sequence representation
* Sequence validation
* Nucleotide composition
* GC content
* Reverse complement
* DNA transcription
* Protein translation

### Python Libraries

* Biopython
* Matplotlib

### Basic Software Engineering

* Virtual environments
* Dependency management
* Modular code organization
* Input validation
* Error handling
* Git version control
* GitHub repositories
* README documentation

---

# Learning Roadmap

The recommended way to use this repository is **not to copy the final code directly**.

Start from an empty directory and build the project stage by stage.

---

## Stage 0: Set Up the Development Environment

Before writing bioinformatics code, create an isolated Python environment.

Recommended environment:

* Windows
* VS Code
* Python 3.13
* Python virtual environment (`venv`)

Create the project directory:

```text
BioSeq-Starter/
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it in Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the libraries:

```bash
python -m pip install biopython matplotlib
```

At this stage, the important idea is:

```text
System Python
      ↓
Project-specific virtual environment
      ↓
Project dependencies
```

### What you learn

* What a Python interpreter is
* What `pip` does
* Why virtual environments are useful
* How VS Code selects a Python interpreter

---

## Stage 1: Read Your First FASTA File

Create:

```text
data/
└── example.fasta
```

Example:

```text
>example_sequence
ATGGCCATTGTAATGGGCCGCTGA
```

Use Biopython:

```python
from Bio import SeqIO
```

Then read the file with:

```python
record = SeqIO.read("data/example.fasta", "fasta")
```

Explore:

```python
record.id
record.description
record.seq
```

At this stage, the workflow becomes:

```text
FASTA file
    ↓
SeqIO
    ↓
SeqRecord
    ↓
DNA sequence
```

### What you learn

* What FASTA files look like
* How biological sequence data is stored
* How Python reads external files
* `SeqIO`
* `SeqRecord`
* `Bio.Seq.Seq`

---

## Stage 2: Implement Basic Sequence Algorithms Yourself

Before relying on existing Biopython functions, implement several simple algorithms using basic Python.

Build functions such as:

```python
validate_sequence()
count_bases()
gc_content()
reverse_complement()
```

### Sequence validation

Check whether a DNA sequence contains only:

```text
A T C G
```

This introduces:

* Sets
* Loops
* Conditional statements
* Boolean values

### Nucleotide counting

Count the number of:

```text
A
T
C
G
```

using a Python dictionary.

This introduces:

* Dictionaries
* Indexing
* Counters
* Iteration

### GC content

Calculate the proportion of `G` and `C` nucleotides.

Instead of repeating the counting logic, reuse:

```python
count_bases()
```

This introduces an important programming idea:

> Functions should reuse existing logic instead of duplicating code.

### Reverse complement

Implement the nucleotide mapping:

```text
A ↔ T
C ↔ G
```

and traverse the sequence in reverse order.

This introduces:

* Dictionaries as mappings
* `reversed()`
* String construction

### Why implement these manually?

Biopython already provides convenient ways to perform many of these operations.

However, implementing the simple versions manually helps beginners understand what the library is doing and provides practice with fundamental Python syntax.

---

## Stage 3: Use Biopython for Biological Operations

Not everything should be reimplemented manually.

For standard biological operations, use mature libraries.

Convert the sequence to a Biopython `Seq` object:

```python
from Bio.Seq import Seq

dna = Seq(sequence)
```

Transcribe DNA:

```python
rna = dna.transcribe()
```

Translate RNA:

```python
protein = rna.translate()
```

The workflow now becomes:

```text
DNA
 ↓
transcribe()
 ↓
RNA
 ↓
translate()
 ↓
Protein
```

### What you learn

* Difference between a Python `str` and `Bio.Seq.Seq`
* Functions versus object methods
* DNA transcription
* Codons
* Protein translation
* Stop codons

### An important design idea

Simple algorithms such as nucleotide counting are useful to implement manually for learning.

Complex and standardized biological operations should usually use established libraries.

This introduces an important engineering decision:

> Know when to implement something yourself and when to use a reliable library.

---

## Stage 4: Visualize the Results

Use Matplotlib:

```python
import matplotlib.pyplot as plt
```

Take the nucleotide-count dictionary:

```text
A → count
T → count
C → count
G → count
```

and create a bar chart.

The program saves the result to:

```text
results/nucleotide_distribution.png
```

### Example Visualization

![Nucleotide Distribution](results/nucleotide_distribution.png)

### What you learn

* Converting dictionaries into plotting data
* `keys()` and `values()`
* Python lists
* Matplotlib
* Bar charts
* Saving program-generated files

At this point, the project has a complete data flow:

```text
Input
 ↓
Analysis
 ↓
Biological transformation
 ↓
Visualization
```

---

## Stage 5: Turn a Script into a Small Project

The first versions can live entirely inside:

```text
main.py
```

But as the program grows, separate the responsibilities.

Move sequence-processing functions into:

```text
analyzer.py
```

For example:

```text
analyzer.py
├── validate_sequence()
├── count_bases()
├── gc_content()
└── reverse_complement()
```

Then import them into:

```python
main.py
```

The main file becomes responsible for the overall workflow rather than the implementation of every algorithm.

Add:

```python
def main():
    ...
```

and:

```python
if __name__ == "__main__":
    main()
```

Also introduce error handling for cases such as:

* FASTA file not found
* Empty DNA sequence
* Invalid nucleotide characters
* Invalid FASTA input

### What you learn

* Modules
* Imports
* Separation of responsibilities
* Local variables and function parameters
* `main()`
* `if __name__ == "__main__"`
* `try`
* `except`
* `raise`
* `ValueError`
* `FileNotFoundError`

This is the stage where the code begins to move from:

```text
a Python exercise
```

to:

```text
a small Python project
```

---

## Stage 6: Manage the Project with Git and GitHub

Once the program works, turn the directory into a Git repository.

Add:

```text
.gitignore
requirements.txt
README.md
README.zh-CN.md
```

The `.gitignore` prevents local files such as:

```text
.venv/
__pycache__/
.vscode/
```

from being committed.

The `requirements.txt` records the direct dependencies:

```text
biopython
matplotlib
```

Initialize Git:

```bash
git init
```

Inspect changes:

```bash
git status
```

Stage files:

```bash
git add .
```

Create a commit:

```bash
git commit -m "Initial BioSeq Starter"
```

Connect the repository to GitHub and push it.

### What you learn

* Working directory
* Staging area
* Commits
* Branches
* `main`
* Remote repositories
* `origin`
* `push`
* `.gitignore`
* Dependency documentation

At this stage, the project is no longer just code on one computer.

It becomes a reproducible and shareable project.

---

# Final Project Structure

After completing all stages, the project becomes:

```text
BioSeq-Starter/
│
├── main.py
├── analyzer.py
├── README.md
├── README.zh-CN.md
├── requirements.txt
├── .gitignore
│
├── data/
│   └── example.fasta
│
└── results/
    └── nucleotide_distribution.png
```

The final program follows this workflow:

```text
example.fasta
      ↓
Biopython SeqIO
      ↓
DNA sequence
      ↓
Sequence validation
      ↓
Basic Python algorithms
      ├── nucleotide counts
      ├── GC content
      └── reverse complement
      ↓
Biopython Seq
      ↓
DNA → RNA → Protein
      ↓
Matplotlib
      ↓
nucleotide_distribution.png
```

---

# Final Features

The current basic version supports:

* Reading a single DNA sequence from `data/example.fasta`
* DNA sequence validation
* Sequence length calculation
* A/T/C/G nucleotide counting
* GC content calculation
* Reverse complement generation
* DNA transcription to RNA
* RNA translation to protein
* Nucleotide distribution visualization
* Basic input and file error handling

The feature set is intentionally small.

The purpose of this repository is not to provide a complete bioinformatics toolkit, but to make the entire development process understandable to beginners.

---

# Quick Start

Clone the repository:

```bash
git clone https://github.com/hcwwuu/BioSeq-Starter.git
```

Enter the directory:

```bash
cd BioSeq-Starter
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Replace the DNA sequence inside:

```text
data/example.fasta
```

Then run:

```bash
python main.py
```

---

# Where to Go Next

After understanding the basic version, possible extensions include:

### Multiple FASTA Sequences

Replace:

```python
SeqIO.read()
```

with multi-record processing using:

```python
SeqIO.parse()
```

### ORF Finder

Search for open reading frames using:

```text
ATG
 ↓
coding sequence
 ↓
TAA / TAG / TGA
```

### Motif Searching

Search for specific nucleotide patterns inside sequences.

### NCBI Integration

Retrieve real biological sequences from public databases.

### BLAST

Submit sequences for similarity searching.

### Command-Line Interface

Allow users to run:

```bash
python main.py data/example.fasta
```

instead of using a fixed input path.

---

# Why BioSeq-Starter?

A final working program may only contain a small amount of code.

But the learning process behind it covers much more:

```text
Python environment
        ↓
Python syntax
        ↓
FASTA data
        ↓
Basic algorithms
        ↓
Biopython
        ↓
Data visualization
        ↓
Error handling
        ↓
Modules
        ↓
Git
        ↓
GitHub
```

That progression is the main purpose of BioSeq-Starter.

**The goal is not simply to obtain the final code. The goal is to understand how the final code is built.**
