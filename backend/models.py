from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='projects')
    link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images/')

    def __str__(self):
        return f'{self.project.title} Image'


class User(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    email = models.EmailField()
    resume = models.FileField(upload_to='user_files/')
    link = models.URLField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    about_me = models.TextField()

    def __str__(self):
        return self.name


class UserImage(models.Model):
    user = models.ForeignKey(User, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='user_images/')
    logo = models.ImageField(upload_to='user_images/')

    def __str__(self):
        return f'{self.user.name} Image'


class Skills(models.Model):
    user = models.ForeignKey(User, related_name='skills', on_delete=models.CASCADE)
    skill = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f'{self.user.name} Skill'


class Experience(models.Model):
    user = models.ForeignKey(User, related_name='experiences', on_delete=models.CASCADE)
    experience = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f'{self.user.name} Experience'
