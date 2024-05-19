from django.db import models
import datetime

#Categories of Products - class and then the attributes
class Category(models.Model):
	name = models.CharField(max_length=50)

	#Needs this for it to appear on the website
	def __str__(self): 
		return self.name

	#Make 'categorys' be displayed as 'categories'
	class Meta:
		verbose_name_plural ='categories'

#Employee
class Employee(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	employeeID = models.CharField(max_length=30)
	address = models.CharField(max_length=100, blank=True)
	phone = models.CharField(max_length=10, blank=True)
	email = models.EmailField(max_length=100)
	password = models.CharField(max_length=100)
	gender = models.CharField(max_length=20)
	dateOfBirth = models.CharField(max_length=50)
	position = models.CharField(max_length=50)
	#is_ceo = models.BooleanField(default=False)
	#is_dev = models.BooleanField(default=False)
	#is_hr = models.BooleanField(default=False)
	#is_supervisor = models.BooleanField(default=False)
	#salary = models.DecimalField(default=0, decimal_places=2, max_digits=9, blank=True)
	#hireDate = models.CharField(max_length=50, blank=True)

	def __str__(self):
		return f'{self.first_name} {self.last_name}'

#Employee positions (1=CEO, 2=Dev, 3=HR, 4=Supervisor, 5=Regular Employee)
class Positions(models.Model):
	employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
	ceo = models.IntegerField(default=1)
	dev = models.IntegerField(default=2)
	hr = models.IntegerField(default=3)
	supervisor = models.IntegerField(default=4)
	regularEmployee = models.IntegerField(default=5)

#All of our products
class Product(models.Model):
	name = models.CharField(max_length=100)
	price = models.DecimalField(default=0, decimal_places=2, max_digits=8)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
	description = models.CharField(max_length=250, default='', blank=True, null=True)
	image = models.ImageField(upload_to='uploads/product/')
	#Add Sale attributes. Video #4 has adding boxes to the website


	def __str__(self):
		return self.name

#Employee orders
class Order(models.Model):
	#Foreign key on the product model (i.e. Product class)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	
	#Foreign key on the employee model (i.e. Employee class)
	employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

	quantity = models.IntegerField(default=1)
	addresss = models.CharField(max_length = 100, default='', blank=True)
	phone = models.CharField(max_length=20, default='', blank=True)
	date = models.DateField(default=datetime.datetime.today)
	status = models.BooleanField(default=False)

	def __str__(self):
		return self.product


