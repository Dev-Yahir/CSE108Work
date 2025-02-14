sentence = input("Enter a sentence that you would like to be repeated: ")

amount = int(input("How many times would you like it to be repeated? "))

file_path = "CompletedPunishment.txt"

try:
    with open(file_path, "a") as file1:
        for i in range(amount):
            file1.write(sentence + "\n")
    # print(f"File '{file_path}' created and written successfully.") --> used to check if output was correct
except IOError:
    print("An error occurred while writing to the file.") #In case the file is not created
    exit()
