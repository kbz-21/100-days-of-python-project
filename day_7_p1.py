import random
word_list = ["kaleab", "zewdie", "bogale", "Maico", "tilahun"]
word = random.choice(word_list)
print(word)

guess = input("Guess the Letter: ").lower()
print(guess)


for letter in word:
    if guess==letter:
        print("Right")
    else:
        print("Wrong")