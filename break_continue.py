print()
print("*** looping demo #2 ***")
print()
for item in range(0, 5):
    print(item)

    keep_going = input("<enter> to keep looping, or <any key> to quit")

    if keep_going != "":
        break

print()
print("we are done")
print()
