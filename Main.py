from Bio import SeqIO
import pdb



MSL_list = []
for record in SeqIO.parse("s001.align.1.msl", "fasta"):
    tmp_list = []
    for letter in record.seq:
        tmp_list.append(letter)
    MSL_list.append(tmp_list.copy())
