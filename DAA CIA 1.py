# -*- coding: utf-8 -*-
"""

@author: C J HARINI
"""


import numpy as np
import random as rd 

def generate_sequence(): #equal distrbution
    chars = ['a','c','g','t']
    s1 = ''
    s2 = ''
    l = 16
    a_ct = c_ct = g_ct = t_ct = 0
    
    while len(s1) < l:
        ch = rd.choice(chars)
        if ch=='a' and a_ct<4:
            s1+=ch
            a_ct+=1
        elif ch=='c' and c_ct<4:
            s1+=ch
            c_ct+=1
        elif ch=='g' and g_ct < 4:
            s1+=ch 
            g_ct+=1
        elif ch == 't' and t_ct < 4:
            s1+=ch
            t_ct+=1
    
    a_ct = c_ct = g_ct = t_ct = 0
    
    while len(s2) < l:
        ch = rd.choice(chars)
        if ch=='a' and a_ct<4:
            s2+=ch
            a_ct+=1
        elif ch=='c' and c_ct<4:
            s2+=ch
            c_ct+=1
        elif ch=='g' and g_ct < 4:
            s2+=ch 
            g_ct+=1
        elif ch == 't' and t_ct < 4:
            s2+=ch
            t_ct+=1
    
    return s1,s2

# a,b = generate_sequence()
# print(a,type(a))
# print(b,type(b))
a = "ttttgggaccacgcaa"
b = "caggggttctaactca"

cols = len(b)
rows = len(a)

arr = np.zeros((rows+1, cols+1), dtype=int)

Parent = [[0]*(cols+1) for i in range(rows+1)]
score = 5
penalty = -4


def align(arr,i,j): # recursive code to print Matrix
    if a[i-1] == b[j-1]:
            arr[i][j] = arr[i-1][j-1]+score
    else:
            m = max(arr[i-1][j-1], arr[i-1][j], arr[i][j-1])
            arr[i][j] = m + penalty  
    if j!=len(b):
        return align(arr,i,j+1)
    elif i==len(a):
        print(arr)
    else:
        j=1
        return align(arr,i+1,j)

print(align(arr,rows,cols))

for i in range(1, rows+1):

    for j in range(1, cols+1):

        if a[i-1] == b[j-1]:
            arr[i][j] = arr[i-1][j-1]+score
            Parent[i][j] = (i-1, j-1)

        else:
            m = max(arr[i-1][j-1], arr[i-1][j], arr[i][j-1])
            if arr[i-1][j-1] > arr[i-1][j] and arr[i-1][j-1] > arr[i][j-1]:
                Parent[i][j] = (i-1, j-1)
            elif arr[i-1][j] > arr[i-1][j-1] and arr[i-1][j] > arr[i][j-1]:
                Parent[i][j] = (i-1, j)
            elif arr[i][j-1] > arr[i-1][j] and arr[i][j-1] > arr[i-1][j-1]:
                Parent[i][j] = (i, j-1)

            arr[i][j] = m + penalty

maxx = arr[rows].max()

# print(maxx)
z, x = np.where(arr == maxx)
z = z[0]
x = x[0]

print(arr)
# print(z)
# print(x)

ans = []
p=[]

while(True):
    if z == 0 and x == 0:
        break

    ans.append(arr[z][x])
    p.append((z,x))
    idx = Parent[z][x]
    z = idx[0]
    x = idx[1]

print('\n', ans)

s1=''
s2=''

for i in range(len(p)):
    t=p[i]
    t1=t[0]-1
    t2=t[1]-1
    if a[t1]==b[t2]:
        s1+=a[t1]
        s2+=a[t1]
    else:
        prev=p[i+1]
        if t1<prev[0] and t2==prev[1]:
            s1+='_'
            s2+=b[t2]
        elif t1==prev[0] and t2<prev[1]:
            s2+='_'
            s1+=a[t1]

s1=s1[::-1]
s2=s2[::-1]
print('\n')
print(s1)   
print(s2)