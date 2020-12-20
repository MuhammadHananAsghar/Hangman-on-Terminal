import random


def Hangman(condition):

	if condition == 'start':
		print("	-----------")
		print("	|         |")
		print("	|         |")
		print("	|")
		print("	|")
		print("	|")
		print("	|")
		print("	|")
		print("	|")
		print("	|")
		print("    ---------")

	elif condition == 'head':
		print("	-----------")
		print("	|         |")
		print("	|         |")
		print("	|         O")
		print("	|")
		print("	|")
		print("	|")
		print("	|")
		print("	|")
		print("	|")
		print("    ---------")

	elif condition == 'hands':
		print("	-----------")
		print("	|         |")
		print("	|         |")
		print("	|         O")
		print("	|        / \\")
		print("	|")
		print("	|")
		print("	|")
		print("	|")
		print("	|")
		print("    ---------")

	# elif condition == 'body':
	# 	print("	-----------")
	# 	print("	|         |")
	# 	print("	|         |")
	# 	print("	|         O")
	# 	print("	|        /|\\")
	# 	print("	|         |")
	# 	print("	|")
	# 	print("	|")
	# 	print("	|")
	# 	print("	|")
	# 	print("    ---------")

	elif condition == 'bodyandlegs':
		print("	-----------")
		print("	|         |")
		print("	|         |")
		print("	|         O")
		print("	|        /|\\")
		print("	|         |")
		print("	|        / \\")
		print("	|")
		print("	|")
		print("	|")
		print("    ---------")

	else:
		pass



if __name__ == "__main__":
	words = ["deer","dear","bear","name","goat","boat"]
	word = random.choice(words)
	print(word)
	LIST_WORDS = []
	for w in word:
		LIST_WORDS.append(w)
	length = len(LIST_WORDS)
	Hangman('start')
	line = "Guess the Word --->> "
	id = 0
	idx = len(LIST_WORDS) - len(LIST_WORDS)
	while True:
		user_input = input("Enter Word: ")
		if user_input in LIST_WORDS:
			line += LIST_WORDS[idx]
			print(line)
			idx += 1
			if idx == len(LIST_WORDS):
				print("You Won.")
				break
		else:
			try:
				conditions = ["head", "hands", "bodyandlegs"]
				Hangman(conditions[id])
				print(line)
				id += 1
			except:
				pass

		length -= 1
		print("You Have Chances {} Left.".format(length))
		if length== 0:
			print("You Hanged the Man. :(")
			Hangman("bodyandlegs")
			break

