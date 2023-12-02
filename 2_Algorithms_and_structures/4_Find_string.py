str_where = 'hello world'
str_find = ' wor'

ind_where = 0
ind_find = 0
len_where = len(str_where)
len_find = len(str_find)

while ind_where <= len_where - len_find and ind_find < len_find:
    if str_where[ind_where + ind_find] == str_find[ind_find]:
        ind_find += 1
    else:
        ind_where += 1
        ind_find + 0

print(f"'{str_where}'")

if ind_find == len_find:
    print(f"The string '{str_find}' is found at index {ind_where}")
else:
    print(f"The string '{str_find}' is not found'")
