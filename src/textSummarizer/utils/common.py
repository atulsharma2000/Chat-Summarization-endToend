# instead of writting same component again and again , just create this frequently used component once and use them in your code.
# a common.py file within a utils folder is essential for promoting code reusability, enhancing project organization, simplifying imports, facilitating collaboration among team members, and allowing for easy refactoring. These benefits contribute to more maintainable and scalable codebases.

import os
from box.exceptions import BoxValueError  # Import BoxValueError for handling specific exceptions from the Box library
import yaml  # Import the yaml library for reading and writing YAML files
from textSummarizer.logging import logger  # Import a custom logger for logging messages in your application
from ensure import ensure_annotations  # Import a decorator to ensure function annotations are checked at runtime
from box import ConfigBox  # Import ConfigBox, a convenient way to handle configuration data
from pathlib import Path  # Import Path for object-oriented filesystem paths
from typing import List  # Import List for type hinting

@ensure_annotations  # Decorator to ensure that function annotations are enforced
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a YAML file and returns its contents as a ConfigBox.
    
    Args:
        path_to_yaml (Path): Path to the YAML file.
    
    Raises:
        ValueError: If the YAML file is empty.
    
    Returns:
        ConfigBox: Parsed contents of the YAML file.
    """
    try:
        # Open the specified YAML file in read mode
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)  # Load the YAML content safely into a Python object
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")  # Log a success message
            return ConfigBox(content)  # Return the loaded content wrapped in a ConfigBox for easier access
    except BoxValueError:
        # If the Box library raises a BoxValueError, it indicates that the YAML file is empty
        raise ValueError(f"YAML file: {path_to_yaml} is empty")  # Raise a ValueError with an informative message
    except Exception as e:
        # For any other exceptions, log the error and re-raise it for further handling upstream
        logger.error(f"Failed to read YAML file at {path_to_yaml}: {e}")  # Log an error message with details
        raise e  # Re-raise the exception

@ensure_annotations  # Decorator to ensure that function annotations are enforced
def create_directories(path_to_directories: List[Path], verbose=True):
    """Creates a list of directories.

    Args:
        path_to_directories (List[Path]): List of paths for directories to create.
        verbose (bool, optional): If True, log directory creation. Defaults to True.
    """
    for path in path_to_directories:  # Iterate over each path in the provided list
        os.makedirs(path, exist_ok=True)  # Create the directory if it doesn't exist; ignore if it does
        if verbose:  # If verbose logging is enabled
            logger.info(f"Created directory at: {path}")  # Log a message indicating that the directory was created

@ensure_annotations  # Decorator to ensure that function annotations are enforced
def get_size(path: Path) -> str:
    """Gets the size of a file in kilobytes.

    Args:
        path (Path): Path of the file.

    Returns:
        str: Size of the file in KB.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)  # Get the size of the file in bytes and convert it to kilobytes
    return f"~ {size_in_kb} KB"  # Return the size formatted as a string indicating kilobytes