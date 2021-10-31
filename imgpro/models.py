from django.db import models


# create categories model
class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return str(self.title)

    class Meta:
        db_table = 'Category'


# images Model
class ImageDB(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='image')
    uploaded_date = models.DateField(auto_now_add=True)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'Images_Data'
