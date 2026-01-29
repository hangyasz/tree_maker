import sys
import csv

# Building the tree structure
def build_tree(paths):
    tree = {}
    for path in sorted(paths):
        parts = path.strip('/').split('/')
        current = tree
        for part in parts:
            if part not in current:
                current[part] = {}
            current = current[part]
        # Csak a legvégén, a teljes path végénél biztosítjuk az 'items' listát
        if 'items' not in current:
            current['items'] = []
    return tree

#Adding items to the tree
def add_items_to_tree(tree, rows):
    for item in rows:
        # only add items that are not of type 'Mappa'
        if item.get('Item Type') != 'Mappa':
            parts = item['Path'].strip('/').split('/')
            current = tree
            for part in parts:
                if part not in current:
                    current[part] = {}
                current = current[part]
            # Add the item to the 'items' list   
            if 'items' not in current:
                current['items'] = []
            current['items'].append(item['Name'])

# Printing the tree structure
def print_tree(node, indent=0):
    for key, value in node.items():
        # Write the items in the 'items' list
        if key == 'items':
            for item in value:
                print('  ' * indent + f'- {item}')
        else:
            print('  ' * indent + f'{key}/')
            print_tree(value, indent + 1)

# Main script execution
if len(sys.argv) < 3:
        print("Usage: python script.py <csv_file> <output_file>")
        sys.exit(1)

csv_file = sys.argv[1]
# Ensure the input file is a .csv file
if not csv_file.endswith('.csv'):
    print("Error: The input file must be a .csv file")
    sys.exit(1)

file_path = sys.argv[2]
# Ensure the output file has a .txt extension
if not file_path.endswith('.txt'):
    print("Error: The output file must be a .txt file")
    sys.exit(1)

# Read CSV and collect paths and rows
rows = []
paths = set()

try:
    with open(csv_file, mode='r', encoding='utf-8-sig', newline='') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                rows.append(row)
                paths.add(row['Path'])
except FileNotFoundError:
    print(f"Error: The file {csv_file} was not found.")
    sys.exit(1)                
except Exception as e:
    print(f"Error {e}")
    sys.exit(1)


tree = build_tree(paths)
add_items_to_tree(tree, rows)

# Write the tree structure to the output file
try:
    with open(file_path, 'w', encoding='utf-8') as f:
        sys.stdout = f  # Redirect standard output to the file
        print_tree(tree)
        sys.stdout = sys.__stdout__  # Restore standard output
except Exception as e:
    print(f"Error writing to file {file_path}: {e}")
    sys.exit(1)