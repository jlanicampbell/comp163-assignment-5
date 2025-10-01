# given a positive integer n:
# if in is even, didvde it by 2
# if n is odd, multiply it by 3 and add 1
# continue until n equals 1
# count total steps taken 
print("=== Challenge 1: Collatz Conjecture ===")

current_number = int(input("Enter starting number: "))
step_count = 0

print("Sequence:", current_number, end=" ")

# create loop until the number becomes 1
while current_number != 1:
    if current_number % 2 == 0:
        current_number = current_number // 2
    else:
        current_number = current_number * 3 + 1 
    
    print(current_number, end=" ")
    step_count = step_count + 1

# loop ends, print total steps
print("\nSteps:", step_count)
print()

# Challenge 2: Prime Number Checker 

print("=== Challenge 2: Prime Number Checker ===")

n = int(input("Enter a nuumber: "))

if n > 1:
    print(f"Testing divisors from 2 to {n - 1}...")
    for i in range(2, n):
        if n % i == 0:
            print(f"{n} is not prime (divisible by 3)")
            break
# only if no divisor was found
    else:
        print(f"{n} is prime!")
else:
    print(f"{n} is not prime")
print()

# Challenge 3: Multiplication
print("=== Challenge 3: Multiplication Table ===")
print("Multiplication Table:")

# print column headers
print("  ", end="")
for col in range(1, 11):
    print(f"{col:3}", end="")
print()

# print rows 
for row in range(1, 11):
    print(f"{row:3}", end="")
    for col in range(1, 11):
        print(f"{row * col:3}", end="")
    print()

# used chatgbt to help explain loop variables (row, and col)