import os

#Creating a list of random integers
List1 = [8, 9, 4, 3, 8, 1, 13]
List1.reverse()
print("The reverse list is ", List1)
#Creating a list of random integers
#plus sorting the seceond list
List2 = [21, 434, 34, 64, 67, 78, 655, 23, 43, 333, 555, 777]
List2.sort()
print("The sorted list is ", List2)
#Creating a list of random integers
#then copying the first list to the third list

List3 = []
List3 = List1.copy()
print("List3", List3)


indexvalue = List2[2:6]
print("The Index values are ", indexvalue)