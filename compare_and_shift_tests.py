from random import randint, seed
from check_if_fits import compare_and_shift, TOP, LENGTH, CHAPTER, PARAGRAPH


def generate_top(top_size):

    top = list()
    for ind in range(top_size):
        top.append({LENGTH: 0, CHAPTER: None, PARAGRAPH: None})

    return top


def generate_case(case_size, top_size):

    case = list()
    solution = set()

    for _ in range(case_size):
        num = randint(1, 10000)
        case.append((num, num, num))
        solution.add(num)

    solution = [{LENGTH: num, CHAPTER: num, PARAGRAPH: num} for num in sorted(list(solution), reverse=True)[: top_size]]

    return case, solution


def get_compare_and_shift(top, case):
    pass


if __name__ == '__main__':
    seed(19)

    c, s = generate_case(10, 5)

    for i in c:
        print(i)
    print()
    for i in s:
        print(i)


