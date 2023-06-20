from contextlib import contextmanager


class File:
    def __init__(self, filename, method) -> None:
        self.file = open(filename, method)

    def __enter__(self):
        print("Enter")
        return self.file

    def __exit__(self, type, value, traceback):
        print("Exit")
        print(type, value, traceback)
        self.file.close()
        if type == FileExistsError:
            return True  # Suppresses the exception


with File("sql.py", "r") as f:
    print("Middle")
    file = f.read()
    print(f"File: {len(file)} bytes")
    # raise FileExistsError()


# Using generators
@contextmanager
def file(filename, method):
    file = open(filename, method)
    yield file
    file.close()


with file("sql.py", "r") as f:
    print("Generator context manager")
    file = f.read()
    print(f"File: {len(file)} bytes")
