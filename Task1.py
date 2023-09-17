
#Imperative paradigm
def print_multiplication_table_imp(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f'{i} * {j} = {i*j}')


def print_multiplication_table_func(n):
    def multiply(i, j):
        print(f'{i} * {j} = {i*j}')

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            multiply(i, j)




n = int(input('Enter a number: '))
print_multiplication_table_imp(n)


n = int(input('Enter a number: '))
print_multiplication_table_func(n)
