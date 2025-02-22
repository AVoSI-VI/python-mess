def oldest_person(people: list):
    oldest = ""
    agei = 2050
    for blah in range(len(people)):
        if people[blah][1] < agei:
            oldest = people[blah][0]
            agei = people[blah][1]
    return oldest

def older_people(people: list, year: int):
    ol = []
    for blah in range(len(people)):
        if people[blah][1] < year:
            ol.append(people[blah][0])
    return ol

p1 = ("Adam", 1977)
p2 = ("Ellen", 1985)
p3 = ("Mary", 1953)
p4 = ("Ernest", 1997)
people = [p1, p2, p3, p4]

older = older_people(people, 1979)
print(older)