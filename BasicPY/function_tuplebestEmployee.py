def STAR(employe_list):
    current = 0
    top_employee = ''

    for employee, hours in employe_list:
        if hours > current:
            current = hours
            top_employee = employee

    return (top_employee, current)

employe_list = [('john',100), ('aisha',200), ('cassie', 199)]
result = STAR(employe_list)
print(result)
