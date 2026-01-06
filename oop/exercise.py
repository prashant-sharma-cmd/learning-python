class User:
    def __init__(self, name, birthyear):
        self.name = name
        self.birthyear = birthyear

    def get_name(self):
        return self.name.upper()

    def age(self, current_year):
        current_age = current_year - self.birthyear
        return current_age

user = User(name="John", birthyear=1999)
print(user.get_name(), user.age(2023))

