# -----------------------------------------------------------------------
# -------------------------string methods2-------------------------------
# -----------------------------------------------------------------------
# split(), rsplit() # split(delim, splits)  ~ if not provided then space
# center() # center(return size, filler) ~ if not provided then space
# count() # count(to count, from, to)
# swapcase()
# startswith(), endswith() # returns a boolean
# startswith(string to check, from, to)
# -----------------------------------------------------------------------

a = "this is my full name"

print(a.split())
print(a.split(" ", 2))
print(a.rsplit(" ", 2))

b = "Idress"

print(b.center(10, "~"))

c = "how many times did i say times?"

print(c.count("times"))
print(c.swapcase())

d = "Hello world"

print(d.startswith("H"))
print(d.startswith("w", 6, 11))

print(d.endswith("d"))
print(d.endswith("o", 0, 5))
