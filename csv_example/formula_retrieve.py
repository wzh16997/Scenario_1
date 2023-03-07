import csv

# available letter
Letter = ['A','B','C','D']

# get the last operated logic operation order:
# in    !A&(B|C)&D     the last order is 3 for 2&D 
with open('formula.csv', mode ='r') as file:   
        csvFile = csv.DictReader(file)
        for lines in csvFile:
            last = lines['Order_operation']
# targeted csv file:
# Order_operation  Type  brackets  left  right
# 0                !      False      #     A
# 1                |      True       B     C
# 2                &      False      0     1
# 3                &      False      2     D
#---------------------------------------------
# retrieval operation: order = 3
#             2     &     D
#            /|\           
#             |
#       0     &     1
#      /|\         /|\
#       |           |
#      !A         (B|C)
def print_formula(order):
    with open('formula.csv', mode ='r') as file:   
        csvFile = csv.DictReader(file)
        for lines in csvFile:
            if order == lines['Order_operation']:
                if lines['left'] in Letter:
                    part = lines['left']
                elif lines['left'] == '#':
                    part = ""
                else:
                    part = print_formula(lines['left'])
                part += lines['Type']
                if lines['right'] in Letter:
                    part += lines['right']
                else:
                    part += print_formula(lines['right'])
                if lines['brackets'] == "True":
                    part = "("+part+")"
                return part
                       
print(print_formula(last))