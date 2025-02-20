# Eliya Statema
# 2/20/25
# Math Quiz

variable_1 = 38
variable_2 = 73

print(f"{variable_1} + {variable_2} = ?")

def calculate_sum(n1, n2):
    addition = n1 + n2
    user_answer = int(input("Enter your answer here: "))
    if user_answer == addition:
        print("Congratulations! That is the correct answer.")
    else:
        print(f"The correct answer is {addition}.")

calculate_sum(variable_1, variable_2)