def read_file(filepath):
    with open(filepath, "r") as f:
        return f.read().strip()


def write_output(data):
    print(data)