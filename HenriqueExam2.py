# Henrique Medeiros dos Reis
# Exam 2
# 10/23/2018

def main():
    displayMenu()
    choice = int(input('Enter your choice: '))
    
    while (choice != 5):
        if (choice == 1): # create a method
            get_user_string(user_string)
            user_string = user_string.upper()
            print(user_string)# correct the display   
        elif(choice == 2):# create a method 
            user_string = (input('Please, enter the string: ')).lower()
            print(user_string)# correct the display
        elif(choice == 3):# create a method 
            number_of_words()
        elif(choice == 4):   # create a method 
            user_string = (input('Please, enter the string: '))
            vowels = vowel_counter(user_string)
            print(user_string) # correct display
        else:
            print('Incorrect entry. Enter 1 through 5')
        displayMenu()
        choice = int(input('Enter your choice: '))
    
    
def displayMenu():
    print('Enter 1 to convert a string to uppercase. ')
    print('Enter 2 to convert a string to lowercase. ')
    print('Enter 3 to count the number of words in a string. ')
    print('Enter 4 to count the number of vowels. ')
    print('Enter 5 to exit. ')

def vowel_counter(user_string):
    count = 0
    vowels = 'aeiou'
    for ch in user_string:
        if vowels.find(ch) >=0:
            count += 1
    return count

def get_user_string(user_string):
    
    user_string = input('Please, enter the string: ')
    while len(user_string) <= 0:
        user_string = input('You must enter at least two character.Please try again: ')
    return user_string
main()
