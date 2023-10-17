import os

def process_gcode(filename):
    input_filepath = os.path.join("input", filename)
    output_filepath = os.path.join("output", filename)

    if not os.path.exists(input_filepath):
        print(f"Error: {input_filepath} does not exist!")
        return

    with open(input_filepath, 'r') as f:
        lines = f.readlines()

    with open(output_filepath, 'w') as f:
        for line in lines:
            stripped_line = line.strip()

            # If the line is just 'G92' or starts with 'G92 ' and doesn't have any XYZ coordinates, skip it
            if stripped_line == "G92" or (stripped_line.startswith("G92 ") and not any(axis in stripped_line for axis in ["X", "Y", "Z"])):
                continue

            # Split the line into parts by space
            parts = line.split()

            # Remove any part that starts with 'E'
            parts = [part for part in parts if not part.startswith('E')]

            # Join the parts back together and write to the output file
            f.write(' '.join(parts) + '\n')

    print(f"Processed file saved to {output_filepath}")

if __name__ == "__main__":
    if not os.path.exists("input"):
        os.makedirs("input")
        print("Created 'input' folder. Please place your G-code files in this folder.")
    if not os.path.exists("output"):
        os.makedirs("output")
        print("Processed files will be saved to the 'output' folder.")

    filename = input("Enter the filename of the G-code file located in the 'input' folder: ").strip()
    process_gcode(filename)