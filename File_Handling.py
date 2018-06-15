# fp = open('test.txt')
# print(fp.read())
# fp.close()

# ------------------------------------

# with open('test.txt') as fp:
#     buffer = fp.read()
# print(buffer)

# ---------------------------------------

# fp = open("test.txt")
# while True:
#     buffer = fp.readline()
#     if buffer == '':
#         break
#     print(buffer)
# fp.close()

# --------------readline()---------------------------
# Displays only those lines that contain the word

# fp = open("test.txt")
# while True:
#     buffer = fp.readline()
#     if 'methods' in buffer:
#         print(buffer)
#     if buffer == '':
#         break
# fp.close()

# --------------readlines()-----------------------------

# fp = open('test.txt')
# buffer = fp.readlines()     # Create a list of strings including \n at the end of each string
# print(buffer)
# for line in buffer:
#     print(line, end='')     # end ='', tells print that don't go to next line after each print.
# fp.close()

# ---------------------------------------------------------
# For large file you shoudn't use read() or readlines() methods,
# it may lead to memory problem. You should read a file line
# by line with the readline() method.

# fp = open('test.txt')
# count = 0
# while count < 2:
#     buffer = fp.readline()
#     if buffer == '':
#         break
#     print(buffer, end='')
#     count += 1
# fp.close()

# ---------------------------------------------------
# Count the occurence of word in a file

# fp = open('test.txt')
# word = 0
# while True:
#     buffer = fp.readline()
#     if 'methods' in buffer:
#         word += 1
#     if buffer == '':
#         break
# print(word)
# fp.close()

# -----------------writing a file--------------------------------
# fp = open('test_write.txt', 'w')
# while True:
#     text = input('Enter a line of text: ')
#     if text == '':
#         break
#     fp.write(text+'\n')
# fp.close()
#
# fp = open('test_write.txt')
# buffer = fp.read()
# fp.close()
# print(buffer)

# ------------------------------------------------------
# Copying one file contents to another

# fp = open('test.txt')
# fp_new = open('test_copy.txt', 'w')
# while True:
#     buffer = fp.readline()
#     fp_new.write(buffer)
#     if buffer == '':
#         break
# fp_new.close()
# fp.close()
# with open('test_copy.txt') as fp:
#     buffer = fp.read()
# print(buffer)

# --------------------------------------------------
# Copy the contents of file and reverse it and store the
# the new reverse text to new file

# fp = open('test.txt')
# fp_new = open('test_reverse.txt', 'w')
# while True:
#     buffer = fp.readline()
#     if buffer == '':
#         break
#     fp_new.write(buffer[::-1])      # [start:end:step]
# fp_new.close()
# fp.close()
# with open('test_reverse.txt') as fp:
#     buffer = fp.read()
# print(buffer)

# -----------------Appending a file-----------------------------------

# filename = 'test.txt'
#
# def displayContents(f):
#     fp = open(f)
#     print(fp.read())
#     fp.close()
#
# displayContents(filename)
#
# fp = open('test.txt', 'a')
# while True:
#     text = input('Enter a line of text: ')
#     if text == '':
#         break
#     fp.write(text + '\n')
# fp.close()
#
# displayContents(filename)

# -----------------os.path module----------------------------------
# exists() - gets a path as argument and return True if that path exists, otherwise False

# from os.path import exists
#
# if exists('test.txt'):
#     print('test text file exists')
# else:
#     print('test text file doesn\'t exist')

# -----------------listdir() and join()---------------------------
# from os import listdir, getcwd
# from os.path import join
#
# filelist = listdir('.')
# for name in filelist:
#     pathname = join(getcwd(), name)
#     print(pathname)

# -----------------basename()-------------------------------
# basename extracts the filename from path

# from os.path import basename
# print(basename('/home/vipu/Projects/Git/Python/test.txt'))

# -----------------dirname()-------------------------------------
# dirname, extracts the directory name from a path

# from os . path import dirname
# print ( dirname ( "/System/Home/readme .txt" ))

# -----------------getsize()------------------------------------
# getsize, gets the size of the file that is passed

# from os.path import getsize
#
# num_bytes = getsize('/home/vipul/Projects/Git/Python/test.txt')
# print(str(num_bytes)+'bytes')


# ----------------------------------------------------
# Adds up the sizes of all the files in the current directory

# from os import listdir
# from os.path import getsize
#
# filelist = listdir('.')
# totalSize = 0
# for i in filelist:
#     totalSize += getsize(i)
# print(totalSize)

