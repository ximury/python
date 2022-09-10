a = None
b = a or []
print(b, end="*\n")

b = [1, 2]
print(b[0], end="**\n")

# b = []
for item in b:
    print(item, end="***\n")

a = None
b1 = a or 100
b2 = a if a else 100
print(b1, end="****\n")
print(b2, end="****\n")

di = {'a': True, 'b': False}
print(di.get('a'))
print(di.get('b'))

# "" None False
a = ""

if not a:
    print("***")

a = []
if a is not None:
    print("8888")

q1 = None
# q1 = ''
q2 = q1 or ''

print(q2, type(q2))

print("---------------")

a1 = ''
a1 = None
if a1:
    print(True)

b1 = None
b2 = 0
print(b1 or b2)
print(b2 or b1)
print(None or "")

form = {}
form['a'] = 0
aa = form.get("a") or None
print(aa)

a, b = 1, 0
a = 12
print(a, b)

a = b = 0
b = 12
print(a, b)
