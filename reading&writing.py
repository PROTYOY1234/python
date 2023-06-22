file_name=input("What is Your File Name?")
content=input("What is Your Content?")
with open('file_name','w') as file:
    file.write(content)
open_file=input("Would You Like To Open file?")
if open_file in ['y','n']:
    if open_file=='y':
     with open('file_name','r') as file:
        print(file.read())

