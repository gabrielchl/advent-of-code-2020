instructions = open('example-1.txt').read().replace('\n\n', '\n').split('\n')[:-1]

ship_x = ship_y = 0
wp_x = 10
wp_y = 1

for instruction in instructions:
    action = instruction[0]
    value = int(instruction[1:])

    if action == 'N':
        wp_y += value
    elif action == 'S':
        wp_y -= value
    elif action == 'E':
        wp_x += value
    elif action == 'W':
        wp_x -= value
    elif action == 'L':
        rotate = (value / 90) % 4
        if rotate == 2:
            wp_x *= -1
            wp_y *= -1
        else:
            for _ in range(int(rotate)):
                new_wp_y = wp_x
                wp_x = wp_y * -1
                wp_y = new_wp_y
    elif action == 'R':
        rotate = (value / 90) % 4
        if rotate == 2:
            wp_x *= -1
            wp_y *= -1
        else:
            for _ in range(int(rotate)):
                new_wp_x = wp_y
                wp_y = wp_x * -1
                wp_x = new_wp_x
    elif action == 'F':
        ship_x += wp_x * value
        ship_y += wp_y * value

print(abs(ship_x) + abs(ship_y))
