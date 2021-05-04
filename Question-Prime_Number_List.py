# QUESTION : 

# Print the prime numbers which are between 1 to entered limit number (n).

# 1.You can use a nested for loop.
# 2.Collect all these numbers into a list

# The desired output for n=100 :

# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
# 61, 67, 71, 73, 79, 83, 89, 97]

# ANSWER :

def prime_list(n):
  prime = []
  for i in range(1, n):
    count = 0
    for k in range(1, i + 1):
      if i % k == 0:
        count += 1
    if count == 2:
      prime.append(i)
  print(prime)

prime_list(100)


