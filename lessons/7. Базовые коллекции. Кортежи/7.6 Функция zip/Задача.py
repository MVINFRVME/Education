names = ['Tom', 'Bob', 'Albert']
ages = [20, 45, 70, 100]

people = set(zip(names, ages))
print(people)

people_2 = zip(names, ages)
for i_person in people_2:
    print(i_person)

people_3 = {
    i_name: i_age + 10
    for i_name, i_age in zip(names, ages)
}

print(people_3)
