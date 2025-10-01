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
