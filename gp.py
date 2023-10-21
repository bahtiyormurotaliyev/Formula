class GP:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name
championship = Championship()

grand_prix1 = championship.define_grand_prix("Ali Grand Prix")
grand_prix2 = championship.define_grand_prix("French Grand Prix")

grand_prix = championship.get_grand_prix("Monaco Grand Prix")
if grand_prix is not None:
    print(f"Grand Prix found: {grand_prix.get_name()}")
else:
    print("Grand Prix not found")
