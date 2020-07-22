from Bio import SeqIO

record = SeqIO.read("061.fastq", "fasta")

A = record.seq.count("A")
C = record.seq.count("C")
T = record.seq.count("T")
G = record.seq.count("G")

print(f"A: {A}") # A: 497
print(f"C: {C}") # C: 444
print(f"A: {G}") # A: 585
print(f"A: {T}") # A: 514





