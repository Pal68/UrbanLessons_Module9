from itertools import combinations

def all_variants(text):
    for start in range(len(text)):
        for end in range(start + 1, len(text) + 1):
            yield text[start:end]

def all_variants_v1(text):
    for r in range(1, len(text) + 1):
        for all_comb in combinations(text, r):
            yield  ''.join(all_comb)


s = 'abc'
a = all_variants(s)
print(a)
for i in a:
    print(i)
print()

b = all_variants_v1(s)
print(b)
for i in b:
    print(i)


