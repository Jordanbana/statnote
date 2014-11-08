a = "blah blah blah hello this is alex and alex likes pasta"

b = a.split()
used = []
counts = []
for x in b:
	if not x in used:
		counts.append([b.count(x), x])
		used.append(x)

counts.sort()
print list(reversed(counts))
