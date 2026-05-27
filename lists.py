bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles)
# print(bicycles[0].title())
# print(bicycles[-1].title())

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[2] = 'TVS'
# print(motorcycles)
motorcycles.append('ducati')
# print(motorcycles)
del motorcycles[-2]
popped_motorcycle = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycle)

another_popped = motorcycles.pop(1)
# print(motorcycles)
# print(another_popped)

motorcycles.append('yamaha')
motorcycles.remove('honda')
# print(motorcycles)

cars = ['bmw', 'aston martin', 'toyota', 'hennessy']
# cars.sort()
# i = 0
# for car in cars:
#     print(cars[i].upper())
#     if i<3:
#         i = i + 1
# print("")
# cars.sort(reverse=True)
# i = 0
# for car in cars:
#     print(cars[i].upper())
#     if i<3:
#         i = i + 1
print(sorted(cars, reverse=True))
print(reversed(cars))
print(cars)

n = len(cars)