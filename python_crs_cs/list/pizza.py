pizzas = ['almon-bada', 'pinot-bada', 'pizza']

for pizza in pizzas:
    print('I like ' + pizza.title() + ', Pizza')

print('\nI really like to eat Pizza.\nExpecially ' + pizzas[1].title() + '.')

print('\nThe first three items in the pizza list are: ', pizzas[:3])
print('\nThe items from the middle of the list are: ', pizzas[1:3])
print('\nThe last three items are: ', pizzas[-3:])

friend_pizza = pizzas[:]

pizzas.append('pure_pizza')
friend_pizza.append('orange_pizza')
print('\n\tFriend pizza: ', friend_pizza)
print('\n\tOriginal pizza: ', pizzas)