sentences = []

n = int(input("How many sentences do you want to enter? "))

for i in range(n):
    sentence = input(f"Enter sentence {i + 1}: ")
    sentences.append(sentence)

result = " ".join(sentences)

print("\nConcatenated sentences:")
print(result)