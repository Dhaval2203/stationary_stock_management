from django.db import models

# # Create your models here.
class registation(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    email=models.EmailField()
    password1=models.CharField(max_length=50)
    question=models.CharField(max_length=100)
    answer=models.CharField(max_length=100)

    class Meta:
        db_table='registation'

# class a_registation(models.Model):
#     email=models.EmailField()
#     password=models.CharField(max_length=50)
#     class Meta:
#         db_table='a_registation'

# class a_login(models.Model):
#     email=models.EmailField()
#     password=models.CharField(max_length=50)

#     class Meta:
#         db_table='a_login'
class Contact(models.Model):
    c_id=models.AutoField(primary_key=True)
    c_name=models.CharField(max_length=50)
    c_email=models.EmailField()
    c_phoneno=models.IntegerField()
    c_subject=models.CharField(max_length=50)
    c_massage=models.TextField()
    class Meta:
        db_table='contact'

class Stocks(models.Model):
    p_id=models.AutoField(primary_key=True)
    p_name=models.CharField(max_length=50)
    p_category=models.CharField(max_length=50)
    p_company=models.CharField(max_length=50)
    p_img=models.ImageField()
    stock=models.IntegerField()
    price=models.IntegerField()

    class Meta:
        db_table='stocks'

class Cart(models.Model):
    p_id=models.AutoField(primary_key=True)
    p_name=models.CharField(max_length=50)
    p_category=models.CharField(max_length=50)
    p_company=models.CharField(max_length=50)
    p_img=models.ImageField()
    stock=models.IntegerField()
    price=models.IntegerField()

    class Meta:
        db_table='cart'
