
profs = ["Ackles", "Krebsbach", "Gregg"]

profs = {"Ackles": "Steitz 131", "Krebsbach": "Briggs 411", "Gregg": "Briggs 413"}

print(profs["Ackles"])
print(profs.keys())
print(profs.values())

for i in profs.items():
    print(i)

print("Ackles" in profs)
print("Sattler" in profs)
print("Ackles" not in profs)
print("Sattler" not in profs)