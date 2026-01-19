dinner_invite = ["mus'ab", 'sadiq', 'aliyu', 'muhammad sani']
print('Hi ' + dinner_invite[0].title() + ", you're invited to our dinner.")
print('\nHi ' + dinner_invite[1].title() + ", you're invited to our dinner.")
print('\nHi ' + dinner_invite[2].title() + ", you're invited to our dinner.")
print('Hi ' + dinner_invite[3].title() + ", you're invited to our dinner.")

print('\n' + dinner_invite[1] + 'cannot make it to the dinner.')

dinner_invite[1] = 'aseem'

print('Hi ' + dinner_invite[0].title() + ", you're invited to our dinner.")
print('\nHi ' + dinner_invite[1].title() + ", you're invited to our dinner.")
print('\nHi ' + dinner_invite[2].title() + ", you're invited to our dinner.")
print('Hi ' + dinner_invite[3].title() + ", you're invited to our dinner.")

print('\nThe big dinner is coming!')

dinner_invite.insert(0, 'abdoul')
dinner_invite.insert(3, 'ibrahim')
dinner_invite.append('Umar')


print('Hi ' + dinner_invite[0].title() + ", you're invited to our dinner.")
print('\nHi ' + dinner_invite[1].title() + ", you're invited to our dinner.")
print('\nHi ' + dinner_invite[2].title() + ", you're invited to our dinner.")
print('\nHi ' + dinner_invite[3].title() + ", you're invited to our dinner.")
print('\nHi ' + dinner_invite[4].title() + ", you're invited to our dinner.")
print('\nHi ' + dinner_invite[5].title() + ", you're invited to our dinner.")
print('\nHi ' + dinner_invite[6].title() + ", you're invited to our dinner.")

print("\nWe're sorry inform you that the dinner event is only two guest.")

ex_dinner_invite = dinner_invite.pop()
print('\nHi ' + ex_dinner_invite.title() + ", We're sorry to inform you that your invite to the dinner is canceled.")


ex_dinner_invite = dinner_invite.pop()
print('\nHi ' + ex_dinner_invite.title() + ", We're sorry to inform you that your invite to the dinner is canceled.")


ex_dinner_invite = dinner_invite.pop()
print('\nHi ' + ex_dinner_invite.title() + ", We're sorry to inform you that your invite to the dinner is canceled.")


ex_dinner_invite = dinner_invite.pop()
print('\nHi ' + ex_dinner_invite.title() + ", We're sorry to inform you that your invite to the dinner is canceled.")


ex_dinner_invite = dinner_invite.pop()
print('\nHi ' + ex_dinner_invite.title() + ", We're sorry to inform you that your invite to the dinner is canceled.")

print('\nHi ' + dinner_invite[0].title() + ", We're please to inform you that you're still invited to the dinner!")
print('\nHi ' + dinner_invite[1].title() + ", We're please to inform you that you're still invited to the dinner!")

del dinner_invite[0]
del dinner_invite[0]

print(dinner_invite)