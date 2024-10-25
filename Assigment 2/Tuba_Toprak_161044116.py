import pandas as pd
import numpy as numpy
import math
import matplotlib.pyplot as plt
table = pd.read_csv('manufacturing_defects.txt', sep="\t", header=None)  #read to file 
manufacturing = len(table.loc[0])-2   # find manifacturing size
time = len( numpy.array(table[1]))           #  find time      
numberOfCases = 5    # cases = 0,1,2,3,4
actual_case = []   # to record actual cases
occurrences = 0
case = 0
all = 0
pre_case = []  ## to record pre cases

for x in range(numberOfCases):
    for y in range(2,manufacturing+2):    #to calculate the cases given in the range
        occurrences += numpy.count_nonzero(table[y] == x)   #to calculate how many cases there are    
    actual_case.append(occurrences) # for barplot record
    all += occurrences   # to calculate lambda
    case += x*occurrences  # to calculate predicate cases
    occurrences = 0  #reset 

print("# of Defects ------ # of cases in all company between the years")
for x in range(numberOfCases):
    print("      ",x,"            ",end =" ")
    print("            ",actual_case[x],"                                 ")  #To print the number of cases

lamb = (case/all)            #to calculate lambda
print("Lambda: ",lamb)

print("# of Defects ------ # of cases in all company between the years ------ Predicted \#of cases in all company betweeen the years")
for x in range(numberOfCases):
    print("      ",x,"            ",end =" ")
    print("            ",actual_case[x],"                                 ",end =" ")
    pre_case.append(((pow(lamb,x) * math.exp(-lamb)) / (math.factorial(int(x))))*all)  # to calculate  predicate cases 
    print(pre_case[x])

X_axis = numpy.arange(numberOfCases)   # creating the bar plot 
plt.bar(X_axis - 0.2, actual_case, 0.4, label = 'Actual Cases',color = "#9B59B6") # to set actual case bar plot 
plt.bar(X_axis + 0.2, pre_case, 0.4, label = 'Predicted Cases',color = "#2C3E50")  # to set predicate case bar plot 
plt.title("Real - Calculated Cases Table")  # bar plot title
plt.legend()  
plt.show()


