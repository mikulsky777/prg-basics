N = int(input("Enter the number of leading prime numbers to find: "))

primes = [] 
current_number = 2 

while len(primes) < N:
    is_prime = True  
    
    for i in range(2, int(current_number**0.5) + 1):
        if current_number % i == 0:
            is_prime = False  
            break 

    if is_prime:
        primes.append(current_number)
    
    current_number += 1  

print("Prime numbers:", " ".join(map(str, primes)))