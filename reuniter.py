import os

# Define the directory containing the split files
input_directory = "chunkdec/"

# Define the output file
output_file = "reunited_input.txt"

# Initialize the variable to hold the content of the reunited file
reunited_content = ""

# Iterate over each file in the input directory
for filename in sorted(os.listdir(input_directory)):
    # Skip any files that are not text files
    if not filename.endswith(".txt"):
        continue
    
    # Read the content of the current file
    with open(os.path.join(input_directory, filename), "r") as file:
        content = file.read()
    
    # Append the content of the current file to the reunited content
    reunited_content += content

# Write the reunited content to the output file
with open(output_file, "w") as file:
    file.write(reunited_content)

print("Files reunited successfully.")
