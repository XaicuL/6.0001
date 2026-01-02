# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 12:13:13 2016

@author: ericgrimson
"""

#
# def bisect_search2(L, e):
#     def bisect_search_helper(L, e, low, high):
#         print('low: ' + str(low) + '; high: ' + str(high))  # added to visualize
#         if high == low:
#             return L[low] == e
#         mid = (low + high) // 2
#         if L[mid] == e:
#             return True
#         elif L[mid] > e:
#             if low == mid:  # nothing left to search
#                 return False
#             else:
#                 return bisect_search_helper(L, e, low, mid - 1)
#         else:
#             return bisect_search_helper(L, e, mid + 1, high)
#
#     if len(L) == 0:
#         return False
#     else:
#         return bisect_search_helper(L, e, 0, len(L) - 1)
#
#
#
# testList = [3,2,5,2,1,24,4,22,13]
# testList.sort()
#
# print("Sorted list:", testList)
#
# testList.append(0)
# testList.sort()
#
# print("After append and sort:", testList)
#
#
# print("\nBinary search for 13:")  #True
# print(bisect_search2(testList, 13))
#
# print("\nBinary search for 99 (not in list):") #False
# print(bisect_search2(testList, 99))

#
# def genSubsets(L): #find All subsets of L
#     res = []
#     if len(L) == 0:
#         return [[]]  # list of empty list
#     smaller = genSubsets(L[:-1])  # all subsets without last element
#     extra = L[-1:]  # create a list of just last element
#     new = []
#     for small in smaller:
#         new.append(small + extra)  # for all smaller solutions, add one with last element
#     return smaller + new  # combine those with last element and those without
#
#
# testSet = [1,2,3]
# print(genSubsets(testSet))
#
#

class Toy(object):
    def __init__(self):
        self._elem = []
    def add(self, new_element):
        self._elem += new_element
    def size(self):
        return len(self._elem)

print(type(Toy))
print(type(Toy.__init__), type(Toy.add), type(Toy.size))
#
# t1 = Toy()
# print(type(t1))
# print(type(t1.add))
#
# t2 = Toy()
# print(t1 is t2) #False

t1 = Toy()
t2 = Toy()

t1.add = ([3.4])
t2.add([4])

print(t1.size() + t2.size())
print(t1.add)
print(t2.add)