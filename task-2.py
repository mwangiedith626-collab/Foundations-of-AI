#Australia map‑colouring problem
from constraint import Problem

problem = Problem()

regions = ["WA", "NT", "SA", "Q", "NSW"]

problem.addVariables(regions, ["Blue", "Red", "Green"])

adjacent = [("WA", "NT"), ("WA", "SA"), ("NT", "SA"), ("NT", "Q"),
            ("SA", "Q"), ("SA", "NSW"), ("Q", "NSW")]

for r1, r2 in adjacent:
    problem.addConstraint(lambda a, b: a != b, (r1, r2))

solutions = problem.getSolutions()
print("Number of solutions:", len(solutions))
print("solution:", solutions[0])



#Nairobi sub‑counties colouring.
subcounties = [
    "Westlands", "Dagoretti North", "Dagoretti South", "Langata",
    "Kibra", "Kasarani", "Roysambu", "Ruaraka", "Embakasi North",
    "Embakasi East", "Embakasi West", "Embakasi South", "Embakasi Central",
    "Makadara", "Kamukunji", "Starehe", "Mathare"
]

adjacent = [
    ("Westlands", "Dagoretti North"), ("Westlands", "Starehe"),
    ("Dagoretti North", "Dagoretti South"), ("Dagoretti North", "Kibra"),
    ("Dagoretti South", "Langata"), ("Langata", "Kibra"),
    ("Kibra", "Makadara"), ("Starehe", "Kamukunji"), ("Starehe", "Mathare"),
    ("Mathare", "Ruaraka"), ("Ruaraka", "Kasarani"), ("Kasarani", "Roysambu"),
    ("Embakasi North", "Ruaraka"), ("Embakasi East", "Embakasi North"),
    ("Embakasi West", "Embakasi Central"), ("Embakasi South", "Makadara"),
    ("Embakasi Central", "Kamukunji")
]


colors = ["Red", "Blue", "Green"]

problem.addVariables(subcounties, colors)

for r1, r2 in adjacent:
    problem.addConstraint(lambda a, b: a != b, (r1, r2))

solutions = problem.getSolutions()
print("Number of solutions with 3 colours:", len(solutions))

if len(solutions) == 0:
    problem = Problem()
    colors = ["Red", "Blue", "Green", "Yellow"]
    problem.addVariables(subcounties, colors)
    for r1, r2 in adjacent:
        problem.addConstraint(lambda a, b: a != b, (r1, r2))
    solutions = problem.getSolutions()
    print("Number of solutions with 4 colours:", len(solutions))
    print(" solution:", solutions[0])
else:
    print(" solution:", solutions[0])
