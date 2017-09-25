#! /usr/bin/python3
 
T = int(input())
for j in range(0,T):
  n = int(input())
  for val in range(399,(399+n)):
    print('{0}'.format(val),end=' ')
  print()