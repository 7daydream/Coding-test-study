'''
Result
-----
0.8999999999
false
0.9
true
123.46
-----
'''

a = 0.3 + 0.6
print(a)

if a == 0.9:
    print('true')
else:
    print('false')

print(round(a, 2))

if round(a,2) == 0.9:
    print('true')
else:
    print('false')

print(round(123.456,2))

