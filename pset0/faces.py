def convert(string):
#    if ":)" in string:
#        string = string.replace(":)", "🙂")
#    if ":(" in string:
#        string = string.replace(":(", "🙁")
    print(string.replace(":)", "🙂").replace(":(", "🙁").encode("utf-8"))

def main():
    answer = input("a string please:\n")
    convert(answer)



main()
