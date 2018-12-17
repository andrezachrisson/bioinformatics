# This file takes a column, count the number of indels and
# divide the number of indels by the columns lenght. If this
# value is less than 0.5, keep the column (True). Otherwise
# dissmiss the column (False)
def indel_counter(column):
    indels = column.count('-')
    column_length = len(column)
    value = indels/column_length
    if value < 0.5:
        return True
    else:
        return False
