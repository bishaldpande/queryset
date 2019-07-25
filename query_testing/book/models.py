from django.db import models

# Create your models here.


class Genre(models.Model):
	name = models.CharField(max_length=100)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name


class Author(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.EmailField(null=True, blank=True)

	def __str__(self):
		return f'{self.first_name} {self.last_name}'


class Publisher(models.Model):
	name = models.CharField(max_length=100)
	address = models.CharField(max_length=255)
	website = models.URLField(null=True, blank=True)

	def __str__(self):
		return self.name


class Book(models.Model):
	title = models.CharField(max_length=100)
	genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
	publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
	author = models.ManyToManyField(Author)
	price = models.IntegerField()

	published_date = models.DateField()

	def __str__(self):
		return self.title
