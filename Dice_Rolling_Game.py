import random

dice_faces = {
    1: "⚀",
    2: "⚁",
    3: "⚂",
    4: "⚃",
    5: "⚄",
    6: "⚅"
}

while True:
    choice = input('Roll the dice? 🎲 (y/n): ').lower()

    if choice == 'y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f'You rolled: {dice_faces[die1]}, {dice_faces[die2]} (Values: {die1}, {die2})')

        if die1 == die2:
            print('🎊 Lucky Roll! You rolled a double! 🎊')

        print()  # for spacing

    elif choice == 'n':
        print('Thanks for playing! 🎲')
        break

    else:
        print('Invalid choice! 🎲\n')
