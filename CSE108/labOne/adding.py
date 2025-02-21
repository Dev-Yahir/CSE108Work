import array

nums = input("Enter two or more numbers seperated by spaces: ") #takes input from the user

if not nums.strip(): #checks to see if the input is empty
    print("Error: Please enter a String.")
    exit()

arr = array.array('d') #array that contains all the numbers entered by the user

def makeNumbers(numList): #function that takes the input and converts it to a array of numbers
    global arr
    try: #creates the list of integers and then appends them to the array
        numbers = list(map(float, numList.split()))
        arr.extend(numbers)
    except ValueError: #checks to see if the input is a number
        print("Error: Please enter valid input seperated by spaces.")
        exit()
    
    if(len(arr) < 2): #checks to see if the input is less than 2
        print("Error: Please enter two or more numbers.")
        exit()

makeNumbers(nums) #takes input and converts it to a array of numbers that pass the input parameters
numsum = sum(arr) #sums the numbers in the array that the user entered

print("The sum of the numbers is: ", numsum) #final output