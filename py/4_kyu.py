import math

# reusebal code block

def test (funk_rez, right_answer):
	if funk_rez is right_answer:
		return True
	return False 

# Counting Change Combinations
# link: https://www.codewars.com/kata/541af676b589989aed0009e7

def count_change(money: int, coins: list) -> int:
	count_change = 3
	return count_change

def test_count_change (*args):
	rezalts = []
	rezalts.append (test(count_change (4, [1,2]), 3))
	rezalts.append (test(count_change (10, [5,2,3]), 4))
	rezalts.append (test(count_change (11, [5,7]), 0))
	print (rezalts)

# Superheroes Convention #1 Pandemic
# link: https://www.codewars.com/kata/6202149e89771200306428f0/train/python

# first try to complit this task 
def is_possible_try_1(database: dict) -> bool:
	"""return true if its possible"""
	half_of_count = math.ceil(len (database) / 2)
	for target_hero in database.keys ():
		how_many_hate_him = 0
		for check_hero in database.keys ():
			if database.get(check_hero).count (target_hero):
				how_many_hate_him += 1
		if half_of_count < how_many_hate_him:
			return False
	return True 

# second try to complit this task 
def check_hate_list (list_of_hate: list, members_list: list) -> bool:
	""""""
	for i in list_of_hate:
		if members_list.count (i):
			return False
	return True

def is_possible_try_2 (database: dict) -> bool:
	"""return true if its possible"""
	database = dict(sorted(database.items(), key = lambda x: -len(x[1])))
	first_day_combinations_list = []
	seconde_day_combinations_list = []
	for target_hero in database.keys():
		if check_hate_list (database.get(target_hero), first_day_combinations_list) or len (database.get(target_hero)) == 0:
			first_day_combinations_list.append (target_hero)
		elif check_hate_list (database.get(target_hero), seconde_day_combinations_list):
			seconde_day_combinations_list.append (target_hero)
		else:
			print ("This last hero: ", target_hero)
			print ("This is list of all heroes: ", database)
			return False
	return True

# third attempt to solve this task
def is_possible (database: dict) -> bool:
	"""return true if its possible"""
	# sort database for  
	database = dict(sorted(database.items(), key = lambda x: -len(x[1])))
	first_day_hate_combinations_list = []
	seconde_day_hate_combinations_list = []
	for target_hero in database:

	return True

def test_is_possible (*args):
	rezalts = []
	rezalts.append (test (is_possible ({0:[1, 2], 1: [0], 2: [0], 3: []}), True))
	rezalts.append (test (is_possible ({0:[1, 2], 1: [0], 2: [0], 3: [], 4:[5,6], 5:[4], 6:[4]}), True))
	rezalts.append (test (is_possible ({0:[1, 2, 3], 1: [0], 2: [0,3], 3: [2,0]}), False))
	rezalts.append (test (is_possible ({0: [1, 2], 1: [0], 2: [0, 3], 3: [2, 4, 5], 4: [3, 5], 5: [3, 4]}), False))
	rezalts.append (test (is_possible ({3: [7, 5, 9], 5: [3, 4, 8], 0: [4, 10], 1: [6, 7], 4: [0, 5], 7: [1, 3], 6: [1], 8: [5], 9: [3], 10: [0], 2: []}), True))
	print (rezalts)

if __name__ == '__main__':
	test_is_possible ()