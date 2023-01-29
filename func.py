def function():
    string=input("enter string")
    print("The input string is:", string)
    mySet = set(string)
    for element in mySet:
        countOfChar = 0
        for character in string:
            if character == element:
                countOfChar += 1
        print("Count of character '{}' is {}".format(element, countOfChar))
function()
