# f=open("student.txt",mode="r",encoding="utf-8")
# print("file object: ",f)
# print("file name: ",f.name)
# print("file mode: ",f.mode)
# print("file readable: ",f.readable())
# print("file writable: ",f.writable())
#
# f.close()
#
# print("is file closed: ",f.closed)
#
# #NOTE: you can check for all file modea1
#
# # check fil exist or not isfile()
# # for that import os module
#
# import os
# print(os.path.isfile("student.txt"))
#
# #usecase 
# #if you dont want to show file not exit error to user
#
#
#
# if os.path.isfile("student.txt"):
#     print(f.name)
# else:
#     print("file not found.") 
#

# writing file 
#---------------------
# mode w= it will create file if not exist ,if exist overwrites it 
#mode  a= append


# f=open("teacher.text",mode="w")
# f.write("Hello Sir!\n")
# f.write("How are you?\n")
# f.close()

#writelines() -> to write group of string

# f= open("student.txt",mode="w")
#
# lst=["Surya\n","kuari\n","Dolma\n","Fulmaya\n","Dristy\n","Apple"]
# f.writelines(lst)
# f.close()
# print("write success")

#note try all mode

#reading file
#--------------
# for reading file , file must exist other throws file not found error
#read(size)


# fo= open("student.txt",mode="r")
# data=fo.read()
# print(data)
# print("Completed!!")

# fo= open("student.txt",mode="r")
# data1=fo.read(2) # it will read 2 chars and cursor will be after that char
# data2=fo.read(2)# it will read chars after that cursor
# print(data1)
# print(data2)
# print("Completed!!")
# fo.close()
#
# # readline()

# fo= open("student.txt",mode="r")
# data1=fo.readline() 
# print(data1)
# print("Completed!!")
# fo.close()


# readlines()-> returns data in list form


# fo= open("student.txt",mode="r")
# data1=fo.readlines() 
# print(data1)
#
# for i in data1:
#     print(i,end="")
#
# print("Completed!!\n")
# fo.close()


# tell()-> finds the position of file pointer from the beginning of the file .starts from position 0
#syntax: file_object.tell()

# fo= open("student.txt",mode="r")
# print(fo.tell())
# data= fo.read(4)
# print(data)
# print(fo.tell())

#note : if you want to work on specific position on file 


# seek()-> used to move file pointer from one position to another
#-------------------------------------

# fo= open("student.txt",mode="r")
# print(fo.tell())
# fo.seek(7) # moves cursor from  0 to 7 position
# data= fo.read()
# print(data)

# r+ mode -> read then write
#---------------------------

# fo= open("student.txt",mode="r+")
# print(fo.tell())
# data= fo.read()
# print(fo.tell())
# fo.write("Youtube!")
# print(fo.tell())
# print(data)
#
# print(fo.tell())

# w+ mode -> write then read
#---------------------------

# fo= open("student.txt",mode="w+")
#
# fo.write("Youtube!")
#
# data= fo.read()
#
# print(data) # no result because the cursor is at last position after write , after cursor position no data
#
# fo.seek(0)# moving cursor to 0 position
# data= fo.read() # now it reads data
#
# print(data) 

# a+ mode -> append then read
#---------------------------
#in append mode file cursor will be at last of the data by default
# fo= open("student.txt",mode="w+")
#
# fo.write("Youtube!")
#
# data= fo.read()
#
# print(data) # no result because the cursor is at last position after write , after cursor position no data
#
# fo.seek(0)# moving cursor to 0 position
# data= fo.read() # now it reads data
#
# print(data) 


#copying from one file to another
#--------------------------------
# f1= open("student.txt",mode="r")
# f2= open("student1.txt",mode="w")
#
# data=f1.read()
# f2.write(data)
# f1.close()
# f2.close()

# with statement
# when open file with [with]statement no need to close the file explicitly

# with open("student.txt",mode="r") as f:
#     data= f.read()
#     print(data)
# print(f.closed) #// checking whether file is closed

import os
#checking current directory
path=os.getcwd()
print(path)
#checking if absolute path
print(os.path.isabs(path))
#checking whether relative path
print(os.path.relpath(path)) 


















