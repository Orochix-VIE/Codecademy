# Hier ging es darum Noten und Schulfächer mittles append und remove zu organisieren in Listen. Einmal in einer normalen liste und in einer 2D Liste

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]



gradebook.append(["computersience",100])

gradebook.append(["visual arts", 93])
gradebook [-1][1] = 98
gradebook.remove(["poetry",85])
gradebook.append(["poetry", "Pass"])


full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook)

