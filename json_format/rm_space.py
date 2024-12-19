with open("content_with_space") as f:
  content = f.read()
  content = content.replace(" ", "").replace("\n", "")
  print(content)