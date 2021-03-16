# This program demonstrates a function that accepts two arguments.
def main():
    input1 = int(input('Gimme a number. '))
    input2 = int(input('Gimme another number. '))
    results = calculate_sum(input1, input2)
    print('The sum of ' + str(input1) + ' and ' + str(input2) + ' is: ' + str(results))

# The calculate_sum function accepts two arguments.
def calculate_sum(x, y):
    sum = x + y
    return sum

main()
