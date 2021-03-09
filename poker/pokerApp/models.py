from django.db import models


def upload_image(instance, filename):
    """
    Upload an image
    :param instance: player
    :param filename: file
    :return: image route
    """
    return './users/' + str(instance.id) + '/' + filename


class Player(models.Model):  # extends model
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=60)
    password = models.CharField(max_length=30, default="pestillo01")
    nick = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    country = models.CharField(max_length=30, null=True)
    money = models.IntegerField()
    matches = models.ManyToManyField('Match')
    avatar = models.ImageField(upload_to=upload_image)


    def get_id(self):
        return self.id

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def __str__(self):
        return str(self)


class Match(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    money = models.IntegerField()
    players = models.ManyToManyField('Player')
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.money} {self.date}"
