# ECHO is on.

class Human:
    def __init__(self, first_name: str, last_name: str, age: int, address: str, is_hungry: bool, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address
        self.is_hungry = is_hungry

        # BONUS: Assign any additional attributes from kwargs
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __repr__(self):
        return f"Human( first_name={self.first_name} last_name={self.last_name} age={self.age} address={self.address} is_hungry={self.is_hungry} )"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def order_drinks(self):
        if self.age >= 21:
            return "Party time!"
        else:
            return "Denied"

    def eat(self):
        self.is_hungry = False

    def win_lottery(self):
        self.address = "TomorrowLand"
