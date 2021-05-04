# QUESTION :

# Create a list consisting of Fibonacci numbers from 1 to 55 using control flow statements.

# The desired output is like :

# fibonacci →  [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# ANSWER :

fibonacci = [1, 1]  # Fibonacci numbers begin with (1, 1)

for i in range(1, 56):
  if i == fibonacci[-1] + fibonacci[-2]:  # rule of the Fibonacci numbers
    fibonacci.append(i)

print(fibonacci)

