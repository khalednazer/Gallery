from django.db import models
from django.utils.text import slugify

# Create your models here.

class Cat(models.Model):
    name = models.CharField(max_length=28)
    def __str__(self) -> str:
        return self.name

class Phot(models.Model):
    count = 1
    desc = models.CharField(max_length=200, null=True)
    catg = models.ForeignKey(Cat,on_delete=models.SET_NULL, null=True, blank=True, related_name='oks')
    create = models.CharField(null=True, max_length=30, blank=True)
    img = models.ImageField(null=True)
    slug = models.SlugField(null=True, blank=True)
    def __str__(self) -> str:
        return self.desc
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.desc)
            slug = base_slug
            count = 1
            while Phot.objects.filter(slug = slug).exists(): 
                slug = base_slug + '_'+ str(count)
                count +=1
            self.slug = slug
        if self.catg is None:
            newCategory= self.create
            data=Cat.objects.create(name =newCategory) 
            self.catg =data
        super().save(*args, **kwargs)
                
# اريد CheckboxSelectMultiple بها كل Cat و عند اختيار اي عنصر يظهر لي جميع العناصر من Phot التي قيمت catg خاصتها تساوي العنصر الذي اخترته 
