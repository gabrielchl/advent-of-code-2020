rows = open('input.txt').read().replace('\n\n', '\n').split('\n')[:-1]


def get_adjacent(row_id, col_id):
    adjacent = []
    for adjacent_row_id in range(row_id - 1, row_id + 2):
        for adjacent_col_id in range(col_id - 1, col_id + 2):
            if adjacent_row_id == row_id and adjacent_col_id == col_id:
                continue
            if adjacent_row_id < 0 or adjacent_col_id < 0:
                continue
            try:
                adjacent.append(rows[adjacent_row_id][adjacent_col_id])
            except IndexError:
                pass
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
            elif col == '#' and adjacent.count('#') >= 4:
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
