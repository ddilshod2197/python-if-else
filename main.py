class Arxitektor:
    def __init__(self, ism, familiya, tajriba):
        self.ism = ism
        self.familiya = familiya
        self.tajriba = tajriba

    def ishlaydi(self):
        return f"{self.ism} {self.familiya} ishlaydi va {self.tajriba} yili tajriba qilgan."

class Google:
    def __init__(self, nom):
        self.nom = nom

    def ishlaydi(self, arxitektor):
        return f"{self.nom}da {arxitektor.ism} {arxitektor.familiya} ishlaydi."

class Meta:
    def __init__(self, nom):
        self.nom = nom

    def ishlaydi(self, arxitektor):
        return f"{self.nom}da {arxitektor.ism} {arxitektor.familiya} ishlaydi."

# Arxitektor yaratish
arxitektor = Arxitektor("Ali", "Valiyev", 10)

# Google va Meta yaratish
google = Google("Google")
meta = Meta("Meta")

# Arxitektor ishlaydi
print(arxitektor.ishlaydi())

# Arxitektor Google va Meta da ishlaydi
print(google.ishlaydi(arxitektor))
print(meta.ishlaydi(arxitektor))
