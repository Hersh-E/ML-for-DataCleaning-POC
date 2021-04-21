

# Pure Python implementation of CompGED

def compged(string1, string2, even_space = True, debug = False):

	cost = 0
	output = ''
	pointer1 = 0
	pointer2 = 0
	exit = False
	iter = 0
	while True:
		iter += 1
		# exit if both strings are exhausted
		if pointer1 >= len(string1) and pointer2 >= len(string2):
			# if debug:
			# 	print('done')
			exit = True
		# Append
		elif pointer2 >= len(string2):
			if debug:
				print('append')
			output = output + string1[pointer1:]
			cost += 50 * len(string1[pointer1:])
			pointer1 += 0
			pointer2 += 0
			exit = True
		# Truncate - Exits
		elif pointer1 >= len(string1):
			if debug :
				print('truncate')
			output = output + ''
			cost += 10 * len(string2[pointer2:])
			pointer1 += 0
			pointer2 += 0
			exit = True
		# Match
		elif string1[pointer1] == string2[pointer2]:
			# if debug:
			# 	print('match')
			output = output + string2[pointer2]
			cost += 0
			pointer1 += 1
			pointer2 += 1
		# Blanks
		elif string1[pointer1] == ' ':
			if debug:
				print('blank1')

			if even_space:
				while True:
					if not(string2[pointer2].isdigit() or string2[pointer2].isalpha()):
						if debug:
							print('punctuation')
						cost += 30
					else:
						if debug:
							print('delete')
						cost += 100
					pointer2 += 1
					if pointer2 >= len(string2) or string2[pointer2] == ' ':
						break
			else:
				output = output + string1[pointer1]
				cost += 10
				pointer1 += 1
				pointer2 += 0

		elif string2[pointer2] == ' ':
			if debug:
				print('blank2')
			if even_space:
				while True:
					if not(string1[pointer1].isdigit() or string1[pointer1].isalpha()):
						if debug:
							print('punctuation')
						cost += 30
					else:
						if debug:
							print('insert')
						cost += 100
					pointer1 += 1
					if pointer1 >= len(string1) or string1[pointer1] == ' ':
						break
			else:
				output = output + ''
				cost += 10
				pointer1 += 0
				pointer2 += 1
		# Double
		elif string1[pointer1] == string1[pointer1 - 1]:
			if debug:
				print('double')
			output = output + string2[pointer2 - 1]
			cost += 20
			pointer1 += 1
			pointer2 += 0
		# Single
		elif string2[pointer2] == string2[pointer2 - 1]:
			if debug:
				print('single')
			output = output + ''
			cost += 20
			pointer1 += 0
			pointer2 += 1
		# swap
		elif string1[pointer1:pointer1 + 2] == string2[pointer2:pointer2 + 2][::-1]:
			if debug:
				print('swap')
			output = output + string1[pointer1:pointer1 + 2]
			cost += 20
			pointer1 += 2
			pointer2 += 2
		# Punctuation
		elif not(string1[pointer1].isdigit() or string1[pointer1].isalpha()):
			if debug:
				print('punctuation')
			output = output + string1[pointer1]
			cost += 30
			pointer1 += 1
			pointer2 += 0
		elif not(string2[pointer2].isdigit() or string2[pointer2].isalpha()):
			if debug:
				print('punctuation')
			output = output + ''
			cost += 30
			pointer1 += 0
			pointer2 += 1
		# fDelete
		elif (len(string2) > (pointer2 + 1)) and (pointer2 == 0 and pointer1 == 0 and string1[pointer1] == string2[pointer2 + 1]):
			if debug:
				print('fdelete')
			output = output + ''
			cost += 200
			pointer1 += 0
			pointer2 += 1
		# fInsert
		elif (len(string1) > (pointer1 + 1)) and (pointer2 == 0 and pointer1 == 0 and string1[pointer1 + 1] == string2[pointer2]):
			if debug:
				print('finsert')
			output = output + string1[pointer1]
			cost += 200
			pointer1 += 1
			pointer2 += 0
		# fReplace
		elif pointer2 == 0 and pointer1 == 0:
			if debug:
				print('freplace')
			output = output + string1[pointer1]
			cost += 200
			pointer1 += 1
			pointer2 += 1
		# Delete
		elif (len(string2) > (pointer2 + 1)) and (string1[pointer1] == string2[pointer2 + 1]):
			if debug:
				print('delete')
			output = output + ''
			cost += 100
			pointer1 += 0
			pointer2 += 1
		# Insert
		elif (len(string1) > (pointer1 + 1)) and (string1[pointer1 + 1] == string2[pointer2]):
			if debug:
				print('insert')
			output = output + string1[pointer1]
			cost += 100
			pointer1 += 1
			pointer2 += 0
		# Replace
		else:
			if debug:
				print('replace')
			output = output + string1[pointer1]
			cost += 100
			pointer1 += 1
			pointer2 += 1

		if exit:
			break
		if iter > 100:
			print('pointer1 = {}'.format(pointer1))
			print('pointer2 = {}'.format(pointer2))
			print('l1 = {}, l2 = {}'.format(string1[pointer1], string2[pointer2]))
			print(output)
			break

	return cost
