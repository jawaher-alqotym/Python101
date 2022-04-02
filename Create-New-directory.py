import os

# Make a new folder named 'Data' in pythonProject folder...
os.makedirs('Data')

# Make a new file, x -> create
f = open('Data/Test-data', 'x')

# append into the new file, 'a' -> is for append -> اكتبي داخل الملف
open('Data/Test-data', 'a').write('Hello world!\n I am jawaher')



# delete file
# os.remove('Data/Test-data')

# Read and print from a file
f = open('Data/Test-data', 'r')
print(f.read())



# Always remember to close the file
f.close()