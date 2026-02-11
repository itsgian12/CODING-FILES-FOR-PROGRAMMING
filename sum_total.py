def sum(num1 ,num2):
    def new_func(num1, num2):
        return num1 + num2
    return new_func(num1, num2)
    
total = sum(10,20)
print(total)

# print (sum(10,sum(10,5)))
