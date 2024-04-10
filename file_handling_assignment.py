from importlib.resources import contents


def write_to_file(filename,content):
    """Writes content to a file in write mode ('w')

    Args:
    filename: Jessica
    content: I love Jessica
    """
    try:
        with open(filename, 'w') as file:
            file.write(content)
            print(f"Successfully wrote to {filename}")
    except FileNotFoundError:
        print(f"Error:File'{filename}'")
    except PermissionError:
        print(f"Error: Insufficient permissions to write to'{filename}'")
    finally:
        if 'file' in locals():
            file.close()

def read_from_file(filename):
    """
    Reads the contents of the file and display on the console
    Args:
        filename: Brian
        """
    try:
        with open(filename,'r') as file:
            content = file.read()
            print(f"\nContents of'{filename}':\n{content}")
    except FileNotFoundError:
        print(f"Error:File'{filename}' not found")
    except PermissionError:
        print(f"Error: Insufficient permissions to read from '{filename}'")

def append_to_file(filename):
    """
    Appends content to a file in append mode'a'
    Args:
        filename:Love 
        content: Love is a beautiful thing
        """
    try:
        with open(filename,'a') as  file:
            file.write(contents() + "\n")
            print(f"Successfully appended to '{filename}'")
    except FileNotFoundError:
        print(f"Error:File '{filename}' is not found.")
    except PermissionError:
        print(f"Error: Insufficient permissions to append to '{filename}'")
    finally:
        if 'file' in locals():
            file.close()

write_to_file("my_file.txt", "This is the first line.\n")
write_to_file("my_file.txt","Here's some more text with a number:42/n")
write_to_file("my_file.txt", "This is my final line.\n")

read_from_file("my_file.txt")

append_to_file("my_file.txt","Appended line 1.\n")
append_to_file("my_file.txt", "Appended line 2 with another number: 100\n")
append_to_file("my_file.txt", "This is the final appended line.")

read_from_file("my_file.txt")


