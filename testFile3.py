cars = ["honda", "bmw", "audi", "chevy", "acura", "dodge"]

length = len(cars)
print(length)

cars.append("benz")
print(cars)

cars.insert(1, "jeep")
print(cars)

x = cars.index("honda")
print(x)


y = cars.pop()
print(y)
print(cars)

cars.remove("acura")
print(cars)

slicing = cars[0:2]
print(slicing)
print("*" * 20)
print(cars)
cars.sort()

print(cars)
