import hashlib
import csv

def generate_sha256_hash(input_string):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(input_string.encode('utf-8'))
    return sha256_hash.hexdigest()

# Generate SHA-256 hashes for numbers 0 to 9999
hashes = {str(number): generate_sha256_hash(str(number)) for number in range(10000)}

# Write the hashes to a CSV file
csv_filename = 'hashes.csv'
with open(csv_filename, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Number', 'SHA-256 Hash'])  # Write header
    for number, sha256_hash in hashes.items():
        csv_writer.writerow([number, sha256_hash])


print(f"Hashes written to {csv_filename}")