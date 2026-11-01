from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Company(models.Model):
    name= models.CharField(max_length=20, unique=True)

    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name

class HSN(models.Model):
    hsn_number = models.IntegerField(max_length=10, unique=True)
    sgst = models.DecimalField(max_digits=5, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    cgst = models.DecimalField(max_digits=5, decimal_places=2, default=0, validators=[MinValueValidator(0)])

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)

    @property
    def gst (self):
        return self.sgst + self.cgst

    class Meta:
        verbose_name = "HSN"
        verbose_name_plural = "HSNs"

    def __str__(self):
        return str(self.hsn_number)

class Product(models.Model):
    name = models.CharField(max_length=30)
    packing = models.CharField(max_length=10, null=True)
    mrp = models.DecimalField(max_digits=5, decimal_places=2)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True, related_name="Product")
    hsn = models.ForeignKey(HSN, on_delete=models.SET_NULL, null=True, blank=True, related_name="Product")
    selling_discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    selling_scheme_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    description = models.TextField(blank=True)
    quantity = models.IntegerField(default=0)
    is_available = models.BooleanField(default=True)


    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)

    def get_company (self):
        return self.company.name

    def __str__(self):
        return f"${self.pk} - {self.name}"


class ProductImages (models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_image')
    image = models.ImageField(upload_to="products/")
    is_primary = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)

    def product_name(self):
        return self.product.name

    class Meta:
        verbose_name_plural = "Product Images"