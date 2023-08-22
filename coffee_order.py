print()
print("*** Coffee Order Demo ***")
# /\ for the title

# \/ make a loop
keep_going = ""
while keep_going == "":

    want_coffee = input("do you want coffee? ").lower()
    if want_coffee != "yes":
        print("why not bruv, its quoit noice")
        continue

    else:
        print("good choice")
        break
# getting input and answering accordingly

print()
print("end of program")
print()
