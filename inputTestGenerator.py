import random

# The time it takes to map out 100,1000,10000,100000,1000000 random integers (using the same set each time). Have those sets in a separate set of files so you can just call up the files to get the numbers

with open("Testing Data/inputTest100.txt", "w") as file:
    file.write(f'{[random.randint(-1000000,1000000) for index in range(100)]}')

with open("Testing Data/inputTest1000.txt", "w") as file:
    file.write(f'{[random.randint(-1000000,1000000) for index in range(1000)]}')

with open("Testing Data/inputTest10000.txt", "w") as file:
    file.write(f'{[random.randint(-1000000,1000000) for index in range(10000)]}')

with open("Testing Data/inputTest100000.txt", "w") as file:
    file.write(f'{[random.randint(-1000000,1000000) for index in range(100000)]}')

with open("Testing Data/inputTest1000000.txt", "w") as file:
    file.write(f'{[random.randint(-1000000,1000000) for index in range(1000000)]}')
