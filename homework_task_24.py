def group_by_surname(list_of_enrollees):
    a_i = []
    j_p = []
    q_t = []
    u_z = []
    for i in range (len(list_of_enrollees)):
        name_surname = (list_of_enrollees)[i]
        surname_first_leter_ord = ord((name_surname[0]))
        if 65 <= surname_first_leter_ord <= 73:
            a_i += [name_surname]
        if 74 <= surname_first_leter_ord <= 80:
            j_p += [name_surname]
        if 81 <= surname_first_leter_ord <= 84:
            q_t += [name_surname]
        if 85 <= surname_first_leter_ord <= 90:
            u_z += [name_surname]
    return len(a_i), len(j_p), len(q_t), len(u_z)
 #   return ((name_surname)[0])

print(group_by_surname(['Your Mom', 'Alex Soulfear', 'Hogger Gnoll', 'Katty Perry', 'Arthur Dent', 'Timmy Turner', 'Useless Rubish', 'Jimmy Newtron', 'Pinkie Pie', 'Rick Sunchess']))

