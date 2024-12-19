# accept DNA sequence as input - return list of RNA sequence

def transcription():
    print("Enter your DNA sequence below:")
    DNA_seq = input()
    RNA_seq = []

    for letter in DNA_seq:
        if letter == "A":
            RNA_seq.append("U")
        else:
            RNA_seq.append(letter)

    RNA_seq = ''.join(RNA_seq)
    print(RNA_seq)
    return RNA_seq

def translation(RNA_seq):
    # Group RNA sequence into codons
    codon_list = [RNA_seq[i:i+3] for i in range(0, len(RNA_seq), 3)]

    print("Codon list:", codon_list)
    return codon_list


RNA_seq = transcription()
codon_list = translation(RNA_seq)
