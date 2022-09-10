checked_user = ["a|num1", "b|num2"]
for item in checked_user:
    terminal_user_id = item.split("|")[0]
    terminal_user_name = item.split("|")[1]
    print(terminal_user_id)
    print(terminal_user_name)