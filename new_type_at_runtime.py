#!/usr/bin/env python3

# Creating a new type at runtime


print('--- Demo: creating a new type at runtime ---')

# Here I create a new type with an attribute 'hello' that has the value
# 'world'. I then instantiate that type and check the 'hello' attribute.
new_type = type('NewType', (), {'hello':'world'})
new_type_instance = new_type()
print(new_type_instance.hello)

# Here we see that the type was created, despite not being traditionally
# declared via `class X:`
print(type(new_type_instance))



print()
print('--- Demo: runtime hierarchy ---')

# Here I'll take this to its logical extreme by creating an inheritance
# hierarchy without explicitly declaring a class in the traditional sense. We
# will find that these 'runtime-made' types work just like any other types.

def raise_not_implemented():
    raise NotImplementedError()

type_animal = type('Animal', (), {'talk': lambda _self: raise_not_implemented()})
type_dog = type('Dog', (type_animal,), {'talk': lambda _self: print('Bark')})
type_cat = type('Cat', (type_dog,), {'talk': lambda _self: print('Meow')})

my_dog = type_dog()
my_cat = type_cat()

my_dog.talk()
my_cat.talk()


print()
print('--- Demo: procedural type generation ---')

# So, in conclusion, we can procedurally create types at runtime. I don't
# believe that this is useful, but its theoretically possible.

import random

def new_random_type():
    chars = '0123456789abcdefghijklmnopqrstuvwxyz'
    unique_str = ''.join([random.choice(chars) for x in range(1,20)])
    name=f'Creature_{unique_str}'
    return type(name, (type_animal,), {'talk':lambda _self: print(unique_str)})

new_creature = new_random_type()()
print(type(new_creature))
new_creature.talk()

