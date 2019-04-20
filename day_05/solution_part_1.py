def match(x, y): return (x.lower() == y.lower() and ((x.isupper() and y.islower()) or (x.islower() and y.isupper())))


polymer = open('input.txt').readline().strip()
mod_polymer = []

for c in polymer:
    if mod_polymer and match(c, mod_polymer[-1]):
        mod_polymer.pop()
    else:
        mod_polymer.append(c)

print("Remaining units after fully reacting the scanned polymer:", len(mod_polymer))
