rows = open('input.txt').read().replace('\n\n', '\n').split('\n')[:-1]


def get_adjacent(row_id, col_id):
    adjacent = ['.'] * 8
    r = 1
    # yes this is really bad i know
    for i in range(11):
        if row_id - r >= 0 and row_id - r < len(rows) and col_id - r >= 0 and col_id - r < len(rows[0]):
            if rows[row_id - r][col_id - r] != '.' and adjacent[0] == '.':
                adjacent[0] = rows[row_id - r][col_id - r]
        if row_id - r >= 0 and row_id - r < len(rows):
            if rows[row_id - r][col_id] != '.' and adjacent[1] == '.':
                adjacent[1] = rows[row_id - r][col_id]
        if row_id - r >= 0 and row_id - r < len(rows) and col_id + r >= 0 and col_id + r < len(rows[0]):
            if rows[row_id - r][col_id + r] != '.' and adjacent[2] == '.':
                adjacent[2] = rows[row_id - r][col_id + r]
        if col_id - r >= 0 and col_id - r < len(rows[0]):
            if rows[row_id][col_id - r] != '.' and adjacent[3] == '.':
                adjacent[3] = rows[row_id][col_id - r]
        if col_id + r >= 0 and col_id + r < len(rows[0]):
            if rows[row_id][col_id + r] != '.' and adjacent[4] == '.':
                adjacent[4] = rows[row_id][col_id + r]
        if row_id + r >= 0 and row_id + r < len(rows) and col_id - r >= 0 and col_id - r < len(rows[0]):
            if rows[row_id + r][col_id - r] != '.' and adjacent[5] == '.':
                adjacent[5] = rows[row_id + r][col_id - r]
        if row_id + r >= 0 and row_id + r < len(rows):
            if rows[row_id + r][col_id] != '.' and adjacent[6] == '.':
                adjacent[6] = rows[row_id + r][col_id]
        if row_id + r >= 0 and row_id + r < len(rows) and col_id + r >= 0 and col_id + r < len(rows[0]):
            if rows[row_id + r][col_id + r] != '.' and adjacent[7] == '.':
                adjacent[7] = rows[row_id + r][col_id + r]
        r += 1
    return adjacent


def round(rows):
    new_rows = rows.copy()
    for i, row in enumerate(new_rows):
        new_rows[i] = list(row)

    for row_id, row in enumerate(rows):
        for col_id, col in enumerate(row):
            adjacent = get_adjacent(row_id, col_id)
            if col == 'L' and adjacent.count('#') == 0:
                new_rows[row_id][col_id] = '#'
            elif col == '#' and adjacent.count('#') >= 5:
                new_rows[row_id][col_id] = 'L'

    for i, row in enumerate(new_rows):
        new_rows[i] = ''.join(row)
    return new_rows


def diff(old, new):
    for i in range(len(old)):
        if old[i] != new[i]:
            return True
    return False


while True:
    new_rows = round(rows)
    if rows == new_rows:
        counter = 0
        for row in new_rows:
            counter += ''.join(row).count('#')
        print(counter)
        break
    rows = new_rows
