# Écrivez un programme Python pour trouver la médiane parmi trois nombres donnés comme input


# Input the first number 25
# Input the second number 15
# Input the third number 35
# Median of the above three numbers -
# 25

# a=25
# b=15
# c=35

# import statistics
# print(statistics.median([a,b,c]))

# correction 

numbers=[]
input_len = int(input("sasir le nombre de chiffre voulu"))

for i in range(input_len):
    val=float(input(f"entre number { i + 1 } ;"))
    numbers.append(val)

numbers.sort()

input_len = len(numbers)
mid=input_len //2

if input_len % 2 ==1 :
    median=numbers[ mid ]
else :
    median=(numbers[mid-1]+numbers[mid])/2

print("le median est :",median)