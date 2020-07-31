from assingment2_solution import LogFile, DelimFile
# from assingment2 import LogFile, DelimFile


fh = LogFile('text.txt')
fh.write('My name is Anigo Muntoya!')
fh.write('You killed my father. prepere to DIE!')

se = DelimFile('text1.csv', ',')
se.write(['a', 'b', 'c,e', 'd'])
se.write(['1', '2', '3', '4'])
