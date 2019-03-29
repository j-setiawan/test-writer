from sys import argv

from model.test import *
from app import build_test

with open(argv[1], 'r') as f:
    contents = f.read()

contents = contents.split('\n\n')

test_title = contents[0]
test_question_list = []

for q in contents[1:]:
    question = q.split('\n')

    # Determine question type
    question_info = question[0].split()

    q_type = question_info[0]
    q_pts = question_info[1]
    q_args = question_info[2:]

    sub_q = True if 'sub' in q_args else False

    q_pts = float(q_pts)
    q_question = question[1]

    if q_type == 'short':
        test_question_list.append(ShortQuestion(q_question, q_pts, question[2:], sub=sub_q))
    elif q_type == 'medium':
        choices = []

        for c in question[2:]:
            choices.append(c.split('|'))

        test_question_list.append(MediumQuestion(q_question, q_pts, choices, sub=sub_q))
    elif q_type == 'long':
        num_answer_lines = 1
        numbered_arg = [i for i, s in enumerate(q_args) if 'lines=' in s]

        if len(numbered_arg) > 0:
            num_answer_lines = int(q_args[numbered_arg[0]].split('=')[1])

        test_question_list.append(LongQuestion(q_question, q_pts, question[2:],
                                               translation=True if 'translation' in q_args else False,
                                               num_answer_lines=num_answer_lines,
                                               sub=sub_q))
    elif q_type == 'table':
        test_question_list.append(TableQuestion(q_question, q_pts, question[2].split('|'), question[3:]))
    elif q_type == 'picture':
        test_question_list.append(PictureQuestion(q_question, q_pts, question[2], question[3:]))
    elif q_type == 'translation':
        test_question_list.append(TranslationQuestion(q_question, q_pts, question[2], question[3]))
    elif q_type == 'dialogue':
        choices = []

        idx = 2
        while idx < len(question):
            choices.append(Dialogue(question[idx].split('|'), question[idx + 1]))
            idx += 2

        test_question_list.append(DialogueQuestion(q_question, q_pts, choices))
    elif q_type == 'freeform':
        numbered = True
        numbered_arg = [i for i, s in enumerate(q_args) if 'numbered=' in s]

        if len(numbered_arg) > 0:
            numbered = q_args[numbered_arg[0]].split('=')[1].lower() != 'false'

        choices = []

        for c in question[2:]:
            choices.append(c.split('|'))

        test_question_list.append(FreeFormQuestion(q_question, q_pts, choices, numbered=numbered))
    else:
        raise Exception('Unknown question type {}'.format(q_type))

build_test(Test(test_title, test_question_list), 'test_parser.docx')
