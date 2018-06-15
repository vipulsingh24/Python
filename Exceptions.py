# num = int(input('Enter a number: '))
# print('3 divided by {} is {}'.format(num, 3/num))
# print('GoodBye!')

# -------------------------------------
# num = int(input('Enter a number: '))
# if num == 0:
#     print("Dividing by zero is not allowed.")
# else:
#     print('3 divided by {} is {}'.format(num, 3 / num))
# print('GoodBye!')

# --------------Exception Handling-------------------

# num = int(input('Enter a number: '))
# try:
#     print('3 divided by {} is {}'.format(num, 3 / num))
# except:
#     print("Dividing by zero is not allowed.")
# print('GoodBye!')

# ----------------------------------------
# Multiple Statements in try-except block

# num = int(input('Enter a number: '))
# try:
#     print('3 divided by {} is {}'.format(num, 3 / num))
#     print('3 divided by {}-3 is {}'.format(num, 3 / (num-3)))
# except:
#     print('Division by zero is not allowed.')
# print('GoodBye!')

# --------------------------------------

# num = int(input('Enter a number: '))
# try:
#     print('3 / {} = {}'.format(num, 3/num))
# except ZeroDivisionError:
#     print('Dividing by zero is not allowed.')
# except ValueError:
#     print('You have not entered an integer')
# print('GoodBye!')

# ------------------------------------------

# fruitlist = ['apple', 'banana', 'cherry']
# try:
#     num = input('Enter a number: ')
#     if '.' in num:
#         num = float(num)
#     else:
#         num = int(num)
#     print(fruitlist[num])
# except IndexError:
#     print('Index out of range.')
# except ValueError:
#     print('You have not entered an integer.')
# except TypeError:
#     print('Index can\'t be in float')
# except:
#     print('Something else went wrong.')

# ---------------else-----------------------

# try:
#     num = 3 / int(input('Enter a number: '))
# except ZeroDivisionError:
#     print('Division by zero is not allowed.')
# except ValueError:
#     print('You have not entered an integer.')
# except:
#     print('Something went wrong')
# else:
#     print(num)
# print('GoodBye!')

# ---------------finally----------------------

# try:
#     fp = open('test.txt')
#     print('File Opened.')
#     print(fp.read())
# finally:
#     fp.close()
#     print('File Closed.')

# ---------------exception arguments-----------------
# The variable will always have a tuple of arguments (even if there is only one), that were
# provided to the exception when it was raised.

# try:
#     print(int('NotAnInteger'))
# except ValueError as ex:
#     print(ex.args)

# try:
#     fp = open('NotAFile')
#     fp.close()
# except IOError as ex:
#     print(ex.args)

# ---------------------------------------------

# import errno
#
# try:
#     fp = open('NotAFile')
#     fp.close()
# except IOError as ex:
#     if ex.args[0] == errno.ENOENT:
#         print('File not Found')
#     else:
#         print(ex.args[0], ex.args[1])

# ---------------raising exceptions-------------------

# def getStringLenMax10(prompt):
#     s = input(prompt)
#     if len(s) > 10:
#         raise ValueError('Length exceeds 10', len(s))
#     return s
#
# print(getStringLenMax10("Use 10 character or less: "))

# -------------------------------------------

# fp = open('nofile.txt')
# try:
#     buffer = fp.read()
#     print(buffer)
# except IOError:
#     fp.close()
#     raise
# fp.close()