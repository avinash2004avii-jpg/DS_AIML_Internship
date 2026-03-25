#** TASK-1 THE PERSONAL CONTACT BOOK

contacts={"avi":7483,"hemi":9483,"akhi":8546}
contacts.update({"akash":7567})
print(contacts)
contacts.update({"avi":7854})
print(contacts)
exist_contacts=contacts.get("avi")
print(exist_contacts)
missing_contacts=contacts.get("abhi","contact not found")
print(missing_contacts)
for name,number in contacts.items():
    print(f"contacts:{name} | phone: {number}")

#** TASK-2 THE DUPLICATE CLEANER

raw_logs=["id01","id02","id01","id05",
          "id02","id08","id01"]
unique_users=set(raw_logs)
print(unique_users)
present="id05" in unique_users
print(present)
original_list=len(raw_logs)
print(original_list)
duplicates=len(unique_users)
print(duplicates)
duplicates_removed=original_list-duplicates
print(duplicates_removed)

#** TASK-3 THE INTREST MATCHER

friend_a={"python","cooking","hiking","movies"}
friend_b={"hiking","gaming","photography","python"}

print(f'intersection:{friend_a & friend_b}')
print(f'union:{friend_a|friend_b}')
print(f'difference:{friend_a - friend_b}')