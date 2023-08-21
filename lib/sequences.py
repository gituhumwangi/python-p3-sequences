#!/usr/bin/env python3

def print_fibonacci(length):
    pass
    if length <= 0:
        return[]
    elif length == 1:
        return[0]

    
    fibonacci_sequence = [0,1]
    while len (fibonacci_sequence) < length :
        next_number=fibonacci_sequence[-1] + fibonacci_sequence[-2] 
        next_number.append(fibonacci_sequence)
    print(fibonacci_sequence)
    return fibonacci_sequence
    
    

    

    


