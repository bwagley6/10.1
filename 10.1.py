import os


# function to make directory if not exists and return it's name
def make_directory():
    # get the directory input from the user
    directory = input("Enter the directory you would like to save: ")
    # check if the directory does not exist
    if not os.path.isdir(directory):
        # create the directory
        os.mkdir(directory)
    # return the directory name entered by the user
    return directory


def main():
    # call the make directory function to create the directory
    directory = make_directory()
    # get the file name, name, address, phone from the user
    file_name = input("Enter file name: ")
    name = input("Enter name: ")
    address = input("Enter address: ")
    phone_number = input("Enter phone number: ")

    # open the file in that specified directory
    with open(f"{directory}/{file_name}", "a") as file:
        # make the comma separated line and write the line to file
        line = f"{name},{address},{phone_number}"
        file.write(line)
    # close the file
    file.close()

    # open the file again in read mode and print the contents of the file
    with open(f"{directory}/{file_name}") as file:
        print("File contents:")
        print(file.read())


main()