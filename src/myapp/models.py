from django.db import models
from django.contrib.auth.models import User


def user_directory_path(instance, filename):
    return 'lawyer/{0}/{1}'.format(instance.author.id, filename)

# class Category(models.Model):
#     name = models.TextField(max_length=100)

#     class Meta:
#         verbose_name_plural = "Categories"

#     def __str__(self):
#         return self.name
    
class Post(models.Model):
    OPTIONS = (
        ('Draft', 'Draft'),
        ('Published', 'Published')
    )
    
    title = models.CharField(max_length=10000)
    content = models.TextField(max_length=2000000)
    image = models.URLField(max_length=100000, blank=True)     #  chARFIELD YA DA URL OLARAK KOYACAGIz
    # under this code category works, but with id not with name. thats whay i dont use on tzhis project
    # category = models.ForeignKey(Category, on_delete = models.PROTECT, blank=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=OPTIONS, default='Published')
    slug = models.SlugField(max_length = 5000, blank=True, unique=True) 

    def __str__(self):
        return self.title
    
    @property
    def comment_count(self):
        return self.comment_set.all().count()

    @property
    def view_count(self):
        return self.postview_set.all().count()
    
    @property
    def like_count(self):
        return self.like_set.all().count()
    
    @property
    def comments(self):
        return self.comment_set.all()


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=2000)

    def __str__(self):
        return self.user.username


class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class PostView(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
