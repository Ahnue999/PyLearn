# ------------------------------------------------------------------------
# -------------------------string-formatting------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------

name = "Mohamed"
age = 19
grade = 86.6

print("My name is %s\nMy age is %d\nMy grade is %.2f" % (name, age, grade))
print("%.5s" % name)

print("My name is {}\nMy age is {:d}\nMy grade is {:.2f}".format(name, age, grade))
print(f"My name is {name}\nMy age is {age}\nMy grade is {grade}")

a, b, c = 0, 1, 2

print("{2}, {1}, {0}".format(a, b, c))

print("{:.3f}".format(10 / 3))
print(10 // 3)
