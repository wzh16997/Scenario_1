import csv

# available letter: A B C D     available logic operation number: 10
Range = ['A','B','C','D','0','1','2','3','4','5','6','7','8','9']

#         operate sequence,   type of operation,  left sub-operation/letter,  right sub-operation/letter
fields = ['Order_operation', 'Type', 'brackets', 'left', 'right'] 
order = 0
rows = []

# test formula 
formula = "!A&(B|C)&D"         


# operating order: !A&(B|C)&D
# 0: !A is stored,  current formula: 0&(B|C)&D
# 1: (B|C) is stored, current formula: 0&1&D
# 2: 0&1 is stored, current formula: 2&D
# 3: 2&D is stored, current formula: 3
# 4: end 
while not formula == str(order-1):
        i = 0
        while True:
                if i >= len(formula):
                    break
                if formula[i] == '!':
                    has_brackets = False
                    if formula[i+1] in Range:
                        if formula[i-1] == "(" and formula[i+2] == ")":
                            has_brackets = True
                        rows.append([order,formula[i],has_brackets,"#",formula[i+1]])
                        if has_brackets:
                            formula = formula.replace(formula[i-1:i+3],str(order))
                        else:
                            formula = formula.replace(formula[i:i+2],str(order))
                        order += 1
                elif formula[i] == '&':
                    has_brackets = False
                    if formula[i-1] in Range and formula[i+1] in Range:
                        if formula[i-2] == "(" and formula[i+2] == ")":
                            has_brackets = True
                        rows.append([order,formula[i],has_brackets,formula[i-1],formula[i+1]])
                        if has_brackets:
                            formula = formula.replace(formula[i-2:i+3],str(order))
                        else:
                            formula = formula.replace(formula[i-1:i+2],str(order))
                        order += 1
                        i -= 1
                elif formula[i] == '|':
                    has_brackets = False
                    if formula[i-1] in Range and formula[i+1] in Range:
                        if i-2 >= 0 and (formula[i-2] == '!' or formula[i-2] == '&') or i+2 < len(formula) and (formula[i+2] == '!' or formula[i+2] == '&'):
                            pass
                        else:
                            if formula[i-2] == "(" and formula[i+2] == ")":
                                has_brackets = True
                            rows.append([order,formula[i],has_brackets,formula[i-1],formula[i+1]])
                            if has_brackets:
                                formula = formula.replace(formula[i-2:i+3],str(order))
                            else:
                                formula = formula.replace(formula[i-1:i+2],str(order))
                            order += 1
                            i -= 1
                i += 1
filename = "formula.csv"
    
with open(filename, 'w', newline='') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(fields) 
    csvwriter.writerows(rows)

