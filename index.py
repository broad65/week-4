# File Read & Write Challenge
def modify_file(input_file, output_file):
    try:
        # Open the input file to read
        with open(input_file, "r") as file:
            content = file.read()

        # Modify the content (for example, converting to uppercase)
        modified_content = content.upper()

        # Write the modified content to the new output file
        with open(output_file, "w") as file:
            file.write(modified_content)

        print(f"Modified content has been written to {output_file}")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except IOError:
        print(f"Error: There was an issue reading or writing to the files.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
input_filename = "example.txt"  # Replace with your input file
output_filename = "modified_example.txt"  # New file to save modified content
modify_file(input_filename, output_filename)


# Error Handling Lab: Ask for filename and handle errors
def read_file():
    filename = input("Please enter the filename: ")
    
    try:
        # Try to open the file
        with open(filename, "r") as file:
            content = file.read()
            print("\nFile content:")
            print(content)
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"Error: The file '{filename}' cannot be read.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
read_file()
