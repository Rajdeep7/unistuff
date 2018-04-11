"""Simple exam trainer

Asks repeatedly all questions in a .md file in a random order. In each round,
all falsely answered questions are saved and asked again in the next round until
all questions have been answered correctly.

Each question in the input file should be in one line starting with '###'.
Everything until the next question is considered to be in the answer. Lines
starting with '## ' are ignored (these are intended for chapter titles).

A sample file (with german questions) can be found here:
https://github.com/batzner/unistuff/blob/master/LMU/IT-Sicherheit/Fragen.md
"""

import random
import os


def do_round(qnas):
    print('NEW ROUND: %d QUESTIONS' % len(qnas))
    # Keep the false answers for the next round
    false_answers = []
    for i, (question, solution) in enumerate(qnas):
        part = input('(%d/%d) %s\n' % (i+1, len(qnas), question))
        answer = part
        # Wait for input until the user inputs an empty line
        while part:
            part = input()
            answer += part
        print(solution)

        correct_input = None
        while correct_input not in ['y', 'n']:
            correct_input = input('Correct? (y / n)\n')

        if correct_input is 'n':
            false_answers.append((question, solution))

        print()

    correct_count = len(qnas) - len(false_answers)
    print('ROUND COMPLETE %d out of %d correct -> %f' % (correct_count, len(qnas), correct_count / len(qnas)))
    return false_answers


def main():
    path = input('Enter the path of the .md file:\n')
    if '~' in path:
        path = os.path.expanduser(path)

    with open(path) as questions_file:
        lines = questions_file.readlines()
    lines = [l for l in lines if not l.startswith('## ')]
    text = ''.join(lines)

    qnas = text.split('###')[1:]
    qnas = [[x.strip() for x in qna.split('\n', 1)] for qna in qnas]
    todo = qnas
    while todo:
        random.shuffle(todo)
        todo = do_round(todo)


if __name__ == '__main__':
    main()
