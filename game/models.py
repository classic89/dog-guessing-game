from django.db import models, momtestpenny

class Question(models.Model):
    question_text = models.ForeignKey(Answer, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date played')
    choice = models.BooleanField(default=False)
    user_id = models.ForeignKey(momtestpenny.settings.AUTH_USER_MODEL)

class Answer(models.Model):
    answer = models.CharField(max_length=200)
    choice_text = models.CharField(max_length=200)
    pet_id = models.ForeignKey(Pet, on_delete=models.CASCADE)
    percent = models.IntegerField(default=0)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

class Image(models.Model):
    filepath = models.FilePathField()
    image = models.ImageField()
    alt = models.TextField()
    file_name = models.CharField(max_length=200)

class Pet(models.Model):
    pet_name = models.CharField(max_length=200)
    height = models.IntegerField()
    weight = models.IntegerField()
    birthday = models.DateField('birthday')
    embark_url = models.URLField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)

class Breed(models.Model): 
    name = models.CharField(max_length=200)
    avg_height = models.IntegerField()
    avg_weight = models.IntegerField()
    avg_life = models.IntegerField()
    group = models.CharFiel(max_length=200)
    akc_year = models.IntegerField()
    description = models.TextField()
    image = models.ForeignKey(Answer, on_delete=models.CASCADE)


    
