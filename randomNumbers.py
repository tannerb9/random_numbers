import random
''' Print a message to the console indicating whether each value of
`number` is in the `my_randoms` list.
'''

my_randoms = list()
for i in range(10):
    my_randoms.append(random.randrange(1, 6))

numbers_1_to_10 = range(1, 11)

for number in numbers_1_to_10:
    if number in my_randoms:
        print(f"{number} is in the random list")
