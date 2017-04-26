'''
Dictionary
Dictionary items are in brackets{}, in key: value pairs, separated with ","
sample: {"key1":"value1", "key2":"value2"}'''
car = {"make":"bmw", "model":"550i", "year": 2016}
print(car)

d = {}

model = car["model"]

print(car["model"])
print(model)

d["one"] = 1
d["two"] = 2
d["three"] = 3
d["four"] = 4

print(d)

sum_1 = d["two"] + 12

print(sum_1)
print(d)

d["two"] = d["two"] + 8
print(d)

sum_1 = d["three"] + 5
print(sum_1)

