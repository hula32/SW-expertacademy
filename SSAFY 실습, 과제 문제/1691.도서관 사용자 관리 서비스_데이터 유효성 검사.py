data = {'blood_group' : 'a'}

blood_types = {'c'}


check = True
check_list = []

if data['blood_group'] not in blood_types:
    check = False
    check_list.append('blood_group')

print(check, check_list)