import os
import re

def files_are_equal(file1, file2):
  # Check if both files exist
  if not os.path.isfile(file1):
    print(f"File '{file1}' does not exist.")
    return False
  if not os.path.isfile(file2):
    print(f"File '{file2}' does not exist.")
    return False
    
  with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
    content_1 = f1.read().decode('utf-8')
    content_2 = f2.read().decode('utf-8')
    # content_1.split('\n',)
    docid_1 = re.split(r'[\n,]', content_1)
    docid_2 = re.split(r'[\n,]', content_2)
    docid_1 = [s for s in docid_1 if s]
    docid_2 = [s for s in docid_2 if s]
    docid_1 = sorted(docid_1)
    docid_2 = sorted(docid_2)
    print(docid_1)
    print(docid_2)
    set1 = set(docid_1)
    set2 = set(docid_2)
    for doc in docid_1:
      if doc not in set2:
        print(doc, " lost in f2")
    for doc in docid_2:
      if doc not in set1:
        print(doc, " lost in f1")
# Example usage
file1 = 'left'
file2 = 'right'

# file1 = 'left_recall'
# file2 = 'right_recall'

files_are_equal(file1, file2)