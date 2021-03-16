# This program has two functions.
# First, define the main() function.
def main():
    print('I have a message for you.')
    x = 3
    message(x)
    print('See you later!')

# Define the function
def message(num):
    n = 0
    while n < num:
        print('The num is: ', n)
        n += 1
    # print('I like coding.')
    # print('Python is my favorite language!')

# Call the function
main()
