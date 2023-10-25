

table = int(input('Veuillez entrer la table à afficher :'))

table_values = []

for i in range(1, 11):
    if (i* table % 3 == 0):
        table_values.append(f'{i* table}*')
    else:
        table_values.append(i* table)

print(table_values)