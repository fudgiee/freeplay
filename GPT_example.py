# EXAMPLE ONE
class AminoAcid:
    def __init__(self, name, symbol, codons, size=None, polarity=None, acidity=None, hydrophobic=None):
        self.name = name
        self.symbol = symbol
        self.codons = codons
        self.size = size
        self.polarity = polarity
        self.acidity = acidity
        self.hydrophobic = hydrophobic

    def matches_codon(self, codon):
        return codon in self.codons

# Dynamically create arginine or any amino acid
def arginine():
    return AminoAcid(
        name="Arginine",
        symbol="R",
        codons=["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"],
        size="large",
        polarity=True,
        acidity=False,
        hydrophobic=False,
    )

# Example usage
arg = arginine()
print(f"Amino Acid: {arg.name}, Symbol: {arg.symbol}, Codons: {arg.codons}")
print(arg.matches_codon("CGU"))  # True
print(arg.matches_codon("XYZ"))  # False


# EXAMPLE 2
class AminoAcids:
    # Maps amino acids to single-letter codes
    aa_dict = {
        "Alanine": "A", "Arginine": "R", "Asparagine": "N", "Aspartic Acid": "D",
        "Cysteine": "C", "Glutamic Acid": "E", "Glutamine": "Q", "Glycine": "G",
        "Histidine": "H", "Isoleucine": "I", "Leucine": "L", "Lysine": "K",
        "Methionine": "M", "Phenylalanine": "F", "Proline": "P", "Serine": "S",
        "Threonine": "T", "Tyrosine": "Y", "Tryptophan": "W", "Valine": "V"
    }

    # Maps codons to amino acids
    codon_table = {
        "GCU": "Alanine", "GCC": "Alanine", "GCA": "Alanine", "GCG": "Alanine",
        "CGU": "Arginine", "CGC": "Arginine", "CGA": "Arginine", "CGG": "Arginine",
        "AGA": "Arginine", "AGG": "Arginine",
        "UUU": "Phenylalanine", "UUC": "Phenylalanine",
        "AUG": "Methionine",
        "UAA": "Stop", "UAG": "Stop", "UGA": "Stop",
        # Add other codon mappings as needed
    }

    @classmethod
    def get_amino_acid(cls, codon):
        return cls.codon_table.get(codon, "Unknown")  # Fetch amino acid or "Unknown"


# Function to transcribe DNA into RNA
def transcription():
    print("Enter your DNA sequence below:")
    DNA_seq = input().upper()  # Ensure the input is in uppercase
    RNA_seq = []  # Initialize an empty list for the RNA sequence

    # Convert DNA to RNA
    for letter in DNA_seq:
        if letter == "A":
            RNA_seq.append("U")
        elif letter == "T":
            RNA_seq.append("A")
        elif letter == "C":
            RNA_seq.append("G")
        elif letter == "G":
            RNA_seq.append("C")
        else:
            print(f"Invalid nucleotide '{letter}' in DNA sequence. Skipping.")

    RNA_seq = ''.join(RNA_seq)  # Convert the list to a string
    print("Transcribed RNA sequence:", RNA_seq)
    return RNA_seq


# Function to translate RNA into amino acids
def translation(RNA_seq):
    # Split RNA sequence into codons (chunks of 3)
    codon_list = [RNA_seq[i:i + 3] for i in range(0, len(RNA_seq), 3) if len(RNA_seq[i:i + 3]) == 3]

    # Map codons to amino acids using the AminoAcids class
    amino_acid_list = [AminoAcids.get_amino_acid(codon) for codon in codon_list]

    print("Codon list:", codon_list)
    print("Amino acid list:", amino_acid_list)
    return amino_acid_list


# Main Program
RNA_seq = transcription()  # Get the RNA sequence from transcription
amino_acids = translation(RNA_seq)  # Translate RNA into amino acids
