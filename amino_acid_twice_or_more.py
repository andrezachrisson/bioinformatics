def amino_acid_twice(column):
    dict = {}
    for i in column:
        if i != '-' and i not in dict:
            value = column.count(i)
            dict[i] = value
            if value > 2:
                return True
                break
    return False
