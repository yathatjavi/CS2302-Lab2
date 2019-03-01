
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 19:00:04 2019

@author: yathatjavi
Professor Olac fuentes
TAs:
    -Anindita Nath
    -Maliheh Zaragaran
IA
    -Eduardo Lara
Peer Leader
    -Erick Macik
    
the puspose of this lab is to demonstrate my knowldge of implementing different
sort algorithms with a provided sigly linked list abstract data type as 
provided by Professor Olac Fuentes
"""

import lists
from random import randint
from datetime import datetime as dt

def fillList(L):
    n = int(input(' What size list would you like to test?'))
    for i in range(n):
        lists.Append(L,randint(0,100))

def qSortHelper(item,L1,L2,pivot):
    #used to create two lists 
    #L! will hold items smaller than pivot
    #L2 contains the latter
    if item < pivot:
       lists.Append(L1,item)
    else:
       lists.Append(L2,item)
    return L1, L2
 
def quickSort(L):
    #will take a list break that list into two samller with items greater
    #or less than the item at index 0
    #will then concatinate the two lists after all recursive calls
    if L.size >1:
        pivot = L.head.item
        l1=lists.List()
        l2=lists.List()
        #for every element in L
        temp =L.head.next
        while temp is not None:
            l1,l2 = qSortHelper(temp.item,l1,l2,pivot)
            temp = temp.next
        quickSort(l1)
        quickSort(l2)
        #lists.Append(l1,pivot)
        lists.Prepend(l2,pivot)
        lists.Concatenate(l1,l2)
        L.head = l1.head
        
def fillTList(L):
    lists.Append(L,1)
    lists.Append(L,2)
    lists.Append(L,3)
    lists.Append(L,4)
    lists.Append(L,5)
    
def swap(n1,n2):
    #used to swap the items of two nodes withotu swaping the node
    temp = n2.item
    n2.item=n1.item
    n1.item=temp
    
def bubbleSort(L):
    #will take a list and iterate through swapping items if the current item is
    #larger than the susseding item
    #will return a sorted list of thoes items
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
    #will take two lists and create a single list of order items contatined
    #in the two smaller lists
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
    # will split the provied list in half with equal nodes in each list if 
    #given a a list with even amount of nodes
    if count < size/2:
        lists.Append(LL, item)
    else:
        lists.Append(RL,item)
               
def mergeSort(L):
    #will take a list and break it down into two smaller lists and iterate the
    #smaller lists appedning the smaller item of both sorted lsits to the now 
    #sorted list
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
    if L is not None and n < L.size:
        t = L
        if n == 0:
            return t.head.item
        else:
            t.head= t.head.next
            #temp = lists.List()
            #temp.head=t
            return rank(t,n-1)
        
def rank01(L,n):
    if lists.IsEmpty(L):
        return None
    temp=L.head
    while temp is not None and n > 0:
        temp=temp.next
        n= n-1
    return temp.item
        
def quickSortMotified(L,n):
    if L.size>1:
        t=L.head
        rnk = rank01(L,n)
        pivot = L.head.item
        smallList = lists.List()
        largeList = lists.List()
        while t is not None:
            #print(t.item)
           smallList,largeList = qSortHelper(t.item,smallList,largeList,pivot)
           t = t.next
        if(pivot == rnk): # rank n is pivot
            return pivot
        elif(lists.Contains(smallList,rnk)): # rank n in small list
            nr = rank01(largeList,largeList.head.item)
            return quickSortMotified(largeList,nr)
        else: # rank n in large list
            nr = rank01(smallList,smallList.head.item)
            return quickSortMotified(smallList,nr)
            
        
def quickSM(L,n):
    if L.size >1:
        t=L.head
        pivot = L.head.item
        smallList = lists.List()
        largeList = lists.List()
        t = t.next
        while t is not None:
            smallList,largeList = qSortHelper(t.item,smallList,largeList,pivot)
            t = t.next
        if (smallList.size+1)==n:
            return pivot
        elif (smallList.size+1)<n:
            return quickSM(largeList,0)
        else:
            return quickSM(largeList,0)
            
L= lists.List()
emptyList= lists.List() 
testList= lists.List()
fillList(L)
fillTList(testList)

print('Original list: ', end=' ')
#lists.Print(L)
starttime=dt.now()
bubbleSort(L)
endtime=dt.now()-starttime
print('it took ' + str(endtime) + ' to execute')
#quickSort(L)
#mergeSort(L)
#print(quickSM(L,L.size/2))

#lists.Print(L)

'''
lists.Append(L,10)
lists.Append(L,90)
lists.Append(L,1)
lists.Print(L)'''

