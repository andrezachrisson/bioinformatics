from Bio import SeqIO
import pdb


def read_file(file_name)
MSL_list = []
for record in SeqIO.parse(file_name, "fasta"):
    tmp_list = []
    for letter in record.seq:
        tmp_list.append(letter)
    MSL_list.append(tmp_list.copy())
return MSL_list.copy()

def uniq(column):
    dict = {}
    count = 0
    for amino in column:
        if amino != "-":
            count =+1
            print(count)
            dict[amino] = count
            print(amino)
    return True


def noise_checker(column):
    value = uniq(column)

    if value == True:
        print("true")
    else:
        print("false")

    return None

test = ["-", "b", "c", "c"]
noise_checker(test)
