#!/usr/bin/env python3

def print_fibonacci(num):
    pass
    if num <= 0:
        print([])
    elif num == 1:
        print([0])
    elif num == 2:
        print([0,1])

    
    fibonacci_sequence = [0,1]
    while len (fibonacci_sequence) < num :
        next_number=fibonacci_sequence[-1] + fibonacci_sequence[-2] 
        fibonacci_sequence.append(next_number)
    # print(fibonacci_sequence)
    return fibonacci_sequence
    
    
    

print(print_fibonacci(10))


    


