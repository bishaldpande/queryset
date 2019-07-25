import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'query_testing.settings')

import random
import django
# Import settings
django.setup()

from book.models import Genre, Author, Publisher, Book
from faker import Faker

fake = Faker('en_GB')

def populate():

    # for authors
    for _ in range(100):
        Author.objects.create(
            first_name=fake.first_name(), 
            last_name=fake.last_name(), 
            email=fake.email()
            )
    genres = ['Action', 'Crime', 'Drama', 'Fiction', 'Science fiction', 'Horror', 'Thriller', 'Fairytale', 'Adventure', 'Biography']
    for g in genres:
        Genre.objects.create(name=g)

    # for publisher
    for _ in range(100):
        Publisher.objects.create(
            name=fake.company(),
            address=fake.address(),
            website=fake.url()
            )

    # for books

    for _ in range(10000):
        book = Book(title=fake.sentence())
        
        choices = range(1, 101)

        book.publisher_id = random.choice(range(1,101))
        book.genre_id = random.choice(range(1,11))
        
        book.price = random.randint(10, 500)
        book.published_date = fake.past_date(start_date="-100y")
        book.save()
        
        no_choice = [1,2,3,4,5]
        authors = random.choices(choices, k=random.choice(no_choice))
        book.author.add(*authors)
        book.save()
        if _%100==0:
            print(f'{_} objects created')

if __name__ == "__main__":
    print("Populating the databases...Please Wait")
    populate()
    print('Populating Complete')