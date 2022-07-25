from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import FileExtensionValidator


USER = get_user_model()


class Tag(models.Model):
    tag = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.tag


class Category(models.Model):
    title = models.CharField(max_length=30)
    parent_category = models.ForeignKey('self', blank = True, null = True, related_name="category", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def get_products(self):
        return Product.objects.filter(category = self)

    def __str__(self):
        return self.title

class Property(models.Model):
    title = models.CharField(max_length=30)
    category = models.ManyToManyField(Category)

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'

    def __str__(self):
        return self.title

class PropertyValue(models.Model):
    title = models.CharField(max_length=30)
    property = models.ForeignKey(Property , on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Property Value'
        verbose_name_plural = 'Property Values'

    def __str__(self):
        return self.title


class Brand(models.Model):
    title = models.CharField('Brand', max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    brand = models.ForeignKey(Brand, null=True, on_delete=models.CASCADE)
    property_value = models.ManyToManyField(PropertyValue)
    category = models.ForeignKey(Category, null=False, blank=False, on_delete=models.CASCADE)
    main_image = models.ImageField(' Main Image', upload_to='media/products', null = True)
    description = models.TextField()
    detail = models.TextField()
    video = models.FileField(upload_to='videos_uploaded',null=True,
            validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    tag = models.ManyToManyField(Tag)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def get_tags(self):
        return Tag.objects.filter(product = self)

    def get_property_values(self):
        return PropertyValue.objects.filter(product = self)

    def __str__(self):
        return self.title

    # def real_price(self):
    #     discount = discount.product_price.all()
    #     print (discount)
    #     return discount
        

class Discount(models.Model):
    value = models.IntegerField()
    is_percentage = models.BooleanField(default=True)
    product = models.ManyToManyField(Product, related_name='product_price')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Discount'
        verbose_name_plural = 'Discounts'

    def __str__(self):
        return str(self.value)


class Review(models.Model):
    product = models.ForeignKey(Product, related_name='comments', on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', verbose_name='Parent Comment', on_delete=models.CASCADE, db_index=True,
                                       related_name='sub_reviews', blank=True, null=True)
    author = models.ForeignKey(USER, on_delete=models.CASCADE, verbose_name='User',
                                        db_index=True,null=True,blank=True, related_name='reviewusers')
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __srt__(self):
        return self.title, self.name


class Image(models.Model):
    image = models.ImageField('Image', upload_to='media/products', null = True , blank=True )
    product = models.ForeignKey(Product, null= True, blank = True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ProductPropertyValue(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    property_value = models.ForeignKey(PropertyValue, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Product Property Value'
        verbose_name_plural = 'Product Property Values'


class Shipping(models.Model):
    phone_number = models.CharField(max_length=15)
    your_mesaage = models.TextField()
    flat_plot = models.CharField(max_length=50, null=True)
    adress = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    region_state = models.CharField(max_length=50)
    user = models.ForeignKey(USER, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Shipping'
        verbose_name_plural = 'Shipping'

    def __srt__(self):
        return self.user



