sum_questions = 0

questions = []
with open("input.txt") as file:
    first_line = True
    for line in file:
        if line == '\n':
            sum_questions += len(questions)
            questions = []
            first_line = True
            continue
        if first_line:
            for char in line:
                if first_line and char not in questions and char != '\n':
                    questions.append(char)
        else:
            remove_questions = []
            for question in questions:
                if question not in line:
                    remove_questions.append(question)
            for remove_question in remove_questions:
                questions.remove(remove_question)
        first_line = False

print(sum_questions + len(questions))
