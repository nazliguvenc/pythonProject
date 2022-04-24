
for letter in "Giraffe Academy":
    print(letter)

print("===========================")

friends = ["Jim", "Karen", "Kevin"]
for friend in friends:
    print(friend)
print("===========================")

for index in range(3, 10):    # 10 not include
    print(index)
print("===========================")

for index in range(len(friends)):
    print(index)
print("===========================")

for index in range(5):
    if index == 0:
        print("first Iteration")
    else:
        print("Not first")