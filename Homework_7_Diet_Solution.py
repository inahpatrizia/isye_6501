import pulp
from pulp import *
import pandas as pd
food=pd.read_excel('C:\Users\salra\Projects\ISY 6051\diet.xls')
food=food[0:64] #grab only the food data
food=food.values.tolist() #convert into list
print(food)
label=[x[0] for x in food] #save the food names that are in the A column of the excel sheet

#create a dictionary for the cost of the foods, calories and nutrition
cost=dict([(x[0], float(x[1])) for x in food])
cal=dict([(x[0], float(x[3])) for x in food])
cholestrol=dict([(x[0], float(x[4])) for x in food])
fat=dict([(x[0], float(x[5])) for x in food])
sodium=dict([(x[0], float(x[6])) for x in food])
carbs=dict([(x[0], float(x[7])) for x in food])
fiber=dict([(x[0], float(x[8])) for x in food])
protein=dict([(x[0], float(x[9])) for x in food])
vitA=dict([(x[0], float(x[10])) for x in food])
vitC=dict([(x[0], float(x[11])) for x in food])
Ca=dict([(x[0], float(x[12])) for x in food])
Fe=dict([(x[0], float(x[13])) for x in food])

ref=[cal,
cholestrol,
fat,
sodium,
carbs,
fiber,
protein,
vitA,
vitC,
Ca,
Fe]
refname=['cals',
'cholestrol',
'fat',
'sodium',
'carbs',
'fiber',
'protein',
'vitA',
'vitC',
'Ca',
'Fe']

minDic=[1500,
30,
20,
800,
130,
125,
60,
1000,
400,
700,
10
]
maxDic=[2500,
240,
70,
2000,
450,
250,
100,
10000,
5000,
1500,
40
]

problem=LpProblem("Best Problem", LpMinimize)
amountVars=LpVariable.dicts("Amounts", label, 0) #define our primary variables

problem +=lpSum([cost[i]* amountVars[i] for i in label]), 'total cost'

for v in range(len(ref)):
    problem +=lpSum([ref[v][i]*amountVars[i] for i in label]) >= minDic[v], str('min'+' '+refname[v])
    problem +=lpSum([ref[v][i]*amountVars[i] for i in label]) <= maxDic[v], str('max'+' '+refname[v])
problem.solve()
print("Status:", LpStatus[prob.status])


# vardic={}
# for v in problem.variables():
#     vardic[v.name]=v.varValue
# print("Total Cost of Diet = ", value(problem.objective))
# #Total Cost of Diet =  4.337116797399999
#
# def filterTheDict(dictObj, callback):
#     """Obtained from thispointer.com"""
#     newDict = dict()
#     # Iterate over all the items in dictionary
#     for (key, value) in dictObj.items():
#         # Check if item satisfies the given condition then add to new dict
#         if callback((key, value)):
#             newDict[key] = value
#     return newDict
# #return non zero foods
#
# newdict=filterTheDict(vardic, lambda i: i[1]!=0)
# print('The optimal solution is:', newdict)
#
# #The optimal solution is: {'Amounts_Celery,_Raw': 52.64371, 'Amounts_Frozen_Broccoli': 0.25960653, 'Amounts_Lettuce,Iceberg,Raw': 63.988506, 'Amounts_Oranges': 2.2929389,
# #'Amounts_Poached_Eggs': 0.14184397, 'Amounts_Popcorn,Air_Popped': 13.869322}
#
#
# ##Question 2
# problem2=LpProblem("Best Problem", LpMinimize)
# amountVars=LpVariable.dicts("Amounts", label, 0) #define our primary variables
#
# problem2 +=lpSum([cost[i]* amountVars[i] for i in label]), 'total cost'
#
# for v in range(len(ref)):
#     problem2 +=lpSum([ref[v][i]*amountVars[i] for i in label]) >= minDic[v], str('min'+' '+refname[v])
#     problem2 +=lpSum([ref[v][i]*amountVars[i] for i in label]) <= maxDic[v], str('max'+' '+refname[v])
# binary=LpVariable.dicts("InOrOut", label, 0,1, LpBinary) #if food is selected
# for f in label:
#     problem2 += amountVars[f]>= binary[f]*0.1
#     problem2 += amountVars[f]<= binary[f]*1e5
#
#
# problem2 += binary['Frozen Broccoli']+binary['Raw Iceberg Lettuce']<=1  #celery or broccoli
#
# #set up categories for each type
# meat=['Frankfurter, Beef','Ham,Sliced,Extralean','Kielbasa,Prk','Hamburger W/Toppings','Hotdog, Plain','Pork']
# poultry=['Roasted Chicken','Bologna,TurAmounts_Pretkey']
# fish=['Sardines in Oil','White Tuna in Water']
# eggs=['Poached Eggs', 'Scrambled Eggs']
# meat_binary=LpVariable.dicts("InOrOut", meat, 0,1, LpBinary) #if meat is selected
# poultry_binary=LpVariable.dicts("InOrOut", poultry, 0,1, LpBinary)
# fish_binary=LpVariable.dicts("InOrOut", fish, 0,1, LpBinary)
# eggs_binary=LpVariable.dicts("InOrOut", eggs, 0,1, LpBinary)
#
# #if the food is selected and it is meat/fish/poultry then it needs to be at least 3 of such groups
# for f in label:
#
#     problem2 += amountVars[f]*meat_binary[f]+amountVars[f]*poultry_binary[f]+amountVars[f]*fish_binary[f]+amountVars[f]*eggs_binary[f]>=3
#
# problem2.solve()
#
# vardic2={}
# for v in problem2.variables():
#     vardic2[v.name]=v.varValue
#
#
# print("Total Cost of Diet = ", value(problem2.objective))
# newdict2=filterTheDict(vardic2, lambda i: i[1]!=0)
# print('The optimal solution is:', newdict2)