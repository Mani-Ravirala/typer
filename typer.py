import time
import pyautogui

# Function to read the text file and type its contents
def type_paragraph_from_file(file_path, typing_speed=0.01):
    with open(file_path, 'r') as file:
        content = file.read()

    # Give some time to switch to the text input field
    time.sleep(5)

    # Type out the content character by character with a delay
    for char in content:
        pyautogui.typewrite(char, interval=typing_speed)

# Replace 'path/to/your/file/input.txt' with the actual path to your text file
file_path = r"your_input_path"

# Call the function to type the paragraph from the file
type_paragraph_from_file(file_path)
