from Bio import SeqIO
from Bio.Seq import Seq
from noise_test import *
import pdb

def read_file(file_name):
    MSA_list = []
    reduced_file='reduced_file'
    with open(file_name) as reference, open(reduced_file,'w') as reduced:
        records = SeqIO.parse(file_name, 'fasta')
        for record in records:
            tmp_list = []
            for letter in record.seq:
                tmp_list.append(letter)
            MSA_list.append(tmp_list.copy())
        remove_index = check_all_columns(MSA_list)
        new_list = clean(remove_index, MSA_list)
        records = SeqIO.parse(file_name, 'fasta')
        for idx, record in enumerate(records):
            record.seq = Seq("".join(new_list[idx]))
            SeqIO.write(record, reduced, 'fasta')

def check_all_columns(MSA_list):
    remove_index = []
    for column in range(0,len(MSA_list[0])):
        tmp_col = []
        for row in MSA_list:
            tmp_col.append(row[column])
        if not noise_checker(tmp_col):
            remove_index.append(column)

    return remove_index

def noise_checker(column):
    if indel_counter(column) and uniq(column) and amino_acid_twice(column):
        return True
    else:
        return False

def clean(remove_index, MSA_list):
    for index in reversed(remove_index):
        for row in MSA_list:
            row.pop(index)
    return MSA_list






read_file('s001.align.1.msl')
