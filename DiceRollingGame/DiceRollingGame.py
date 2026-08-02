import random
a = [1, 2, 3, 4, 5, 6]
choice = input("Roll the dice? (y.n): ") 
if choice.lower() == 'a':
    print('Invalid choice')
elif choice.lower() == 'b':
    print('Invalid choice')
elif choice.lower() == 'y':
  print(random.choice(a))
else:
    print('Thanks for playing')
