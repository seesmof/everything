def print_valid_parentheses_combinations(n):
    def generate_valid_combinations(open_count, close_count, current_combination):
        if open_count == close_count == n:
            print("".join(current_combination))
            return

        if open_count < n:
            current_combination.append("(")
            generate_valid_combinations(
                open_count + 1, close_count, current_combination
            )
            current_combination.pop()

        if close_count < open_count:
            current_combination.append(")")
            generate_valid_combinations(
                open_count, close_count + 1, current_combination
            )
            current_combination.pop()

    generate_valid_combinations(0, 0, [])


n = int(input("Enter the number of brackets: "))
print_valid_parentheses_combinations(n)
print()


def print_valid_parentheses_combinations_imperative(n):
    stack = []
    stack.append(("", 0, 0))

    while stack:
        current_combination, open_count, close_count = stack.pop()

        if open_count == close_count == n:
            print(current_combination)
            continue

        if open_count < n:
            stack.append((current_combination + "(", open_count + 1, close_count))

        if close_count < open_count:
            stack.append((current_combination + ")", open_count, close_count + 1))


print_valid_parentheses_combinations_imperative(n)
