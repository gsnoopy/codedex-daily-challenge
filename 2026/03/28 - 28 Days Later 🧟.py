def days_to_infect(city):

    humans = 0
    zombies = []
    days = 0

    for row in range(len(city)):
        for col in range(len(city[row])):
            if city[row][col] == '👤':
                humans += 1
            if city[row][col] == '🧟':
                zombies.append((row, col))

    directions = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    ]

    while zombies and humans > 0:

        new_zombies = []

        for row, col in zombies:
            for move_row, move_col in directions:

                next_row = row + move_row
                next_col = col + move_col

                if 0 <= next_row < len(city) and 0 <= next_col < len(city[0]) and city[next_row][next_col] == '👤':
                    city[next_row][next_col] = '🧟'
                    humans -= 1
                    new_zombies.append((next_row, next_col))

        if not new_zombies:
            return -1

        zombies = new_zombies
        days += 1

    return days