#!/usr/bin/python3

import math

#  Statistics helper will be able to solve statistics problems by
#calculating the problems for the user

print("\nStatistics Helper!")

#ask the user what equation they are trying to solve
print("What kind of equation are you trying to solve?")
print("1. Chebyshev's inequality equation")
print("2. IQR with given Q's")
print("3. Find P(A or B) using P(A), P(B), and P(A and B)")
print("***Enter only the number of your choice***")
choice = input()

#use if statements to determine which type of equation needs to be solved
#Chebyshev's inequality equation
if choice is 1:
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
    print("\nThe percentage is " + str(percent))
    print("The lower bound is " + str(lowerBound))
    print("The upper bound is " + str(upperBound))

#Find P(A or B)
if choice is 3:
    #ask for the values of P(A) and P(B)
    a = float(input("Enter the value of A\n"))
    b = float(input("Enter the value of B\n"))
    
    #ask the user if P(A and B) is mutually exclusive
    exclusive = input("Is P(A and B) mutually exclusive?\n")
    #if P(A and B) is mutually exlusive add the values of P(A) and P(B)
    if exclusive == 'yes':
        aOb = a + b
    #if P(A and B) is not mutually exlusive, ask the user for the value of P(A and B)
    #and add P(A) and P(B) and subtract P(A and B)
    elif exclusive == 'no':
        print("Enter P(A and B)")
        aNb = float(input())
        aOb = a + b - aNb
    #print the value of P(A orB)
    print("P(A or B) is equal to " + str(aOb))
