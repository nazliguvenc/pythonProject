lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
#friends.extend(lucky_numbers)
friends.append("Creed")
friends.insert(1, "Kelly")
friends.remove("Karen")
friends.pop()
print(friends)
print(friends.index("Oscar"))
print(friends.count("Jim"))
friends.sort()
print(friends)
lucky_numbers.reverse()
print(lucky_numbers)
friends2 = friends.copy()
print(friends2)