# Crossover point

 
# Defination : The point at which value of fuzzy set = 0.5 , is called cross-overpoint

A = dict()
A = {"a": 1, "b": 0.3, "c": 0.5, "d": 0.2 ,"e":0.5}

for i in A :
     X = A[i]
     if X == 0.5 :
         print('for',i,'= 0.5 , crossover point is present')

