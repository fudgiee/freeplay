# pulls from the table on the bottom of https://www.hgvs.org/mutnomen/codon.html
# usage: copy/paste directly from table for correct three letter input

print(f'Paste string: ')
raw_codons = input()
print(raw_codons)

codons_list = raw_codons.split(", ")

quoted_codons = [f'{seq}' for seq in codons_list]

print(quoted_codons)

for codon in quoted_codons:
    print(codon)