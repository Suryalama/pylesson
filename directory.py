import os

#getcwd -> to know current working directory
print(os.getcwd())

# os.mkdir()-> to create directory
#os.mkdir("mydir")# to create child directory parent must exist

#os.makedirs("parentdir/childdir/granddir") # it will create as well child folder at the same time

#os.chdir('mydir')  # change the working directory

# os.renames(old, new) # renames the directory 
#os.rmdir('directory_name') # removes the directory
#os.rmdir('parentdirectory/childdirectory') # removes the child directory
# os.removedirs(name) # removes directory with child directories

# os.walk(path,topdown=True,onerror=None,followlinks=False)
# os.walk()-> used to know contents of a directory including sub directory.

# w= os.walk('.') #  dot(.) represents current path (directory)
#
# for i in w:
#     print(i)















