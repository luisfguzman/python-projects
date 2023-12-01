from datetime import datetime

user_input = input("Enter your goal with a deadline separated by colon. For example 'learn music:dd.mm.yyyy'\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline_date = datetime.strptime(input_list[1], "%d.%m.%Y")

# calculate how many daus from now until deadline
current_date = datetime.today()

deadline = deadline_date - current_date

if deadline.days < 0:
    print("user, you entered a date in the past, please try gain!")

print(f"Dear user, time remaining for your goal: '{goal}' is {deadline.days} days")