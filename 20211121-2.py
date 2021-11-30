class Book:
    akcija = 1.4

    def __init__(self, title, metai, kaina):
        self.title = title
        self.metai = metai
        self.kaina = kaina

    def full_name(self):
        return f'{self.title},{self.metai}'

    def mazinti_kaina(self):
        self.kaina = self.kaina - self.akcija

if __name__ == "__main__":

    knyga_1 = Book("python", 2000, 20)
    print(knyga_1.title)
    pavadinimas = knyga_1.full_name()
    print(pavadinimas)
    print

