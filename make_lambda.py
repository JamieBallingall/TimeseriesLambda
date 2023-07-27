# This script will strip out any comments, spaces or newline characters from a file
# It acts a compiler for Excel LAMBDA functions, allowing us to write more structured functions
# It was generated in nearly the form below by ChatGPT

import sys

def clean_function(input_text):
  lines = input_text.split("\n")
  processed_lines = []

  for line in lines:
    # Remove comments (lines starting with "//")
    if "//" in line:
      line = line[:line.index("//")]
    line = line.replace(" ", "") # Remove spaces
    processed_lines.append(line)

  return "".join(processed_lines)

if __name__ == "__main__":
  try:
    input_text = sys.stdin.read()               # Read from STDIN until EOF is encountered
    processed_text = clean_function(input_text) # Remove spaces, newlines, and comments
    sys.stdout.write(processed_text)            # Write the processed text to STDOUT

  except KeyboardInterrupt:
    sys.exit(0) # In case of KeyboardInterrupt (e.g., Ctrl+C), gracefully exit without errors


# import sys

# def remove_spaces_and_newlines(input_text):
#   return input_text.replace(" ", "").replace("\n", "")

# if __name__ == "__main__":
#   try:
#     # Read from STDIN until EOF is encountered
#     input_text = sys.stdin.read()

#     # Remove spaces and newlines
#     processed_text = remove_spaces_and_newlines(input_text)

#     # Write the processed text to STDOUT
#     sys.stdout.write(processed_text)

#   except KeyboardInterrupt:
#     # In case of KeyboardInterrupt (e.g., Ctrl+C), gracefully exit without errors.
#     sys.exit(0)