import math
import os
import random
import re
import sys


# write your code here
def avg(*num):
    if len(num)==0:
        return None
    sum=0
    for i in num:
        sum=sum+i
        moy=sum/len(num)
    return(moy)

nums = map(int, input().split())
res = avg(*nums)
print(res)
    
    