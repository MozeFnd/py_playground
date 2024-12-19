byte_values = [229,183,165,229,133,183,230,156,141,229,138,161,95,229,133,182,228,187,150]

# Convert the list of integers to a bytes object
byte_array = bytes(byte_values)

# Decode the bytes using GBK encoding
decoded_string = byte_array.decode('utf-8')

# Print the result
print(decoded_string)