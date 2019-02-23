# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 19:00:04 2019

@author: yathatjavi
"""

import lists
from random import randint

def fillList(L):
    n = int(input(' What size list would you like to test?'))
    for i in range(n):
        lists.Append(L,randint(0,100))

def qSortHelper(item,L1,L2,pivot):
    if item < pivot:
       lists.Append(L1,item)
    else:
       lists.Append(L2,item)
    
def quickSort(L):
    if L.size >1:
        pivot = L.head.item
        l1=lists.List()
        l2=lists.List()
        #for every element in L
        temp =L.head.next
        while temp is not None:
            qSortHelper(temp.item,l1,l2,pivot)
            temp = temp.next
        quickSort(l1)
        quickSort(l2)
        lists.Append(l1,pivot)
        #lists.Prepend(l2,pivot)
        lists.Concatenate(l1,l2)
        
        L.head = l1.head
        
def fillTList(L):
    lists.Append(L,1)
    lists.Append(L,2)
    lists.Append(L,3)
    lists.Append(L,4)
    lists.Append(L,5)
    
def swap(n1,n2):
    temp = n2.item
    n2.item=n1.item
    n1.item=temp
    
def bubbleSort(L):
    if L.head== None:
        return
    done = False
    while done is not True:
        done = True
        t = L.head
        while t.next is not None:
            if t.next.item < t.item:#if next item is smaller swap node.items
              swap(t.next,t)
              done = False
            t= t.next
            
def merge(LL,RL):
    t1 = LL.head
    t2 = RL.head
    SL =lists.List()
    while t1 is not None or t2 is not None:
        if t2 == None or t1.item < t2.item:
            #if left list item small or right list is empty append
            lists.Append(SL,t1.item)
            t1=t1.next
        else:
            lists.Append(SL,t2.item)
            t2=t2.next
    return SL
def mergSplitter(LL,RL,count,item,size):
    if count < size/2:
        lists.Append(LL, item)
    else:
        lists.Append(RL,item)
               
def mergeSort(L):
    SL = lists.List()
    if L.size >1:
        counter =0
        temp = L.head
        #split into 2 smaller lists
        ll =lists.List()
        rl =lists.List()
        while temp is not None:
            mergSplitter(ll,rl,counter,temp.item,L.size)
            counter =+1
            temp = temp.next
        mergeSort(ll)
        mergeSort(rl)
        SL=merge(mergeSort(ll), mergeSort(rl))
    #L.head= SL.head
        
def rank(L,n):
    t = L.head
    if n == 0:
        return t.item
    else:
        t = t.next
        temp = lists.List()
        temp.head=t
        return rank(temp,n-1)

def quickSortMotified(L,n):
    t=L.head
    rnk = rank(L,n)
    if n >1:
        pivot = L.head.item
        smallList = lists.List()
        largeList = lists.List()
        while t is not None:
            #print(t.item)
            qSortHelper(t.item,smallList,largeList,pivot)
            t = t.next
        if(pivot == rank): # rank n is pivot
            return pivot
        elif(lists.Contains(smallList,rnk)): # rank n in small list
            nr = rank(largeList,largeList.head.item)
            return quickSortMotified(largeList,nr)
        else: # rank n in large list
            nr = rank(smallList,smallList.head.item)
            return quickSortMotified(smallList,nr)
            
L= lists.List()
emptyList= lists.List()
testList= lists.List()
fillList(L)
fillTList(testList)

print('Original list: ', end=' ')
lists.Print(L)
#bubbleSort(L)
#quickSort(L)
#mergeSort(L)
#print(lists.isSorted(testList))
print(quickSortMotified(L,3))

lists.Print(L)

'''
lists.Append(L,10)
lists.Append(L,90)
lists.Append(L,1)
lists.Print(L)'''

