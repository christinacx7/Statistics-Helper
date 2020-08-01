import math

#Statistics helper will be able to solve statistics problems

print("\nStatistics Helper!")

#ask the user what equation they are trying to solve
print("What kind of equation are you trying to solve?")
print("1. Chebyshev's inequality equation\n2. IQR with given Q's")
print("***Enter only the number of your choice***")
choice = input()

#use if statements to determine which type of equation needs to be solved
if(choice is 1):
    #ask the user for the mean
    print("\nEnter the mean")
    mean = float(input())

    #ask the user for the standard deviation
    print("Enter the standard deviation")
    standardDeviation = float(input())

    #ask the user for the k value
    print("Enter the K value")
    k = int(input())

    #calculate the percentage
    percent = "{:.0%}".format(1 - (1/(math.pow(k,2))))

    #calculate the lower bound
    lowerBound = mean - (k * standardDeviation)

    #calculate the upper bound
    upperBound = mean + (k * standardDeviation)

    #print percent, lowerbound, and upperbound values
    print("\nThe percentage is ", percent)
    print("The lower bound is ", lowerBound)
    print("The upper bound is ", upperBound)