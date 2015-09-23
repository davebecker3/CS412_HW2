import csv
from datetime import datetime, date, time

print("    This is the output of file: \'CS412_HW02_03py\'.")


def read_print():
    with open('CoC_BWQ_2015_WT.csv', newline='') as f:
        reader = csv.reader(f)
        # input_list = [] #Putting this here is no good! Thx, Aziz!
        calumet = []
        print("    Here's the print output direct from the reader:")
        for stuff in reader:
            # input_list.append(stuff[0])
            if(stuff[0] == 'Calumet Beach'):
                in_lst = []
                # input_list.clear()
                in_lst.append(datetime.strptime(stuff[9], '%m/%d/%Y %H:%M %p'))
                in_lst.append(float(stuff[2]))
                calumet.append(in_lst)
                print(calumet)
        print("    The length of the list \"calumet\" is: ", len(calumet))
        print(in_lst)
        print("    The length of the input list is: ", len(in_lst))

        max_temp = 0.0
        max_temp_index = 0
        for stuff in calumet:
            if(stuff[1] > max_temp):
                max_temp = stuff[1]
                max_temp_index = calumet.index(stuff)
                print("    The max temp found so far is: ", max_temp)
        print("    The final max temp is: ", max_temp)
        print("    The index of the max temp is: ", max_temp_index)
        print("    The sub-list at that index is: ", calumet[max_temp_index])

        min_temp = 100.0
        min_temp_index = 0
        for stuff in calumet:
            if(stuff[1] < min_temp):
                min_temp = stuff[1]
                min_temp_index = calumet.index(stuff)
                print("    The min temp found so far is: ", min_temp)
        print("    The final min temp is: ", min_temp)
        print("    The index of the min temp is: ", min_temp_index)
        print("    The sub-list at that index is: ", calumet[min_temp_index])

if __name__ == "__main__":
    import sys
    read_print()
