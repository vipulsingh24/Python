'''
“Binary files” is the term used to refer to all files that are not text files.

The handling of binary files is quite similar to the handling of text files. You have to open()
a file when you want to access its contents, close () it when you are finished, read () from
the file and write () to the file.
'''

# hw1 = "Hello, World!"
# hw2 = b"Hello, World!"
#
# for c in hw1:
#     print(c, end='')
# print()
# for c in hw1:
#     print(str(ord(c))+',', end='')
# print()
# for c in hw2:
#     print(c, end='')

# ---------------------------------------------

# bs = bytes([72 ,101 ,108 ,108 ,111 ,44 ,32 ,119 ,111 ,114 ,108 ,100 ,33])
# print(bs)
# bch = bytes([72])
# print(bch)
# wrong = bytes(72)
# print(wrong)


# --------From a byte string to regular string------

# hw1 = b"Hello , world !"
# hw2 = str( hw1 )
# print ( hw2 )  # So type casting str() doesn't work

# You have to “decode” the byte string according to a certain decoding scheme, which usually
# is "utf-8", as that is the most common Unicode format.

# hw1 = b"Hello , world !"
# hw2 = hw1.decode ( "utf -8" )
# print(hw2)
# hw3 = hw2.encode ( "utf -8" )
# print(hw3)
# bs = bytes([72 ,101 ,108 ,108 ,111 ,44 ,32 ,119 ,111 ,114 ,108 ,100 ,33])
# bs_str = bs.decode('utf-8')
# print(bs_str)

# -----------------------------------------------
# open the file “pc_rose.txt,” and read ten times ten bytes from it.

# fp = open('test.txt', 'rb')
# for i in range(10):
#     buffer = fp.read(10)
#     print(buffer)
# fp.close()

# -------------Writing to a binary file---------------------

from os.path import getsize

# filename = 'test_binary.txt'
# fp = open(filename, 'wb')
# fp.write(b"And now for something completely different ...\ x0A\
# \x00\x00\x00\x00\xD4\xE8\xE5\xA0\xD3\xF0\xE1\xEE\xE9\xF3\xE8\xA0\
# \xC9\xEE\xF1\xF5\xE9\xF3\xE9\xF4\xE9\xEF\xEE\x00\x00\x00")
# fp.close()
# print(getsize(filename), 'bytes written')

# fp = open(filename, encoding='latin-1')
# while True:
#     buffer = fp.readline()
#     if buffer == '':
#         break
#     print(buffer)
# fp.close()

# ----------Positioning the file pointer---------
'''
The seek () method is particularly useful when you open a file in “reading and writing”
mode ("r+b"). It allows you to move through the file, reading where you need to read, and
(over)writing where you need to (over)write.
'''

# fp = open( "test_binary.txt", "rb" )
# print ( "1. Current position of the file pointer is", fp . tell () )
# fp . seek ( 50 )
# print ( "2. Current position of the file pointer is", fp . tell () )
# buffer = fp . read ( 23 )
# print ( "3. Current position of the file pointer is", fp . tell () )
# fp . close ()
# print ( buffer )
# s = ""
# for c in buffer :
#     s += chr(c-128)
# print ( "The secret words are:", s )