def get_extesion(file_name):
    file_name_splitted = file_name.split('.')
    if len(file_name_splitted) > 1 and (not file_name_splitted[-1] == ''):
        print("Extension:",file_name_splitted[-1])
    else:
        print("File name:", file_name, "is not correct")



get_extesion("myasdasd")
print(type(get_extesion))