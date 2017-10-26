rows = 'ABC'
cols = 'ABC'

print (rows == cols)

for i in xrange(9):
    print i

dia1 = set([rows[i] + cols[i] for i in xrange(len(rows))])
# dia1.remove('A1')
print(dia1)


dia2 = set([rows[i] + cols[len(rows) - i - 1] for i in xrange(len(rows))])
dia2.update(dia1)
print(dia2)
dia1.remove('A1')
print (dia1)
print (dia2)