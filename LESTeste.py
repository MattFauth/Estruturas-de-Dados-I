import LES
l=LES.LES()
l.insertEnd('A')
l.insertEnd('B')
l.insertEnd('C')
l.show()
l.insertAfter('X','C')
'''l.insertEnd('C')
l.insertEnd('B')
l.insertEnd('A')'''
l.show()
print('****')
print(l.getQuant())
print('****')
print(l.substituirEcontar('C','K'))
l.show()
print('****')
print(l.substituirEcontar('A','X'))
l.show()
print('****')
print(l.substituirEcontar('X','Z'))
l.show()
print('****')
l.substituir('Z','X')
l.show()



'''
l.insertAfter('X','A')
l.show()
print('****')'''
'''if not l.itsFull():
    l.insertEnd('B')
if not l.itsFull():
    l.insertEnd('C')
if not l.itsFull():
    l.insertEnd('D')
if not l.itsFull():
    l.insertEnd('E')
if not l.itsFull():
    l.insertEnd('F')
l.show()'''
'''
l.insertEnd('B')
l.insertEnd('C')
l.insertEnd('D')
l.insertEnd('E')
l.insertEnd('F')
l.show()'''
'''l.show()
print('****')
l.removeEnd()
l.show()
print('****')
l.insertEnd('C')
l.show()'''
