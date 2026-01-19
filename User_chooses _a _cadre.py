networking = []
programming = []
sysadmin = []

while True:
    name = input("Enter interviewee name (or 'exit'): ")
    if name.lower() == "exit":
        break

    cadre = input("Choose cadre (networking/programming/sysadmin): ").lower()

    if cadre == "networking":
        networking.append(name)
    elif cadre == "programming":
        programming.append(name)
    elif cadre == "sysadmin":
        sysadmin.append(name)
    else:
        print("Invalid cadre")

print("\n--- Interviewees by Cadre ---")
print("Networking:", networking)
print("Programming:", programming)
print("System Administration:", sysadmin)

total = len(networking) + len(programming) + len(sysadmin)
print("\nTotal Interviewees:", total)
