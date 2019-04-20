from string import ascii_lowercase


def match(x, y): return (x.lower() == y.lower() and ((x.isupper() and y.islower()) or (x.islower() and y.isupper())))


polymer = open('input.txt').readline().strip()
min_len = None

for c in ascii_lowercase:
    rem_polymer = polymer.replace(c, "").replace(c.upper(), "")
    mod_polymer = []

    for p in rem_polymer:
        if mod_polymer and match(p, mod_polymer[-1]):
            mod_polymer.pop()
        else:
            mod_polymer.append(p)

    if min_len:
        if len(mod_polymer) < min_len:
            min_len = len(mod_polymer)
    else:
        min_len = len(mod_polymer)

print(min_len)

