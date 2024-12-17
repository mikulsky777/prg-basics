def mean(x,y):
   avg = (x+y)/2
   return avg

n1 = int(input("Enter 1-st number: "))
n2 = int(input("Enter 2-nd number: "))

result = mean(n1,n2)
print(f'The arithmetic mean of the numbers {n1} and {n2} is {result}')