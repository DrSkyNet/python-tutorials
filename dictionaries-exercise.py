phonebook = {
    "John" : 83460286,
    "Jack" : 83462701,
    "Jill" : 83693289
}
phonebook["Jake"] = 82442561
phonebook.pop("Jill")

if "Jake" in phonebook:
    print("Jake is listed in the phonebook")
if "Jill" not in phonebook:
    print("Jill not in phonebook")
