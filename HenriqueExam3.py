# Henrique Exam Program 3
# Henrique Medeiros dos Reis
# 12/09/2019

def main():
    NUMBEROFNUMS = 10
    number_list = [] 
    
    print('Before choosing what you want to do, please enter 10 integers between'+
          ' 1 and 100.')
    for i in range(NUMBEROFNUMS):
        user_num = int(input('Enter the number: '))
        while user_num < 1 or user_num > 100:
            user_num = int(input('You must enter a number between 1 and 100, try again: '))
        number_list.append(user_num)
    print('List of numbers:\n', number_list, sep=' ')

    displayMenu()            
    choice = int(input('Enter your choice: '))
    while choice != 4:
        if choice == 1:
            for i in range(NUMBEROFNUMS):
                largest = find_largest(number_list)
            print('The largest number is: ', largest)

        elif choice == 2:
            for i in range(NUMBEROFNUMS):
                smallest = find_smallest(number_list)
            print('The smallest number is: ', smallest)

        elif choice == 3:
            for i in range(NUMBEROFNUMS):
                sum = sum_list(number_list)
            print('The sum of all the numbers in the list is: ', sum)
            
        else:
            print('Incorrect entry. Please enter 1 through 5')
        displayMenu()
        choice = int(input('Enter your choice: '))
        
def displayMenu():
    print('Enter 1 to find the largest number')
    print('Enter 2 to find the smallest number')
    print('Enter 3 to sum the list of numbers')
    print('Enter 4 to exit')
    
def find_largest(number_list):
    n = len(number_list)
    if n == 1:
        return number_list[0]
    else:
        temp = find_largest(number_list[0:n-1])
        if number_list[n-1] > temp:
            return number_list[n-1]
        else:
            return temp

def find_smallest(number_list):
    n = len(number_list)
    if n == 1:
        return number_list[0]
    else:
        temp = find_smallest(number_list[0:n-1])
        if number_list[n-1] < temp:
            return number_list[n-1]
        else:
            return temp
def sum_list(number_list):
    n = len(number_list)
    if len(number_list) == 1:
        return number_list[0]
    else:
        return number_list[n - 1] + sum_list(number_list[0: n - 1])

main()
