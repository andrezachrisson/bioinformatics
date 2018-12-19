import csv
import matplotlib.pyplot as plt
import re

with open('test.csv', 'r') as data:
        reader = csv.reader(data)
        all_data = list(reader)

        int_data = []
        prev_indx = 0

        all_idx = []
        sum_data = []
        avg_data = []
        max_data = []
        min_data = []
        diff_data = []
        order=[]
        for idx, row in enumerate(all_data):
            if re.search(r'tree', row[0]):
                all_idx.append(idx)
                order.append(all_data[idx][0])

        all_idx.append(len(all_data))
        for idx in range(0,len(all_idx)-1):
            temp_lst = []
            for row in all_data[all_idx[idx]+1:all_idx[idx+1]]:
                temp_lst.append((list(map(int,row))))

            avg_data.append([x/len(temp_lst) for x in list(map(sum, zip(*temp_lst)))])
            max_data.append([max(temp_lst,key=lambda item:item[1])[1], max(temp_lst,key=lambda item:item[0])[0]])
            min_data.append([min(temp_lst,key=lambda item:item[1])[1], min(temp_lst,key=lambda item:item[0])[0]])
            diff_data.append([abs(tup[0]-tup[1]) for tup in temp_lst])
        print(order)
        print(' ')
        print('Average (Normal), Average (reduced)')
        print(avg_data)
        print(' ')
        print('Max (Normal), Max (reduced)')
        print(max_data)
        print('')
        print('Min (Normal), Min (reduced)')
        print(min_data)

        hist1 = plt.figure()
        asym = diff_data[0]+diff_data[1]+diff_data[2]
        plt.hist(asym ,histtype = 'bar')
        hist2 = plt.figure()
        sym = diff_data[3]+diff_data[4] +diff_data[5]
        plt.hist(sym,histtype = 'bar')
        hist1.savefig('asymmetric_comparison',bbox_inches='tight')
        hist2.savefig('symmetric_comparison',bbox_inches='tight')
