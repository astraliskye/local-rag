import os
import sys
import uuid
import chromadb


def list_files(path="."):
    result = []
    files_to_search = [os.path.join(path, f) for f in os.listdir(path)]

    while len(files_to_search) > 0:
        file = files_to_search.pop()
        if os.path.isdir(file):
            additions = [os.path.join(file, f) for f in os.listdir(file)]
            files_to_search = files_to_search + additions
        else:
            result.append(file)
    return result


if __name__ == "__main__":
    client = chromadb.PersistentClient(path="./db")
    collection = client.get_or_create_collection("docs")

    for file in sys.argv[1:]:
        for filename in list_files(file):
            with open(filename) as file:
                id = filename.split(os.sep)[-1]
                try:
                    collection.add(documents=[file.read()], ids=[str(uuid.uuid4())])
                except Exception:
                    print(f"Could not load {id}")
                else:
                    print(id)
