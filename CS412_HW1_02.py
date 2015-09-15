import csv


print("    This is the output of file: \'CS412_HW1.py\'.")


def read_print():
    with open('CoC_BWQ_2015_WT.csv', newline='') as f:
        reader = csv.reader(f)
        input_list = []
        print("    Here's the print output direct from the reader:")
        for stuff in reader:
            input_list.append(stuff[0])
            input_list.append(stuff[2])
            input_list.append(stuff[9])
            print("    The length of the input list is: ", len(input_list))
        print(input_list)

if __name__ == "__main__":
    import sys
    read_print()
