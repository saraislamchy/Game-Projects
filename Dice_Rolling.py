import random

while True:
 choice = input("Roll the dice? (yes/no): ").lower()
 if choice =='yes':
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    print(f"({die1}, {die2})")
 elif choice == 'no':
   print("Thanks for playing!")
   break
 else:
   print("Invalid choice!")   