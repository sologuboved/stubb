from random import randint, seed
from check_if_fits import generate_top_dummy, update_top, LENGTH, CHAPTER, PARAGRAPH


def launch_update_top(top, case):

    for item in case:
        update_top(top, *item)


def generate_case(case_size, top_size):

    case = list()
    solution = set()

    for _ in range(case_size):
        num = randint(1, 10000)
        case.append((num, num, num))
        solution.add(num)

    solution = [{LENGTH: num, CHAPTER: num, PARAGRAPH: num} for num in sorted(list(solution), reverse=True)[: top_size]]

    return case, solution


def run_tests(num_cases, case_size, top_size):

    res = list()
    cases_and_solutions = [generate_case(case_size, top_size) for _ in range(num_cases)]

    for item in cases_and_solutions:
        case = item[0]
        correct_solution = item[1]
        solution_in_question = generate_top_dummy(top_size)
        launch_sort_top(solution_in_question, case)
        if solution_in_question == correct_solution:
            res.append(False)
        else:
            prettyprint_nomatch(case, correct_solution, solution_in_question)
            return
    print(sum(res) == 0, len(res) == num_cases)


def prettyprint_nomatch(case, correct_solution, solution_in_question):

    print('Case:')
    for entry in case:
        print(entry)
    print()

    print("Correct solution:")
    for entry in correct_solution:
        print(entry)
    print()

    print("Incorrect solution:")
    for entry in solution_in_question:
        print(entry)


if __name__ == '__main__':
    seed(19)
    run_tests(1, 10, 2)
