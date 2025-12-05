def read_input(filename: str):
    actions = []
    with open(filename) as file:
        for line in file:
            actions.append(line.rstrip())
    return actions

def process_actions(actions: list):
    result = 0 # This is the final password
    index = 50 # Problem said it starts at 50
    
    for action in actions:
        first_char = action[0]
        count = int(action[1:])
        if first_char == 'L': # Decrease
            i = count
            while i > 0:
                i -= 1
                if index == 0:
                    index = 100
                index -= 1
            if index == 0:
                result += 1
            print("Action {} Count {} Index {}".format(first_char, action[1:], index))
                                
        elif first_char == 'R': # increase
            i = count
            while i > 0:
                i -= 1
                if index == 99:
                    index = -1
                index += 1
            if index == 0:
                result += 1
            print("Action {} Count {} Index {}".format(first_char, action[1:], index))

    return result

actions = read_input("input/day1.input")
print(actions)
answer = process_actions(actions)
print(answer)