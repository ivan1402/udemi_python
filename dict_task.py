"""dict_a = {'a': 1, 'b': 2, 'c': 3}
for k, v in dict_a.items():
    print(f'k = {k} v = {v}')
"""

"""Определить средний балл оценок по всем предметам,
и вывести сведения о студентах, средний балл, которых больше 7."""

students = [
    {
        'firstname': 'Ivan',
        'Group': "1a",
        'physics': 6,
        'informatics': 7,
        'matematics': 8
     },
{
        'firstname': 'Eva',
        'Group': "2",
        'biologes': 9,
        'informatics': 8,
        'matematics': 8
     },
{
        'firstname': 'Gleb',
        'Group': "3b",
        'history': 5,
        'informatics': 7,
        'matematics': 7
     },
{
        'firstname': 'Sofa',
        'Group': "1b",
        'physics': 6,
        'informatics': 6,
        'matematics': 6
     },
]
predmeti = ['physics', 'informatics', 'matematics', 'history', 'biologes']
f_name = ['Ivan', 'Eva', 'Gleb', 'Sofa']
sum_stud = len(students)
# print(sum_stud, students[0])
sred_ball = 0
sum_b = 0
sum_pr = 0
for i in range(len(students)):

    for k, v in students[i].items():
        if k in predmeti:
            sum_b += v

            sum_pr += 1
    if sum_b / sum_pr > 7:
        print(sum_b / sum_pr)
        print(students[i])

# print(sum_b, sum_pr)
sred_ball = sum_b / sum_pr
print(f'sred_ball = {sred_ball}')
