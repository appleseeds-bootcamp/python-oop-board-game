class Junction:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
    
    def is_jammed(self):
        return self.name == "Ayalon"

    def __repr__(self):
        return f"Name: {self.name}, Location: ({self.x},{self.y})"
    
    def __eq__(self, value):
        return value.x == self.x and value.y == self.y


if __name__ == "__main__":
    j1 = Junction("Hello", 1, 1)
    j2 = Junction("Goodbye", 1, 1)

    if j1 == j2:
        print("Equal!")
    else:
        print("Not equals")

    j1.is_jammed()
    print(j1)
    print(j2)


