import re
import json

# Function to generate spiral coordinates
def spiral():
    x=y=0
    dx = 0
    dy = -1
    while True:
        yield (x, y)
        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
            dx, dy = -dy, dx
        x, y = x+dx, y+dy

# Read the central_ledger.txt file
with open("central_ledger.txt", "r") as file:
    central_ledger = file.read()

# Parse the ledger entries
ledger_entries = central_ledger.strip().split("\n\n")
ledger_data = []

for entry in ledger_entries:
    entry_dict = {}
    entry_dict["identifier"] = re.search(r"Fractal Identifier: (.*)", entry).group(1)
    entry_dict["png_file"] = re.search(r"Fractal PNG: (.*)", entry).group(1)
    entry_dict["svg_file"] = re.search(r"Fractal SVG: (.*)", entry).group(1)
    entry_dict["text_file"] = re.search(r"Decoded Text: (.*)", entry).group(1)
    entry_dict["fractal_text"] = re.search(r"BEGIN '.*' fractal of the text\n(.*)\nEND '.*' fractal of the text", entry, re.DOTALL).group(1)
    ledger_data.append(entry_dict)

# Assign coordinates to each ledger entry
spiral_generator = spiral()
for entry in ledger_data:
    entry["coordinates"] = next(spiral_generator)

# Convert the ledger data to JSON
ledger_json = json.dumps(ledger_data, indent=4)

# Write the JSON data to a file
with open("ledger.json", "w") as file:
    file.write(ledger_json)
