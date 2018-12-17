from Bio import SeqIO
import pdb

def read_file(file_name):
    MSA_list = []
    for record in SeqIO.parse(file_name, "fasta"):
        tmp_list = []
        for letter in record.seq:
            tmp_list.append(letter)
        MSA_list.append(tmp_list.copy())
    return MSA_list.copy()

    
def uniq(column):
    dict = {}
    count = 0
    for amino in column:
        if amino != "-" and amino not in dict:
            count +=1
            dict[amino] = count
    column.remove("-")
    if count/len(column) > 0.5:
        return True
    else:
        return False


def noise_checker(column):
    value = uniq(column)
    if value == True:
        print("true")
    else:
        print("false")

    return None

test = ["-", "b", "c", "c"]
noise_checker(test)
