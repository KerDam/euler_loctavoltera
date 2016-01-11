from numpy import arange
import os

def euler (nameOfTheGraph, step, ite, expressionList, initialValuesDict):

    # this will open all the files
    files = []
    for x in range(len(expressionList)):
        files.append(open(".graph"+str(x)+".txt",'w'))

    for n in arange(0,ite * step,step):
        initialValuesDictCopy = initialValuesDict
        for expression in expressionList:
            expressionCopy = expression[0];

            #Write the data in the file
            files[expressionList.index(expression)].write(str(n) + '\t' + str(initialValuesDict[expression[1]]) + '\n')

            # this part will valuate the expression and put the result in the
            #dictionnary

            for i in initialValuesDict.keys():
                expressionCopy = expressionCopy.replace(i,str(initialValuesDictCopy[i]))
            initialValuesDict[expression[1]] = initialValuesDict[expression[1]] +  step * eval(expressionCopy)

    # This will close all the files
    for f in files:
        f.close()

    #This make a graph with the data wrote in the files using gnuplot
    command = "gnuplot -p -e \"set title \\\""+nameOfTheGraph+"\\\"; plot"
    for expression in expressionList:
        command = command + ' \\\".graph'+str(expressionList.index(expression))+".txt\\\" title \\\""+expression[2]+"\\\","
    command = command[:len(command)-1] + "\""
    os.system(command)


step = 0.1
ite = 4000
a = "x*(0.05 - 0.002*y)" , 'x', 'proie'
b = "-y*(0.06 - 0.004*x)", 'y', 'predateur'
expressionList= [a,b]
initialValuesDict = {'x':10, 'y':10}
# a = "2.0 * (x)",'x','carre'
# expressionList = [a]
# initialValuesDict = {'x':10, 'y':10}
euler("Dynamique des populations",step, ite, expressionList, initialValuesDict)
