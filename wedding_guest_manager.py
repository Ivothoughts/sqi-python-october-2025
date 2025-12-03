# stage1
confirmed_guests = ["Alice", "Charlie", "Eve", ""
"Bob", "Frank", "Grace", "David", "Hannah", "Liam", "Mia"]
waitlist =[]

print("\n\nStage 1")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)

#2 Three siblings Ken, Jack and Ivy accept the invitation but are put on the waitlist.
waitlist.extend(["Ken", "Jack", "Ivy"])
print("\n\nStage 2")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)

#3  Noah, the groom’s ex-classmate in the university and Oliver who lives next door to the bride have accepted the invitation. Put them on the waitlist.
waitlist.append("Noah")
waitlist.append("Oliver")
print("\n\nStage 3")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)

#4  Alice has a family emergency and won’t be able to attend the wedding, She cancels her attendance. Remove Alice from the confirmed guest list and add the first person from the waitlist to the confirmed list. 
confirmed_guests.remove("Alice")
confirmed_guests.append(waitlist.pop(0))

print("\n\nStage 4")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)

#5 Charlie is the godfather of the groom and he is the one funding the wedding. Therefore he is a VIP guest and the couple has asked you to make sure he is on the guestlist. Check whether or not Charlie is on the guestlist.

print("\n\nStage 5")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)
print(f"It is {"Charlie" in confirmed_guests} that Charlie is the guest list.")

#6 David and Eve have decided they no longer want to attend the wedding and therefore cancel their attendance. Remove them from the confirmed_guests list.
confirmed_guests.remove("David")
del confirmed_guests[1]
print("\n\nStage 6")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)

#7  Move the first 2 people on the waitlist into the guestlist to fill up the newly freed slots.

confirmed_guests.append(waitlist.pop(0))
confirmed_guests.append(waitlist.pop(0))
print("\n\nStage 7")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)

#8  Oliver just realized the day of the wedding is the same day he has to take his pet to see the vet and he cancels his attendance. Remove him from the waitlist.

waitlist.pop()
print("\n\nStage 8")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)

#9 The event planner has asked you for the names of the last 3 guests on the guest list because she needs to make additional arrangements for them. Get her this information.

print("\n\nStage 9")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)
print("Last three confirmed guest: ", confirmed_guests[-3:])

# 10. 	The bride and groom have decided that they want to allow room for 5 more people to attend their wedding. Move 
# 	waitlisted guest (Noah) into the confirmed_guests list.
 
confirmed_guests.append(waitlist.pop(0))
print("\n\nStage 10")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)

# 11. 	The event planner wants a report on the number of people who will be attending the wedding. Give her this information.

print("\n\nStage 11")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)
print("Number of confirmed guests:", len(confirmed_guests))

# 12. 	The event planner has also requested that you give her a list of all the names of the confirmed_guests. 
# The guests would be seated alphabetically at the venue and so she wants the names in alphabetical order.

confirmed_guests.sort()
print("\n\nStage 12")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)

# 13. 	A new guest called Collins who is the son of Grace and Noah would be attending on their behalf, Replace Grace and Noah 
# 	on the confirmed_guests list with Collins. Make sure you re-sort the list.
confirmed_guests.pop()
del confirmed_guests[3]
confirmed_guests.append("Collins")
confirmed_guests.sort()
print("\n\nStage 13")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)

# 14. 	The caterer has also requested for the confirmed_guests list so she can provide the guests with customized bags 
# 	containing their food with their names on it. Give her a copy of the confirmed_guests list titled 
# 	guests_list_for_caterer`.

guest_list_for_caterer = confirmed_guests.copy()
print("\n\nStage 14")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)
print("Guest list for caterer:", guest_list_for_caterer)

#15  The deadline for accepting the invitations sent has now passed. There is no more need for the waitlist. 	Clear the waitlist.

waitlist.clear()
print("\n\nStage 15")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)


["something", "fishy", "is_going" , "on"]