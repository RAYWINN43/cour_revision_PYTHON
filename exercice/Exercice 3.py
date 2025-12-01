# Écrivez un programme Python pour obtenir la série de Fibonacci entre 0 et 50.

# Remarque : La Suite de Fibonacci est la série de nombres :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Chaque nombre suivant est trouvé en additionnant les deux nombres qui le précèdent.


# 1                                                                                                             
# 1                                                                                                             
# 2                                                                                                             
# 3                                                                                                             
# 5                                                                                                             
# 8                                                                                                             
# 13                                                                                                            
# 21                                                                                                            
# 34

a=0
b=1
i=0
temp=0
while i <10:
    print(a)
    temp=a
    a=b
    b=temp+b
    i +=1