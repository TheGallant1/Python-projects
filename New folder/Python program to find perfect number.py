ef is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_perfect_numbers(limit):
    perfect_numbers = []
    p = 2
    
    while True:
        mersenne = (2 ** p) - 1
        if is_prime(mersenne):
            perfect_number = (2 ** (p - 1)) * mersenne
            if perfect_number > limit:
                break
            perfect_numbers.append(perfect_number)
        p += 1
    
    return perfect_numbers
  
limit = 1000000
perfect_numbers = find_perfect_numbers(limit)
print(f"Perfect numbers up to {limit}: {perfect_numbers}")
