import os

def files_are_equal(file1, file2):
    # Check if both files exist
    if not os.path.isfile(file1):
        print(f"File '{file1}' does not exist.")
        return False
    if not os.path.isfile(file2):
        print(f"File '{file2}' does not exist.")
        return False

    # Compare file sizes first for a quick check
    # if os.path.getsize(file1) != os.path.getsize(file2):
    #     return False

    chunk_size = 16
    # Compare file contents
    line_number = 1
    with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
        while True:
            # Read chunks of data
            chunk1 = f1.read(chunk_size)
            chunk2 = f2.read(chunk_size)
            # if chunk1 != chunk2:
            #     return False
            # if not chunk1:  # End of file
            #     break

            # Read chunks of data
            # chunk1 = f1.readline()
            # chunk2 = f2.readline()
            if chunk1 != chunk2:
                print('line_number: ', line_number)
                print('left:')
                print(chunk1)
                print('right:')
                print(chunk2)
                return False
            if not chunk1:  # End of file
                break
            line_number += 1

    return True

# Example usage
file1 = 'left'
file2 = 'right'

# file1 = 'left_recall'
# file2 = 'right_recall'

if files_are_equal(file1, file2):
    print("The files have the same content.")
else:
    print("The files do not have the same content.")