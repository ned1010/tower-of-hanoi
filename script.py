from stack import Stack

print("Welcome to Tower of Hanoi")
print("Here are the rules for the game\n 1. Only one disk can be moved among the towers at any given time."
" \n 2. Only the top disk can be removed. \n 3. No large disk can sit over a small disk.")

stacks = []
left_stack = Stack("left")
middle_stack = Stack("middle")
right_stack = Stack("right")

#stacks are stored in an array.
#all stacks are list nested in the main stacks list
stacks += [left_stack, middle_stack, right_stack]

#number of disks to play the game
num_of_disks = int(input("\n\nEnter the number of disks you want to play the game: "))

while num_of_disks < 3:
    num_of_disks = int(input("Enter a number greater than 3: "))

for i in range(num_of_disks, 0, -1):
    left_stack.push(i)

#optimal moves

optimal_moves = 2**(num_of_disks) - 1
print(f"The fastest you can finish this game is in {optimal_moves} moves")


def get_user_input():
    options = [i.get_name()[0] for i in stacks]
    while True:
        for i in range(len(stacks)):
            name = stacks[i].get_name()
            letter = options[i]
            print(f"Enter {letter} letter for {name}")
        user_input = input("Enter: ")

        if user_input in options:
            for i in range(len(stacks)):
                if user_input == options[i]:
                    return stacks[i]


#play the game
user_moves = 0
while (right_stack.get_size() != num_of_disks):
    print("\n\n\n ...Your current stacks looks like...")

    for stack in stacks:
        print(stack.print_list())

    while True:
        print("\nWhich stack do  you want to move from")
        from_stack = get_user_input()
        print("\nwhich stack do you want to move to")
        to_stack= get_user_input()

        if from_stack.get_size() == 0:
            print("The stack is empty, try again....")
        elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
            node = from_stack.pop()
            to_stack.push(node)
            user_moves += 1
            break
        else:
            print("Try again!")
print(f"You finished the game in {user_moves}")

