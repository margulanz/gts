from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify

class Tag(models.Model):
    name = models.CharField(max_length = 15, verbose_name="Название тэга")

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length = 100, verbose_name="Название категории")

    def __str__(self):
        return self.name

class Post(models.Model):
    STATUS = (
        (True, "Опубликовано"),
        (False, "Не опубликовано")
    )
    title = models.CharField(unique = True,max_length = 100, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Контент")
    slug = models.SlugField(default="", unique=True, blank = True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.DO_NOTHING)
    pub_date = models.DateTimeField(auto_now_add = True,verbose_name="Дата публикации", null = True, blank = True)
    edit_date = models.DateTimeField(auto_now = True,null = True, blank = True,verbose_name="Дата изменения")
    tags = models.ManyToManyField(Tag, verbose_name="Теги")
    category = models.ForeignKey(Category, on_delete = models.DO_NOTHING, verbose_name="Категория")
    status = models.BooleanField(choices = STATUS,default = True, verbose_name="Статус")

    def save(self, *args, **kwargs):
        if not self.id and not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)