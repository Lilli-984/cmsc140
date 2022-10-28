import random 
import matplotlib.pyplot as plt

def generate_dna(tablenum):

    random.seed(tablenum)

    dna = ['A','C','G','T']

    seq = "".join(random.choices(dna, k=300))

    # replace start with a start codon
    seq = "TAC" + seq[3:]

    # replace any premature stop codons with non-stops
    seq = seq.replace("ATT", "CGG")
    seq = seq.replace("ATC", "GGC")
    seq = seq.replace("ACT", "GCG")

    # Add in a stop codon somewhere towards the end
    stops = ["ATT", "ATC", "ACT"]
    rand_end = 3 * (random.randint(250,300)//3)
    seq = seq[0:rand_end] + random.choice(stops) + seq[rand_end+3:]

    return seq

rna = ""

dna_to_rna = {
    "A": "U",
    "T": "A",
    "C": "G",
    "G": "C"
}
dna = generate_dna(1)
for letter in dna:
    rna += dna_to_rna[letter]

print (rna)
print("")


aa = {
    "UUU": "Phe", "UUC": "Phe", "UUA": "Leu", "UUG": "Leu",
    "UCU": "Ser", "UCC": "Ser", "UCA": "Ser", "UCG": "Ser",
    "UAU": "Tyr", "UAC": "Tyr", "UAA": "STOP", "UAG": "STOP",
    "UGU": "Cys", "UGC": "Cys", "UGA": "STOP", "UGG": "Trp",
    "CUU": "Leu", "CUC": "Leu", "CUA": "Leu", "CUG": "Leu",
    "CCU": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",
    "CAU": "His", "CAC": "His", "CAA": "Gln", "CAG": "Gln",
    "CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg",
    "AUU": "Ile", "AUC": "Ile", "AUA": "Ile", "AUG": "Met",
    "ACU": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",
    "AAU": "Asn", "AAC": "Asn", "AAA": "Lys", "AAG": "Lys",
    "AGU": "Ser", "AGC": "Ser", "AGA": "Arg", "AGG": "Arg",
    "GUU": "Val", "GUC": "Val", "GUA": "Val", "GUG": "Val",
    "GCU": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",
    "GAU": "Asp", "GAC": "Asp", "GAA": "Glu", "GAG": "Glu",
    "GGU": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly"
}

amino_acids = []
for i in range(0,len(rna),3):
    nucleic_acids = rna[i:i+3]
    if aa[nucleic_acids] == 'STOP':
        break
    amino_acids.append(str(aa[nucleic_acids]))

print (amino_acids)

amino_string = "-".join(amino_acids)
print (amino_string)

plt.hist(amino_acids, bins = len(set(amino_acids)))
plt.show()