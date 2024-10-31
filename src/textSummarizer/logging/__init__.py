import os
import sys
import logging  # Import the logging module to enable logging in your application

# Define the format for log messages
# This format includes the timestamp, log level, module name, and the actual log message
logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"

# Specify the directory where log files will be stored
log_dir = "logs"  # This will create a folder named 'logs' in your project directory

# Construct the full path for the log file by joining the log directory and log file name
log_filepath = os.path.join(log_dir, "running_logs.log")

# Create the log directory if it doesn't already exist
# The 'exist_ok=True' parameter prevents an error if the directory already exists
os.makedirs(log_dir, exist_ok=True)

# Set up the basic configuration for logging
logging.basicConfig(
    level=logging.INFO,  # Set the minimum logging level to INFO (captures INFO, WARNING, ERROR, CRITICAL)
    format=logging_str,  # Use the defined format for log messages
    handlers=[  # Define where to send log messages
        logging.FileHandler(log_filepath),  # Log messages will be written to a file
        logging.StreamHandler(sys.stdout)    # Log messages will also be printed to the console (standard output)
    ]
)

# Create a logger object with a specific name for this application/module
logger = logging.getLogger("textSummarizerLogger")

# Optional: Log an initial message indicating that logging has started
# This can help confirm that your logging setup is working correctly when you run your code
logger.info("Logging has started.")