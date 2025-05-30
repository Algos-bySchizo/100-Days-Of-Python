# from prettytable import PrettyTable
import prettytable
# table=PrettyTable()
table=prettytable.PrettyTable()
table.add_column('Pokemon Name',['Pikachu','Squirtle','Charizard'])
table.add_column('Type',['Electric','Water','Fire'])
table.align='c'
print(table)

