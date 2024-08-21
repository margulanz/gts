from django.db import models

class Tag(models.Model):
    class Meta:
        managed = False
        db_table = "posts_tag"
    name = models.CharField(max_length = 15, verbose_name="Название тэга")

    def __str__(self):
        return self.name

class Category(models.Model):
    class Meta:
        managed = False
        db_table = "posts_category"
    name = models.CharField(max_length = 100, verbose_name="Название категории")

    def __str__(self):
        return self.name



class Post(models.Model):
    class Meta:
        managed = False
        db_table = "posts_post"
    title = models.CharField(unique = True,max_length = 100, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Контент")
    slug = models.SlugField(default="", unique=True, blank = True)
    pub_date = models.DateTimeField(auto_now_add = True,verbose_name="Дата публикации", null = True, blank = True)
    tags = models.ManyToManyField(Tag, verbose_name="Теги")
    category = models.ForeignKey(Category, on_delete = models.DO_NOTHING, verbose_name="Категория")