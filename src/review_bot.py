import os
import io
from contextlib import redirect_stdout
from pylint import lint

class CodeReviewBot:
    def __init__(self):
        self.file_path = ""
        self.messages = ""

    def review_code(self):
        if not self.file_path:
            return "No file selected."

        # Create StringIO objects to capture stdout and stderr
        stdout = io.StringIO()

        # Redirect Pylint's output to our StringIO object
        with redirect_stdout(stdout):
            # Run Pylint
            lint.Run([self.file_path], exit=False)

        # Retrieve the captured messages
        self.messages = stdout.getvalue()

        if self.messages:
            formatted_messages = self.format_messages(self.messages)
            return formatted_messages
        else:
            return "No formatting issues found."

    def format_messages(self, messages):
        formatted_messages = ""
        for line in messages.split('\n'):
            if ":" in line:
                parts = line.split(':')
                if len(parts) >= 3:
                    error_code = parts[2].strip()
                    error_description = self.map_error_code(error_code)
                    formatted_messages += f"{parts[0]}: {parts[1]}: {error_description}\n"
                else:
                    formatted_messages += line + '\n'
            else:
                formatted_messages += line + '\n'
        return formatted_messages

    def map_error_code(self, error_code):
        error_map = {
            "C0103": "Module or variable name does not conform to snake_case naming style",
            "C0111": "Missing function docstring",
            "C0112": "Empty docstring",
            "C0114": "Missing description of code",
            "C0115": "Missing class docstring",
            "C0116": "Missing method docstring",
            "C0301": "Line too long",
            "C0302": "Too many lines in module",
            "C0303": "Trailing whitespace",
            "C0325": "Superfluous parentheses",
            "E1101": "Attribute {0} undefined",
            "E1136": "Value {0} is unsubscriptable",
            "E9999": "Internal error",
            # Add more error codes and descriptions as needed
        }
        return error_map.get(error_code, "Unknown error")


    def select_file(self, file_path):
        self.file_path = file_path
        if self.file_path:
            return "File selected: {}".format(os.path.basename(self.file_path))
        else:
            return "No file selected."
