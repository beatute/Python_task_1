# Sukurkite klasę "Movie", kuri gebės sukurti objektus 3 savybėm ir 1 metodu. 
# Naudojant šią klasę sukurkite bent du skirtingus objektus.

# Savybės:
# title: string
# director: string
# budget: number

# Metodas: 
# wasExpensive() - jeigu filmo "budget" yra daugiau nei 100 000 000 mln USD, tada grąžins True, kitu atveju False. 

class Movie:
    def __init__(self, title, director, budget):
        self.title = title
        self.director = director
        self.budget = budget
    
    def wasExpensive(self):
        print(self.budget > 100000000)

    def __str__(self):
        return f"Movie Title: {self.title}, Movie Director: {self.director}, Movie Budget: {self.budget}"

movie_1 = Movie("Avatar: The Way of Water", "James Cameron", 250000000)
movie_2 = Movie("Violent night", "Tommy Wirkola", 20000000)

movie_1.wasExpensive()
print(movie_1)

movie_2.wasExpensive()
print(movie_2)
   