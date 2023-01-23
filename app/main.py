import sys
import os
import zlib


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    # print("Logs from your program will appear here!")

    # Uncomment this block to pass the first stage
    #
    command = sys.argv[1]
    if command == "init":
        os.mkdir(".git")
        os.mkdir(".git/objects")
        os.mkdir(".git/refs")
        with open(".git/HEAD", "w") as f:
            f.write("ref: refs/heads/master\n")
        print("Initialized git directory")
    elif command == "cat-file":
        blob_hash = sys.argv[3]
        with open(f".git/objects/{blob_hash[:2]}/{blob_hash[2:]}", "rb") as f:
            decompressed = zlib.decompress(f.read())
            decompressed = decompressed.decode("utf-8")
            decompressed = decompressed.split("\x00")
            print(decompressed[1], end="")
    else:
        raise RuntimeError(f"Unknown command #{command}")


if __name__ == "__main__":
    main()
