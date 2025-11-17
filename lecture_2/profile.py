def generate_profile(age):
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    else:
        return "Adult"

print("Enter your full name: ", end="")
user_name = input()
print("Enter your birth year: ", end="")
birth_year_str = input()
birth_year = int(birth_year_str)
current_age = 2025 - birth_year
hobbies = list()
hobby_bool = True
while hobby_bool:
    print("Enter a favorite hobby or type 'stop' to finish: ", end="")
    hobby = input()
    if hobby == "stop":
        hobby_bool = False
    else:
        hobbies.append(hobby)
life_stage = generate_profile(current_age)
user_profile = {
    "name": user_name,
    "age": current_age,
    "stage": life_stage,
    "hobbies": hobbies}
print("---")
print("Profile Summary: ")
print(f"Name: {user_profile['name']}\nAge: {user_profile['age']}")
print(f"Life Stage: {user_profile['stage']}")
if user_profile['hobbies'] == []:
    print("You didn't mention any hobbies.")
else:
    print(f"Favorite Hobbies ({len(user_profile['hobbies'])}): ")
    for item in user_profile['hobbies']:
        print(f"- {item}")
print("---")
