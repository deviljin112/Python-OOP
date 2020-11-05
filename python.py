from snake import Snake


class Python(Snake):
    def __init__(self):
        super().__init__(False)
        self.large = True
        self.two_lungs = True

    def digest_large_pray(self):
        return "Big Nom Noms"

    def constrict(self):
        return "Chokeeeeee Time!"

    def climb(self):
        return "Slimy business"

    def shed_skin(self):
        return "Woopty Doopty Fresh Skin!"


# Create an instance of the Python Class
shnake = Python()

# Print out some of the attributes from the Class and its Parents
print(f"Alive: {shnake.alive}")
print(f"Cold Blooded: {shnake.cold_blooded}")
print(f"Venom: {shnake.venom}")
print(f"Two Lungs: {shnake.two_lungs}")
