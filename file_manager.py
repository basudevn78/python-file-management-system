import os

# Function to create a new file
def create_file(filename):
    try:
        with open(filename,'x') as f:
            print(f"{filename} file created successfully...!")
    except FileExistsError:
        print(f"Given filename is already exist....! \nTry something else.")
    except Exception as e:
        print(f"An unidentified error occured.....! \n{e}")

# Function to list all files in the current directory
def list_of_files():
    files= os.listdir()
    if not files:
        print("No file found...!")
    else:
        print("Files in directory :")
        for file in  files:
            print(file)

# Function to read the content of a file
def read_file(filename):
    try:
        with open(filename,'r') as f:
            content = f.read()
            print(f"Contents of '{filename}' - \n{content}")
    except FileNotFoundError:
        print(f"{filename} doesn't exist...!")
    except Exception as e:
        print(f"An unidentified error occured.....! - {e}")

# Function to read a file line-by-line with line numbers
def read_file_lines(filename):
    try:
        with open(filename, 'r') as f:
            for i, line in enumerate(f, 1):
                print(f"{i}: {line.strip()}")
    except FileNotFoundError:
        print(f"{filename} doesn't exist...!")

# Function to append content to a file
def edit_file(filename):
    try:
        with open(filename,'a') as f:
            content = input("Enter data to add :\n")
            f.write(content + "\n")
            print(f"Content added to {filename} succcessfully....!")
    except FileNotFoundError:
        print(f"{filename} file is not found....!")
    except Exception as e:
        print(f"An unidentified error occured.....! - {e}")

# Function to overwrite content in a file (deletes existing content)
def overwrite_file(filename):
    try:
        with open(filename, 'w') as f:
            content = input("Enter new content :\n")
            f.write(content + "\n")
            print(f"{filename} has been overwritten.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to rename a file
def rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(f"File renamed from {old_name} to {new_name}")
    except FileNotFoundError:
        print(f"{old_name} not found!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to search for files containing a specific keyword
def search_files(keyword):
    files = os.listdir()
    matches = [f for f in files if keyword in f]
    if matches:
        print("Matched files:")
        for file in matches:
            print(file)
    else:
        print("No files matched to your search.")

# Function to delete a file
def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} file has been deleted successfully....!")
    except FileNotFoundError:
        print(f"File not found with filename - {filename}")
    except Exception as e:
        print(f"An unidentified error occured.....! - {e}")

# Main function to handle user interaction
def main():
    while True:
        print("\nFILE MANAGEMENT\n")
        print("1: Create file")
        print("2: View all the files")
        print("3: Read file")
        print("4: Read file lines")
        print("5: Edit file")
        print("6: Overwrite file (Existing content will be erased)")
        print("7: Rename file")
        print("8: Search a file")
        print("9: Delete file")
        print("10: Exit")

        choice = input("Enter your Choice(1-10) : ")
        
        # Match-case statement to handle user's choice
        match choice:
            case '1':
                filename = input("Enter the filename : ")
                create_file(filename)
            case '2':
                list_of_files()
            case '3':
                filename = input("Enter the file name : ")
                read_file(filename)
            case '4':
                filename = input("Enter the file name : ")
                read_file_lines(filename)
            case '5':
                filename = input("Enter the file name : ")
                edit_file(filename)
            case '6':
                filename = input("Enter the file name : ")
                overwrite_file(filename)
            case '7':
                filename = input("Enter the name of the file : ")
                new_filename = input("Enter the new name of the file : ")
                rename_file(filename,new_filename)
            case '8':
                keyword = input("Enter a keyword to search the file : ")
                search_files(keyword)
            case '9':
                filename = input("Enter the file name : ")
                delete_file(filename)
            case '10':
                break
            case _:
                print("Invalid choice.......!")


if __name__ == "__main__":
    main()