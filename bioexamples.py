class DNA:
    dna_dict = { "Adenine": "A", "Guanine": "G", "Cytosine": "C", "Thymine": "T"}
    dna_codon = ['A', 'G', 'C', 'T']

class RNA:
    rna_dict = {"Adenine": "A", "Guanine": "G", "Cytosine": "C", "Uracil": "U"}
    rna_codon = ['A', 'G', 'C', 'U']


class AminoAcids:
    aa_dict = {"Alanine": "A", "Arginine": "R", "Asparagine": "N", "Aspartic Acid": "D",
               "Cysteine": "C", "Glutamic Acid": "E", "Glutamine": "Q", "Glycine": "G", "Histidine": "H",
               "Isoleucine": "I", "Leucine": "L", "Lysine": "K", "Methionine": "M", "Phenylalanine": "F",
               "Proline": "P", "Serine": "S", "Threonine": "W", "Tyrosine": "Y", "Tryptophan": "W",
               "Valine": "V"}
    aa_codon = ['A', 'R', 'N', 'D', 'C', 'E', 'Q', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'W', 'Y', 'W', 'V']

    def arginine(self, size, polarity, symbol, codons, acidity, hydrophobic, ):
        acidity = False
        charged = False
        polarity = True
        hydrophobic = False
        codons = ['GCA', 'GCC', 'GCG', 'GCT']
        symbol = "A"

    def alanine(self, polarity, symbol, codons, acidity, hydrophobic, aliphatic):
        acidity = False
        charged = False
        polarity = True
        hydrophobic = False
        codons = ['GCA', 'GCC', 'GCG', 'GCT']
        symbol = "A"



