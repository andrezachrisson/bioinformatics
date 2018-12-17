













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
