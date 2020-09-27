from django.db import models
from django.contrib.auth.models import User
# Create your models here
class Category(models.Model):
    title = models.CharField(max_length=30)
    primaryCategory = models.BooleanField(default=False)

    def __str__(self):
        return self.title
class  Product(models.Model):
    mainimage = models.ImageField(upload_to='products/', blank=True)
    name = models.CharField(max_length=300)
    slug = models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    preview_text = models.TextField(max_length=20, verbose_name='Preview Text')
    detail_text = models.TextField(max_length=100, verbose_name='Detail Text')
    price = models.FloatField()
    

    def __str__(self):
        return f'{self.name} {self.price}'


# Cart Model
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.quantity}  {self.item.name}'

class Order(models.Model):
    orderitems  = models.ManyToManyField(Cart)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    def get_parents(Cart):
        return ",".join([str(p) for p in Cart.orderitems.all()])

    def __str__(self):
        return self.user.username