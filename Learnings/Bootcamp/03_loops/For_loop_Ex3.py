# Print ONLY even numbers from 1–20

""" for even in range (1, 21):
    if even % 2 == 0:
        # print(f"The even numbers from 1 to 20 are: ")
        print(even, end=" ") """

for even in range (1, 21):
    if even % 2 == 0:
        evens = [even for even in range(1, 21) if even % 2 == 0]
print(f"The even numbers from 1 to 20 are: {' '.join(map(str,evens))}") # display the numbers without the []
