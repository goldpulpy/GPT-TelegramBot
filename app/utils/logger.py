from datetime import datetime
from pathlib import Path


class Logger:
    """
    A simple Logger class that writes log messages to a file and prints them.

    Attributes:
        output_file (str): The file path for the log file where messages will be written.
    """

    def __init__(self, output_file: str = "logs.txt") -> None:
        """
        Initializes the Logger instance with the provided output file.

        Args:
            output_file (str): The file path for the log file. Defaults to "logs.txt".
        """
        self.output_file: str = output_file
        
    def log(self, message: str = "", is_start: bool = False) -> None:
        """
        Writes a log message to the output file and prints it to the console.

        The message is prefixed with a timestamp. If 'is_start' is True, the message
        is also prefixed and suffixed with a newline character, to set it apart in the log file.

        Args:
            message (str): The log message to be written. Defaults to an empty string.
            is_start (bool): Whether the log message is the start of a new section. Defaults to False.
        """
        # Get the current timestamp in the specified format
        timestamp = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        # Format the log entry with or without newlines based on 'is_start'
        log_entry = f"\n{timestamp} - {message}\n" if is_start else f"{timestamp} - {message}\n"
        # Open the log file in append mode and write the log entry
        with open(self.output_file, 'a') as file:
            file.write(log_entry)
        # Print the log entry to the console, stripping any leading/trailing whitespace
        print(log_entry.strip())