class Planet:
    def __init__(self,name,planet_type,star):
        if not (isinstance(star,str) and isinstance(name,str) and isinstance(planet_type,str)):
            raise TypeError("name, planet type, and star must be strings")

        if(star == "" or name == "" or planet_type == ""):
            raise ValueError("name, planet_type, and star must be non-empty strings")

        self.name = name
        self.planet_type = planet_type
        self.star = star

    def orbit(self):
        return (f"{self.name} is orbiting around {self.star}...")

    def __str__(self):
        return (f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}")

planet_1 = Planet("alpha", "Europa", "Acrux")
planet_2 = Planet("beta", "Ganymede", "Antares")
planet_3 = Planet("delta", "Proxima", "Pollux")

print(planet_1)
print(planet_2)
print(planet_3)

print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())