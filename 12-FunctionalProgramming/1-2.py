n1 = int(input("Enter 1-st number: "))
n2 = int(input("Enter 2-nd number: "))

# define an anonymous function
mean = lambda x,y: (x+y)/2


result = mean(n1,n2)
print(f'The arithmetic mean of the numbers {n1} and {n2} is {result}')