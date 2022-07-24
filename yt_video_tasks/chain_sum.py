rezalts = 0

def chain_sum (*num):
	nonlocal rezalts
	rez = rezalts 
	print (f"rez = {rez}")
	if len (num):
		rez += num[0]
		return chain_sum
	else: 
		print (rez)

print (f"rezalts = {rezalts}")

if __name__ == '__main__':
	print (chain_sum (5)(2)())
	rezalt = []
	# rezalt.append (chain_sum (5)())
	# rezalt.append (chain_sum (5)(2)())
	# rezalt.append (chain_sum (5)(100)(-10)())
