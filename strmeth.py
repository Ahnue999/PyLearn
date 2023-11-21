# -------------------
# string methods.
# strip(), lstrip() and rstrip()
# title(), capitalize(), upper(), lower()
# zfill()
# -------------------

a = "!**Hello world***"

print(a.strip("*"))
print(a.strip("*!"))

b = "i don't Like 3d games"

print(b.title())
print(b.capitalize())
print(b.upper())
print(b.lower())

a, b, c, d = "8", "86", "240", "aw"

print(a.zfill(3))
print(b.zfill(3))
print(c.zfill(3))
print(d.zfill(3))
