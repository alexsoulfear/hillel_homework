def group_by_surname(list_of_enrollees):
    a_i = []
    j_p = []
    q_t = []
    u_z = []
     for i in range (len(list_of_enrollees)):
        name_surname = (list_of_enrollees)[i]
        first_letter = name_surname[0]
        if 'A' <= first_letter <= 'I':
            a_i += [name_surname]
        if 'J' <= first_letter <= 'P':
            j_p += [name_surname]
        if 'Q' <= first_letter <= 'T':
            q_t += [name_surname]
        if 'U' <= first_letter <= 'Z':
            u_z += [name_surname]
    return len(a_i), len(j_p), len(q_t), len(u_z)
 #   return ((name_surname)[0])

print(group_by_surname(['Your Mom', 'Alex Soulfear', 'Hogger Gnoll', 'Katty Perry', 'Arthur Dent', 'Timmy Turner', 'Useless Rubish', 'Jimmy Newtron', 'Pinkie Pie', 'Rick Sunchess']))

