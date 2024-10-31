def work_school():
    my_string=["Python","Programming","language"]
    my_dictionary={}
    for x in my_string:
        my_dictionary[x]=len(x)
    return my_dictionary
do = work_school()
print( do )