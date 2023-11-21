# ------------------------------------------------------------------------
# -------------------------string-methods-3-------------------------------
# ------------------------------------------------------------------------
# index(), find() # index(to find, start, end) - index returns with an er-
# ror if not found while find returns -1
# rjust(), bjust() # rjust(returns width, filler)
# splitlines()
# expandtabs() # expandtabs(tab size)
# istitle(), isspace(), islower(), isupper(), isalpha(), isalnum() #bool
# ------------------------------------------------------------------------

a = "i love python"

print(a.index("v"))
print(a.find("z"))

b = "Idress"

print(b.rjust(10))

c = """
First
Second
Third
"""

print(c.splitlines())
print(c.split("\n"))

d = "Hi\tit's\tme"

print(d.expandtabs(10))
