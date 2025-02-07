#1-2:
names = ["Nika", "Beso", "Taso", "Lika"]
for name in names:
    print(f"Hello {name}, hope you're having a great day!")

#3:
transport = ["Bayerische Motoren Werke", "Kawasaki motorcycle", "Yamaha scooter"]
for item in transport:
    print(f"I would like to own a {item}.")

#4:
guests = ["Elon Musk", "Jon Jones", "Trump"]
for guest in guests:
    print(f"Dear {guest}, you are invited to dinner at my place.")

#5:
guest_cant_make_it = "Jon Jones"
print(f"{guest_cant_make_it} can't make it to dinner.")
guests[1] = "Elon Musk"
for guest in guests:
    print(f"Dear {guest}, you are invited to dinner at my place.")

#6:
print("Great news! I found a bigger dinner table!")
guests.insert(0, "Elon Musk")
guests.insert(2, "Trump")
guests.append("Jon Jones")
for guest in guests:
    print(f"Dear {guest}, you are invited to dinner at my place.")

#7:
print("Unfortunately, I can only invite two guests.")
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry {removed_guest}, I can't invite you to dinner.")
for guest in guests:
    print(f"{guest}, you are still invited to dinner.")
del guests[:]
print("Final guest list:", guests)

#8:
places = ["Japan", "Norway", "New Zealand", "Switzerland", "Canada"]
print("Original list:", places)
print("Alphabetical order:", sorted(places))
print("Original list after sorted():", places)
print("Reverse alphabetical order:", sorted(places, reverse=True))
places.reverse()
print("Reversed list:", places)
places.reverse()
print("Back to original order:", places)
places.sort()
print("Sorted list:", places)
places.sort(reverse=True)
print("Reverse sorted list:", places)

#9:
guests = ["Elon Musk", "Trump", "Jon Jones"]
print(f"I am inviting {len(guests)} people to dinner.")

#10:
things = ["Everest", "Amazon River", "USA", "Tokyo", "English"]
print("Original list:", things)
things.append("Python")
things.insert(2, "Sahara Desert")
print("List after insert and append:", things)
things.remove("USA")
popped_item = things.pop()
print("Popped item:", popped_item)
things.sort()
print("Sorted list:", things)
things.sort(reverse=True)
print("Reverse sorted list:", things)
things.reverse()
print("Reversed list:", things)

#11:
# print(things[10])  # IndexError
