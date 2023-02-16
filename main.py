# 6
# with open('file1.txt', 'w+') as file1:
#     while True:
#         word = input('enter a word : ')
#         if word == 'exit':
#             break
#         file1.write(f'{word} \n')
#
#     file1.seek(0)
#     print(file1.read())

# 7

# def sum_number(file_name):
#     file2 = open(file_name, 'r+')
#     sum = 0
#     for line in file2.readlines():
#         try:
#             sum += int(line)
#         except:
#             print('sh*t   this line is dang...')
#             continue
#     file2.write(f'\n{sum}')
#     file2.close()
#
#
# f = input('please enter the full path of the file :')
# sum_number(f)

# def find_my_guess(file_name, guess):
#     file3 = open(file_name, 'r')
#     return guess in file3.read().lower()
#
# f = input('enter file name :')
# g = input('enter file word :')
#
# i = find_my_guess(f, g)
#
# print(i)


#9


# def copy_file(source, target):
#     source_file = open(source, 'r')
#     target_file = open(target, 'w')
#
#     target_file.write( source_file.read()[::-1] )
#
#     source_file.close()
#     target_file.close()
#
#
# source = input('from this file :  ')
# target = input('to this file :')
# copy_file(source,target)




# try:
#     x = open('file55.txt', 'r')
#
# except FileNotFoundError:
#     print('file not fount')
#
# except FileExistsError:
#     print('try another name ')
#
# except:
#     pass
#
# finally:
#     x.close()


x=6
x='hello'
