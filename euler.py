from numpy import arange
import os

def makeGraph(files):
    #This make a graph with the data wrote in the files using gnuplot
    command = "gnuplot -p -e \"set title \\\" \\\"; set terminal svg; set output \\\"output.svg\\\"; plot"
    for f in files:
        command = command + ' \\\".graph'+str(files.index(f))+".txt\\\","
    command = command[:len(command)-1] + "\""
    os.system(command)

def euler (step, ite, expressionList, initialValuesDict):

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
    return files

def rk(step, ite, expressionList, initialValuesDict):

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

    return files

def dynamic(a,b,c,d,x,y):
    a = "x*("+str(a)+"-"+str(b)+"*y)",'x'
    b = "-y*("+str(c)+"-"+str(d)+"*x)",'y'
    expressionList = [a,b]
    initialValuesDict = {'x':x, 'y':y}
    makeGraph(rk(0.1, 4000, expressionList, initialValuesDict))

# step = 0.1
# ite = 4000
# a = "x*(0.05 - 0.002*y)" , 'x'
# b = "-y*(0.06 - 0.004*x)", 'y'
# expressionList= [a,b]
# initialValuesDict = {'x':10, 'y':10}
# a = "2.0 * (x)",'x','carre'
# expressionList = [a]
# initialValuesDict = {'x':10, 'y':10}
# rk(step, ite, expressionList, initialValuesDict)
dynamic(0.05, 0.002, 0.06, 0.004, 10,10)
