# comp163-assignment-5
Complete three sequential programming challenges demonstrating mastery of while loops, for loops, and nested loops. Use git workflow from previous assignments. 

# Challenge 1: Collatz Conjecture
I used a 'while' loop because the number of iterations is unknown. The loop needs to continue running until the current number reaches 1, which can take a different number of steps depending on the input.
The program checks if the number is even or odd. If it’s even, it divides by 2. If it’s odd, it multiplies by 3 and adds 1. Each new value is printed until the number reaches 1, while also counting how many steps it takes.
  
# Challenge 2: Prime Number Checker
I used a 'for' loop because the range of possible divisors is known (from 2 up to n-1). A 'for' loop is best when we know the exact range to test.
The program goes through each number from 2 up to n-1. If one of those numbers divides evenly into n, the loop stops and prints that the number is not prime. If no divisor is found, the loop finishes normally and the program prints that the number is prime.

# Challenge 3: Multiplication Table
I used nested 'for' loops. The outer loop goes through the rows, and the inner loop goes through the columns. A 'for' loop is best because we know the exact range of numbers (1 to 10).
The program first prints the header row with numbers 1 through 10. Then, for each row number, it multiplies by each column number and prints the result, creating a grid.

# AI Assistance
I used chatgbt to help explain loop variable concepts (row, and col)