# unicode_str = "\u66f4\u591a\u672c\u5730\u751f\u6d3b\u670d\u52a1"

# # decoded_str = unicode_str.encode("utf-8").decode("unicode_escape")
# print(unicode_str)

# def convert(octal_str):
#     byte_str = bytes(octal_str, "utf-8")

#     # Replace double backslashes with single backslashes
#     byte_str = byte_str.replace(b"\\\\", b"\\")

#     # Decode the byte string
#     chinese_str = byte_str.decode("unicode_escape")
#     return chinese_str

# with open('file') as f:
#     while 1:
#         linedata = f.readline()
#         if (not linedata):
#             break
#         res = linedata # convert(linedata)
#         print(res)
import codecs
# encoded_string = "\350\207\252\344\271\240\345\256\244"
# decoded_string = codecs.decode(encoded_string, "unicode_escape")
# print(decoded_string)

# encoded_string = "\350\207\252\344\271\240\345\256\244"
# # Replace '\' with '\x'
# encoded_string = encoded_string.replace('\\', '\\x')

# # Remove the first two characters ('\x')
# encoded_string = encoded_string[2:]

# # Convert the hex string to bytes and decode it
# decoded_string = bytes.fromhex(encoded_string).decode('utf-8')

# print(decoded_string)

string = "\350\207\252\344\271\240\345\256\244"
string = "\347\262\276\351\200\211\347\225\231\350\250\20050+"
string = "\345\237\272\345\261\202\347\273\204\347\273\207\350\207\252\346\262\273\346\263\225"
string = "\345\270\225\350\220\250\347\211\271"

chinese_string = string.encode("latin1").decode("utf-8")
print(chinese_string)