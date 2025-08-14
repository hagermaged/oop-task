class Phone:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, num):
        self.contacts[name] = num

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]

    def make_call(self, name):
        if name in self.contacts:
            print("calling", name)
        else:
            print(name, "not found")


class Camera:
    def take_pic(self):
        print("The picture was taken successfully")


class Smartphone(Phone, Camera):
    pass


# example
sp = Smartphone()
sp.add_contact("Hager", "010123")
sp.make_call("Hager")
sp.take_pic()