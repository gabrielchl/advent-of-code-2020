sum_questions = 0

questions = []
with open("input.txt") as file:
    for line in file:
        if line == '\n':
            sum_questions += len(list(set(questions)))
            questions = []
            continue
        for char in line:
            if char != '\n':
                questions.append(char)

print(sum_questions + len(list(set(questions))))
