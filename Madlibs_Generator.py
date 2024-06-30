# This opens the file story.txt.
with open("story.txt", "r") as s:
    story = s.read()

# Find words in parentheses
words = set()
beginning_of_word = -1

start_target = "("
end_target = ")"

for i, char in enumerate(story):
    if char == start_target:
        beginning_of_word = i

    if char == end_target and beginning_of_word != -1:
        word = story[beginning_of_word: i + 1]
        words.add(word)
        beginning_of_word = -1

# Get replacements
answers = {}

for word in words:
    answer = input("Enter a word " + word + ": ")
    answers[word] = answer

# Replacing words in the story
for word in words:
    story = story.replace(word, answers[word])

print(story)
