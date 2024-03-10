def add_nots(tests):
    #split a string into multiple letters
    splitTest = list(tests)
    print(splitTest)

    #add '.' after each letter
    finalWord = " "
    for i in splitTest:
        finalWord = finalWord + i + "."
    print(finalWord)

add_nots("python")