import pandas as pd
import numpy as numpy
import math
file1 = open("output.txt","w")

# problem1

df = pd.read_excel('owid-covid-data.xlsx',sheet_name='Sheet1', usecols="C")
countries = df.to_numpy() 
countries1 = numpy.unique(countries)  #aynı ülkeleri çıkardım
file1.write("1-How many countries the dataset has? :")
file1.write(str(countries1.size))

#problem2
file1.write("\n2-When is the earliest date data are taken for a country? Which country is it? : ")
df = pd.read_excel('owid-covid-data.xlsx',sheet_name='Sheet1', usecols="D")
data = df.to_numpy()
minElement = numpy.amin(data)
file1.write(str(minElement))
result = numpy.where(data == numpy.amin(data))
file1.write(str(countries[result]))

#problem3
file1.write("\n\n3-How many cases are confirmed for each country so far? Print pairwise results of country and total cases. : ")
df = pd.read_excel('owid-covid-data.xlsx',sheet_name='Sheet1', usecols="E")
cases = df.to_numpy()
uniqueValues,indicesList = numpy.unique(countries, return_index=True)
between = indicesList
indicesList = numpy.delete(indicesList, 0)
y = countries.size
indicesList = numpy.insert(indicesList, indicesList.size,y)
y = 0
tsum = 0
for x in range(indicesList.size):
    indicesList[x] = indicesList[x]-1
    y = indicesList[x]
for x in range(indicesList.size):
    y = indicesList[x]
    file1.write("\n {} Total Case:{} ".format( countries1[x],cases[y][0]))
#problem4
file1.write("\n\n4-How many deaths are confirmed for each country so far? Print pairwise results of country and total deaths:")
df = pd.read_excel('owid-covid-data.xlsx',sheet_name='Sheet1', usecols="H")
four = df.to_numpy()
uniqueValues,indicesList = numpy.unique(countries, return_index=True)
indicesList = numpy.delete(indicesList, 0)
y = countries.size
indicesList = numpy.insert(indicesList, indicesList.size,y)
y = 0
for x in range(indicesList.size):
    indicesList[x] = indicesList[x]-1
    y = indicesList[x]
    tsum = tsum + four[y]

for x in range(indicesList.size):
    y = indicesList[x]
    file1.write("\n {} Total Deaths:{}   ".format( countries1[x],four[y][0]))

#problem5
df = pd.read_excel('owid-covid-data.xlsx',sheet_name='Sheet1', usecols="Q")
reproduction = df.to_numpy()
file1.write("\n\n5-What are the average, minimum, maximum and variation values of the reproduction rates for each country?")
file1.write("\nCountry   minumum       maximum       average       variation\n")
arr = []
flag = 0

for x in range(countries1.size):
    temp1 = between[x]
    temp2 = indicesList[x]
    arr = []
    for i in range(temp1,temp2+1):
        if not math.isnan(reproduction[i]):
            arr = numpy.append (arr,reproduction[i])
    if not numpy.any(arr):
        file1.write("{}  none   none   none   none  none  \n".format(countries1[flag]))
    else:
        file1.write("{}  {}  {}  {}  {}  \n".format(countries1[flag],numpy.min(arr),numpy.max(arr),numpy.average(arr),numpy.var(arr)))
    flag+=1
#problem 6
df = pd.read_excel('owid-covid-data.xlsx',sheet_name='Sheet1', usecols="R")
icu_pat = df.to_numpy()
file1.write("\n\n6-What are the average, minimum, maximum and variation values of the icu patients (intensive care unit patients) for each country?")
file1.write("\nCountry   minumum       maximum       average       variation\n")
arr1 = []
flag = 0
for x in range(countries1.size):
    temp1 = between[x]
    temp2 = indicesList[x]
    arr1 = []
    for i in range(temp1,temp2+1):
        if not math.isnan(icu_pat[i]):
            arr1 = numpy.append (arr1,icu_pat[i])
    if not numpy.any(arr1):
        file1.write("{}  none   none   none   none  none  \n".format(countries1[flag]))
    else:
        file1.write("{}  {}  {}  {}  {}  \n".format(countries1[flag],numpy.min(arr1),numpy.max(arr1),numpy.average(arr1),numpy.var(arr1)))
    flag+=1
    #problem 7
df = pd.read_excel('owid-covid-data.xlsx',sheet_name='Sheet1', usecols="T")
icu_pat = df.to_numpy()
file1.write("\n\n7-What are the average, minimum, maximum and variation values of the hosp patients (hospital patients)for each country?")
file1.write("\nCountry   minumum       maximum       average       variation\n")
arr2 = []
flag = 0
for x in range(countries1.size):
    temp1 = between[x]
    temp2 = indicesList[x]
    arr2 = []
    for i in range(temp1,temp2+1):
        if not  math.isnan(icu_pat[i]):
            arr2 = numpy.append (arr2, icu_pat[i])
    if not numpy.any(arr2):
        file1.write("{}  none   none   none   none  none  \n".format(countries1[flag]))
    else:
        file1.write("{}  {}  {}  {}  {}  \n".format(countries1[flag],numpy.min(arr2),numpy.max(arr2),numpy.average(arr2),numpy.var(arr2)))
    flag+=1
#problem 8
df = pd.read_excel('owid-covid-data.xlsx',sheet_name='Sheet1', usecols="V")
icu_pat = df.to_numpy()
file1.write("\n\n8-What are the average, minimum, maximum and variation values of the weekly icu (intensive care unit) admissions for each country?")
file1.write("\nCountry   minumum       maximum       average       variation\n")
arr3 = []
flag = 0
for x in range(countries1.size):
    temp1 = between[x]
    temp2 = indicesList[x]
    arr3 = []
    for i in range(temp1,temp2+1):
        if not  math.isnan(icu_pat[i]):
            arr3 = numpy.append (arr3, icu_pat[i])
    if not numpy.any(arr3):
        file1.write("{}  none   none   none   none  none  \n".format(countries1[flag]))
    else:
        file1.write("{}  {}  {}  {}  {}  \n".format(countries1[flag],numpy.min(arr3),numpy.max(arr3),numpy.average(arr3),numpy.var(arr3)))
    flag+=1
#problem 9
df = pd.read_excel('owid-covid-data.xlsx',sheet_name='Sheet1', usecols="X")
icu_pat = df.to_numpy()
file1.write("\n\n9-What are the average, minimum, maximum and variation values of the weekly hospital admissions for each country?")
file1.write("\nCountry   minumum       maximum       average       variation\n")
arr4 = []
flag = 0
for x in range(countries1.size):
    temp1 = between[x]
    temp2 = indicesList[x]
    arr4 = []
    for i in range(temp1,temp2+1):
        if not  math.isnan(icu_pat[i]):
            arr4 = numpy.append (arr4, icu_pat[i])
    if not numpy.any(arr4):
        file1.write("{}  none   none   none   none  none  \n".format(countries1[flag]))
    else:
        file1.write("{}  {}  {}  {}  {}  \n".format(countries1[flag],numpy.min(arr4),numpy.max(arr4),numpy.average(arr4),numpy.var(arr4)))
    flag+=1
#problem 10
df = pd.read_excel('owid-covid-data.xlsx',sheet_name='Sheet1', usecols="Z")
icu_pat = df.to_numpy()
file1.write("\n\n10-What are the average, minimum, maximum and variation values of new tests per day for each country?")
file1.write("\nCountry   minumum       maximum       average       variation\n")
arr5 = []
flag = 0
for x in range(countries1.size):
    temp1 = between[x]
    temp2 = indicesList[x]
    arr5 = []
    for i in range(temp1,temp2+1):
        if not math.isnan(icu_pat[i]):
            arr5 = numpy.append (arr5, icu_pat[i])
    if not numpy.any(arr5):
        file1.write("{}  none   none   none   none  none  \n".format(countries1[flag]))
    else:
        file1.write("{}  {}  {}  {}  {}  \n".format(countries1[flag],numpy.min(arr5),numpy.max(arr5),numpy.average(arr5),numpy.var(arr5)))
    flag+=1
#problem 11
df = pd.read_excel('owid-covid-data.xlsx',sheet_name='Sheet1', usecols="AA")
icu_pat = df.to_numpy()
file1.write("\n\n11-How many tests are conducted in total for each country so far?\n")
arr6 = []
flag = 0
for x in range(countries1.size):
    temp1 = between[x]
    temp2 = indicesList[x]
    arr6 = []
    for i in range(temp1,temp2+1):
        if not math.isnan(icu_pat[i]):
            arr6 = numpy.append (arr6, icu_pat[i])
    if not numpy.any(arr6):
        file1.write("{}  none   none   none   none  none  \n".format(countries1[flag]))
    else:
        file1.write("{}  {}  {}  {}  {}  \n".format(countries1[flag],numpy.min(arr6),numpy.max(arr6),numpy.average(arr6),numpy.var(arr6)))
    flag+=1
#problem 12
df = pd.read_excel('owid-covid-data.xlsx',sheet_name='Sheet1', usecols="AF")
icu_pat = df.to_numpy()
file1.write("\n\n12-What are the average, minimum, maximum and variation values of the positive rates of the tests for each country?")
file1.write("\nCountry   minumum       maximum       average       variation\n")
arr7 = []
flag = 0
for x in range(countries1.size):
    temp1 = between[x]
    temp2 = indicesList[x]
    arr7 = []
    for i in range(temp1,temp2+1):
        if not math.isnan(icu_pat[i]):
            arr7 = numpy.append (arr7, icu_pat[i])
    if not numpy.any(arr7):
        file1.write("{}  none   none   none   none  none  \n".format(countries1[flag]))
    else:
        file1.write("{}  {}  {}  {}  {}  \n".format(countries1[flag],numpy.min(arr7),numpy.max(arr7),numpy.average(arr7),numpy.var(arr7)))
    flag+=1
#problem 13
df = pd.read_excel('owid-covid-data.xlsx',sheet_name='Sheet1', usecols="AG")
icu_pat = df.to_numpy()
file1.write("\n\n13-What are the average, minimum, maximum and variation values of the tests per case for each country?")
file1.write("\nCountry   minumum       maximum       average       variation\n")
arr8 = []
flag = 0
for x in range(countries1.size):
    temp1 = between[x]
    temp2 = indicesList[x]
    arr8 = []
    for i in range(temp1,temp2+1):
        if not math.isnan(icu_pat[i]):
            arr8 = numpy.append (arr8, icu_pat[i])
    if not numpy.any(arr8):
        file1.write("{}  none   none   none   none  none  \n".format(countries1[flag]))
    else:
        file1.write("{}  {}  {}  {}  {}  \n".format(countries1[flag],numpy.min(arr8),numpy.max(arr8),numpy.average(arr8),numpy.var(arr8)))
    flag+=1
#problem14
df = pd.read_excel('owid-covid-data.xlsx',sheet_name='Sheet1', usecols="AJ")
icu_pat = df.to_numpy()
file1.write("\n\n14-How many people are vaccinated by at least one dose in each country?\n")
arr9 = []
flag = 0
for x in range(countries1.size):
    temp1 = between[x]
    temp2 = indicesList[x]
    arr9 = []
    for i in range(temp1,temp2+1):
        if not math.isnan(icu_pat[i]):
            arr9 = numpy.append (arr9, icu_pat[i])
    if not numpy.any(arr9):
        file1.write("{}  none   \n".format(countries1[flag]))
    else:
        file1.write("{}          {}\n".format(countries1[flag], numpy.max(arr9)))
    flag+=1
#problem 15
df = pd.read_excel('owid-covid-data.xlsx',sheet_name='Sheet1', usecols="AK")
icu_pat = df.to_numpy()
file1.write("\n\n15-How many people are vaccinated fully in each country?\n")
arr10 = []
flag = 0
for x in range(countries1.size):
    temp1 = between[x]
    temp2 = indicesList[x]
    arr10 = []
    for i in range(temp1,temp2+1):
        if not math.isnan(icu_pat[i]):
            arr10 = numpy.append (arr10, icu_pat[i])
    if not numpy.any(arr10):
        file1.write("{}  none   \n".format(countries1[flag]))
    else:
        file1.write("{}          {}\n".format(countries1[flag], numpy.max(arr10)))
    flag+=1
#problem 16
df = pd.read_excel('owid-covid-data.xlsx',sheet_name='Sheet1', usecols="AI")
icu_pat = df.to_numpy()
file1.write("\n\n16-How many vaccinations are administered in each country so far?\n")
arr11 = []
flag = 0
for x in range(countries1.size):
    temp1 = between[x]
    temp2 = indicesList[x]
    arr11 = []
    for i in range(temp1,temp2+1):
        if not math.isnan(icu_pat[i]):
            arr11 = numpy.append (arr11, icu_pat[i])
    if  not numpy.any(arr11):
        file1.write("{}  none   \n".format(countries1[flag]))
    else:
        file1.write("{}          {}\n".format(countries1[flag], numpy.max(arr11)))
    flag+=1
#problem 17
file1.write("\n\n17-List information about population, median age, # of people aged 65 older, # of people aged 70 older, economic performance, death rates due to heart disease, diabetes prevalence, # of female smokers,of male smokers, handwashing facilities, hospital beds per thousand people, life expectancy and human development index.")
file1.write("\nCountry  ---Population--Median age---- aged 65 older----- aged 70 older---- economic performance---death rates due to heart disease---diabetes prevalence---female smokers---- male smokers--handwashing facilities--hospital beds per thousand people---- life expectancy and human development index  \n")
df = pd.read_excel('owid-covid-data.xlsx',sheet_name='Sheet1', usecols="AS")
population = df.to_numpy()
df = pd.read_excel('owid-covid-data.xlsx',sheet_name='Sheet1', usecols="AU")
medianage = df.to_numpy()
df = pd.read_excel('owid-covid-data.xlsx',sheet_name='Sheet1', usecols="AV")
age65 = df.to_numpy()
df = pd.read_excel('owid-covid-data.xlsx',sheet_name='Sheet1', usecols="AW")
age70 = df.to_numpy()
df = pd.read_excel('owid-covid-data.xlsx',sheet_name='Sheet1', usecols="AX")
economic = df.to_numpy()
df = pd.read_excel('owid-covid-data.xlsx',sheet_name='Sheet1', usecols="AZ")
deathheart = df.to_numpy()
df = pd.read_excel('owid-covid-data.xlsx',sheet_name='Sheet1', usecols="BA")
deathdiabet = df.to_numpy()
df = pd.read_excel('owid-covid-data.xlsx',sheet_name='Sheet1', usecols="BB")
femalesmoke = df.to_numpy()
df = pd.read_excel('owid-covid-data.xlsx',sheet_name='Sheet1', usecols="BD")
malesmoke = df.to_numpy()
df = pd.read_excel('owid-covid-data.xlsx',sheet_name='Sheet1', usecols="BE")
hand = df.to_numpy()
df = pd.read_excel('owid-covid-data.xlsx',sheet_name='Sheet1', usecols="BF")
hosp = df.to_numpy()
df = pd.read_excel('owid-covid-data.xlsx',sheet_name='Sheet1', usecols="BG")
human = df.to_numpy()
arr12 = []
flag = 0
for x in range(countries1.size):
    temp1 = between[x]
    temp2 = indicesList[x]
    file1.write("{}-- {}-- {}--{}-- {}-- {} -- {}--  {} -- {}--{}--{}--{}-- {}\n".format(countries1[flag],medianage[temp1][0],population[temp1][0],age65[temp1][0],age70[temp1][0],economic[temp1][0],deathheart[temp1][0],deathdiabet[temp1][0],femalesmoke[temp1][0],malesmoke[temp1][0],hand[temp1][0],hosp[temp1][0],human[temp1][0]))
    flag+=1
#problem18
flag = 0
#file1.write("\n\n18-Country      q#3     q#4    q#5_min    q#5_max    q#5_avg    q#5_var   q#6_min    q#6_max    q#6_avg    q#6_var    q#7_min    q#7_max    q#7_avg    q#7_var   q#8_min    q#8_max    q#8_avg    q#8_var  q#9_min    q#9_max    q#9_avg    q#9_var  q#10_min    q#10_max    q#105_avg    q#10_var  ---  q#11_min    q#11_max    q#11_avg    q#11_var  q#12_min    q#12_max    q#12_avg    q#12_var  q#13_min    q#13_max    q#13_avg    q#13_var  q#14_min    q#14_max     q#15_max      q#16_max\n")
#for x in range(countries1.size):
 #   temp1 = between[x]
  #  temp2 = indicesList[x]
   # y = indicesList[x]
    #file1.write("{}  {}  {} {}  {}  {}  {} {}  {}  {}  {} \n".format(countries1[flag],cases[y][0],four[y][0],numpy.min(arr),numpy.max(arr),numpy.average(arr),numpy.var(arr),numpy.min(arr2),numpy.max(arr2),numpy.average(arr2),numpy.var(arr2)))
    #flag +=1    
