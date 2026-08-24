from Bio import SeqIO
from Bio.Seq import Seq
import matplotlib.pyplot as plt

from analyzer import (
    validate_sequence,
    count_bases,
    gc_content,
    reverse_complement
)# Sequence analysis functions

def plot_base_counts(count):
    x = list(count.keys()) # Convert to a standard Python list
    y = list(count.values())

    plt.bar(x, y)
    plt.title("Nucleotide Distribution")
    plt.xlabel("Nucleotide")
    plt.ylabel("Count")
    plt.savefig("results/nucleotide_distribution.png")
    plt.show()

def main():
    # Read FASTA file
    try:
        record = SeqIO.read("data/example.fasta", "fasta")
    except FileNotFoundError:
        print("Error: FASTA file not found")
        exit()
    except ValueError as error:
        print("Error:", error)
        exit()

    sequence = str(record.seq).upper()
    if not sequence:
        raise ValueError("DNA sequence is empty.")
    if not validate_sequence(sequence):
        raise ValueError("Invalid DNA sequence. Only A, T, C and G are allowed.")
    #print("Is the sequence legal? ", validate_sequence(sequence))
    
    print("Length:", len(sequence))
    print("Base Counts:", count_bases(sequence))
    print("GC Content:", round(gc_content(sequence) * 100, 2), "%")
    print("Reverse Complement:", reverse_complement(sequence))

    # Biological conversion
    dna = Seq(sequence)
    print("DNA:", dna)
    rna = dna.transcribe()
    print("RNA:", rna)
    protein = rna.translate() #translate(to_stop = True) stops translation before the first stop codon
    print("Protein:", protein)

    # Visualization
    base_counts = count_bases(sequence)
    plot_base_counts(base_counts)

if __name__ == "__main__":
    main()