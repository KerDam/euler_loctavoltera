from numpy import arange
import os

def rk(nameOfTheGraph, step, ite, expressionList, initialValuesDict):

    # this will open all the files
    files = []
    for x in range(len(expressionList)):
        files.append(open(".graph"+str(x)+".txt",'w'))

    for n in arange(0,ite * step,step):
        initialValuesDictCopy = initialValuesDict
        for expression in expressionList:

            #Write the data in the file
            files[expressionList.index(expression)].write(str(n) + '\t' + str(initialValuesDict[expression[1]]) + '\n')


            # for k1
            expressionCopy = expression[0]
            for i in initialValuesDict.keys():
                expressionCopy = expressionCopy.replace(i,str(initialValuesDictCopy[i]))
            k1 = eval(expressionCopy)

            #for k2
            expressionCopy = expression[0]
            expressionCopy = expressionCopy.replace(expression[1],str(k1 * step / 2.0 + initialValuesDict[expression[1]]))
            for i in initialValuesDict.keys():
                expressionCopy = expressionCopy.replace(i,str(initialValuesDict[i]))
            k2 = eval(expressionCopy)

            #for k3
            expressionCopy = expression[0]
            expressionCopy = expressionCopy.replace(expression[1],str(k2 * step / 2.0 + initialValuesDict[expression[1]]))
            for i in initialValuesDict.keys():
                expressionCopy = expressionCopy.replace(i,str(initialValuesDict[i]))
            k3 = eval(expressionCopy)

        #for k4
            expressionCopy = expression[0]
            expressionCopy = expressionCopy.replace(expression[1],str(k3 * step + initialValuesDict[expression[1]]))
            for i in initialValuesDict.keys():
                expressionCopy = expressionCopy.replace(i,str(initialValuesDict[i]))
            k4 =   eval(expressionCopy)

            initialValuesDict[expression[1]] = initialValuesDictCopy[expression[1]] +(((k2 + 2* k2 + 2* k3 + k4)/6) * step)

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
rk("Dynamique des populations",step, ite, expressionList, initialValuesDict)
