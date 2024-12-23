def arithmetic_arranger(problems, show_answers=False):
    # Step 1: Check if too many problems
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    # Step 2: Storage for rows
    top_row = []
    bottom_row = []
    dash_row = []
    answer_row = []
    
    for problem in problems:
        # Step 2: Split the problem into parts
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Incorrect problem format"
        
        first_operand, operator, second_operand = parts
        

        # Step 3: Validate operator
        if operator not in ['+','-']:
            return "Error: Operator must be '+' or '-'."

        # Step 4: Validate operands
        if not(first_operand.isdigit() and second_operand.isdigit()):
            return "Error: Numbers must only contain digits."
        if len(first_operand) > 4 or len(second_operand) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        # Determine width for formatting
        width = max(len(first_operand), len(second_operand)) + 2

        # Create each row
        top_row.append(first_operand.rjust(width))
        bottom_row.append(operator + second_operand.rjust(width-1))
        dash_row.append("-" * width)

        # Optional: Calculate and store the result
        if show_answers:
            if operator == "+":
                result = str(int(first_operand) + int(second_operand))
            elif operator == "-":
                result = str(int(first_operand) - int(second_operand))
            answer_row.append(result.rjust(width))

     # Combine rows with 4 spaces between problems
    arranged_problems = "\n".join(["    ".join(top_row),"    ".join(bottom_row),"    ".join(dash_row)])
    if show_answers:
        arranged_problems += "\n" + "    ".join(answer_row)

    return arranged_problems

print(arithmetic_arranger(["121 + 21","52 - 9999", "1111 - 999"],True))