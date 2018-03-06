info_str = "Leo Tolstoy*1828-08-28*1910-11-20"
info_spl = info_str.split("*")
name = (info_spl[0])
birth = (info_spl[1])
death = (info_spl [2])
birth_spl = birth.split("-")
death_spl = death.split("-")
lived_for = (int(death_spl[0])) - (int(birth_spl[0]))
print(name, lived_for)