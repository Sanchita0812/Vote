import os

def update_file(filepath, new_content):
    """Updates the content of a file.

    Args:
        filepath: The path to the file.
        new_content: The new content to write to the file.
    
    Raises:
        FileNotFoundError: If the file does not exist.
        IOError: If there's an error writing to the file.

    """
    try:
        with open(filepath, 'w') as f:
            f.write(new_content)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath}")
    except IOError as e:
        raise IOError(f"Error writing to file: {e}")


def append_to_file(filepath, content_to_append):
    """Appends content to an existing file.

    Args:
        filepath: Path to the file.
        content_to_append: Content to append.

    Raises:
        FileNotFoundError: If the file does not exist.
        IOError: If there's an error appending to the file.
    """
    try:
        with open(filepath, 'a') as f:
            f.write(content_to_append)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath}")
    except IOError as e:
        raise IOError(f"Error appending to file: {e}")


def create_file(filepath, initial_content=""):
    """Creates a new file with the given content.

    Args:
        filepath: Path to the new file.
        initial_content: Initial content for the file (optional).

    Raises:
        IOError: If there's an error creating the file.
    """
    try:
        with open(filepath, 'x') as f:  # 'x' mode ensures the file doesn't already exist
            f.write(initial_content)
    except FileExistsError:
        raise FileExistsError(f"File already exists: {filepath}")
    except IOError as e:
        raise IOError(f"Error creating file: {e}")


#Example Usage
file_path = "my_new_file.txt"
try:
    create_file(file_path, "This is some initial content.\n")
    append_to_file(file_path, "This is appended content.\n")
    print(f"File '{file_path}' created and updated successfully.")
except (FileNotFoundError, IOError, FileExistsError) as e:
    print(f"An error occurred: {e}")
