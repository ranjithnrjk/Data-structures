def read_large_file(file_path, batch_size=1024):
    with open(file_path, 'r') as file:
        batch = []
        for line in file:
            batch.append(line)
            if len(batch) == batch_size:
                yield batch.copy()
                batch.clear()
        if batch:
            yield batch


file_path = 'file.txt'
for batch in read_large_file(file_path, batch_size=100):
    print(batch)

