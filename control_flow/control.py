# Write a function that uses while, if and continue statements 
# to print all the even numbers between 0 and 50. 

def even_numbers():
    num = 0
    while num <= 50:
        if num % 2 == 0:
            print(num)
        num += 1


# Write a function that takes an integer argument and prints
#  "Prime" if the number is prime, and "Not prime" if the number is not prime.


def prime_numbers(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                print("Not prime")
                break
        else:
            print("Prime")
    else:
        print("Not prime")



# Write a function that takes a list of integers as input 
# and prints the sum of all the even numbers in the list.

def list_of_integers(input_sum):
    total = 0
    for num in input_sum:
        if num % 2 == 0:
            total += num
    print(total)


# Write a function that takes any two integers as input, and 
# prints the sum of all the numbers between the two integers (inclusive) that are divisible by 3.

def sum_of_numbers(num1, num2):
    total = 0
    for num in range(num1, num2+1):
        if num % 3 == 0:
            total += num
    print(total)
