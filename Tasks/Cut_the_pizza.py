def start_end_index():
    print("Provide a start and end index to cut the pizza: ")
    start = int(input("Give the start index: "))
    end = int(input("Give the end index: "))
    return start,end

def new_word(word):
    start, end = start_end_index()
    newWord = ""
    for index in range(start, end + 1):
        letter = word[index]
        newWord += letter
    return f"word: [ {start} : {end} ]  -> {newWord}"




# Main

word = "pizza"
print("""
                  Pattern

index ->    0   1   2   3   4   5
            +---+---+---+---+---+
            | p | i | z | z | a |
            +---+---+---+---+---+
index ->   -5  -4  -3  -2  -1    

""")

print(new_word(word))