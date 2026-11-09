import hashlib


def generate_file_hashes(*file_paths):
    file_hashes = {}
    for file_path in file_paths:
        try:
            with open(file_path, 'rb') as mi_file:
                content = mi_file.read()
                file_content_hash = hashlib.sha256(content).hexdigest()
                file_hashes[file_path] = file_content_hash

        except FileNotFoundError:
            print(f"File {file_path} not found")
        except IOError:
            print("Error reading file")
    return file_hashes

result = generate_file_hashes("apache_logs.txt", "yakyis_file.txt")
print("РЕЗУЛЬТАТ:\n", result)
