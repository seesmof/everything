# Import the path module from os
from os import path

# Define a path to the current directory using the path module
current_directory = path.dirname(path.abspath(__file__))

# Define the name of the file you want to access
file_name = "your_file_name.csv"

# Create a file path variable, which is a string by either combining the current directory and the file name
wanted_file_path: str = path.join(
    current_directory, file_name
)  # You can just replace the file name variable with your actual file name as a string

# Or, you could just use Python's f-strings to form a path, which is more readable, but might not be as stable
wanted_file_path: str = f"{current_directory}/{file_name}"
