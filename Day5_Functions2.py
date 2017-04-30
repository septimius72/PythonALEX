items = ["Alex", "Hunor", 323.12, 3123.123, "Eduard", "Atilla", "Erdelyi", 134]

str_items = []
num_items = []

for i in items:
	if isinstance(i, float) or isinstance(i, int):
		num_items.append(i)
	elif isinstance(i, str):
		str_items.append(i)
	else:
		pass

print(str_items)

print(num_items)

def parse_lists(abc):
	str_list_items = []
	num_list_items = []

	for i in abc:
		if isinstance(i, float) or isinstance(i, int):
			num_list_items.append(i)
		elif isinstance(i, str):
			str_list_items.append(i)
		else:
			pass
	return str_list_items, num_list_items

print(parse_lists(items))