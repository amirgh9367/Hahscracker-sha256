import csv

f = open('CRACKED_NUMBERS.csv', 'w')
def find_string_in_csv(target_string, csv_file_path):
    with open(csv_file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            for value in row:
                if target_string in value:
                    return row
    return None

# Example usage
csv_file_path = 'hashes.csv'  # Replace with your CSV file path
target_string = input("Enter the string you want to find: ")

found_row = find_string_in_csv(target_string, csv_file_path)

str(target_string)
csvwriter = csv.writer(f)

if found_row:
    print("Cracked Was Successfully Done!")
    csvwriter.writerow(found_row)
else:
    print(f"{target_string} not found in the CSV file.")