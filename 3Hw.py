# 1
squares = [x**2 for x in range(10)]
print(squares)
# 2
even_numbers = [x for x in range(20) if x % 2 == 0]
print(even_numbers)
# 3
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print(upper_words)
# 4
words = ["apple", "banana", "cherry"]
first_letters = [word[0] for word in words]
print(first_letters)
# 5
cubes = [x**3 for x in range(10) if x % 2 != 0]
print(cubes)
# 6
words = ["cat", "dog", "elephant"]
word_lengths = [len(word) for word in words]
print(word_lengths)
# 7
numbers = [1, 2, 3, 4, 5, 6]
result = [x if x % 2 == 0 else x*2 for x in numbers]
print(result)
