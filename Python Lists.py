if __name__ == '__main__':
    N = int(input())
    lists=[]
    commands = {
        "insert": lambda x: lists.insert(int(x[1]), int(x[2])),
        "print": lambda x: print(lists),
        "remove": lambda x: lists.remove(int(x[1])),
        "append": lambda x: lists.append(int(x[1])),
        "sort": lambda x: lists.sort(),
        "pop": lambda x: lists.pop(),
        "reverse": lambda x: lists.reverse()
    }
    
    for i in range(N):
        command = input().split()
        commands[command[0]](command)
