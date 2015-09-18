import csv


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
                input_list = []
                # input_list.clear()
                input_list.append(stuff[9])
                input_list.append(float(stuff[2]))
                calumet.append(input_list)
                print(calumet)
        print("    The length of the list \"calumet\" is: ", len(calumet))
        print(input_list)
        print("    The length of the input list is: ", len(input_list))


if __name__ == "__main__":
    import sys
    read_print()
