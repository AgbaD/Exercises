def is_prime(number):
    cond = False
    a = number//2
    if number == 0 or number == 1:
        print('Number not valid!')
        return cond

    if number == 2 or number == 3:
        cond = True
    else:
        count = 0
        o = [i for i in range(2, a+1)]
        for i in o:
            if number % i == 0:
                cond = False
                break
            else:
                count += 1
        if count == len(o):
            cond = True
        
    return cond

def largest_prime_factor(n):
    factors = [i for i in range(2, n+1) if n%i == 0]
    prime = [i for i in factors if is_prime(i)]
    return max(prime)


ans = []
t = int(input("Enter the number of test cases\n"))
for i in range(t):
    n = int(input("Enter the integer(s) to be tested per line\n"))
    a = largest_prime_factor(n)
    ans.append(a)

print()
for val in ans:
    print(val)