age = 36;
name = "Angela Consoli";

mylanguages = [];
mylanguages.append("Java");
mylanguages.append("Ada95");
mylanguages.append("C");

print(name + ", %d," %age + " is learning Python!" + " " + name + " knows these languages: ");

for l in mylanguages:
    print(l + " ");
    if (l == 'Java'):
        print(" (which is awesome!)");
