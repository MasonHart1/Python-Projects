user_name = input("Enter your name: ")
print("Hello " + user_name)

user_age = input("Enter your age: ")

user_months = int(user_age) * 12

user_days = int(user_age) * 365

print(f'{user_name} is {user_age} years old, or {user_months} months old, or {user_days} days old')