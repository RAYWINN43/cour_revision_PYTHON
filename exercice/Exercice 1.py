# Écrivez une fonction Python qui prend une séquence de nombres et détermine si tous les nombres sont différents les uns des autres.
# test_distinct=[1, 5, 7, 9]
# test_distinct=[2, 4, 5, 5, 7, 9]

def distinctlist(test_distinct):
    if len(test_distinct) == len(set(test_distinct)):
        return True   
    else:
        return False  
    
print(distinctlist([1, 5, 7, 9])) 
print(distinctlist([2, 4, 5, 5, 7, 9])) 