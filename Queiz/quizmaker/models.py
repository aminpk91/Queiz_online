from django.db import models

# Create your models here.

class A (models.Model):
    tags = (('pol', 'politics'),
            ('sprt', 'sports'),
            ('eco', 'economics'),
            ('cul', 'cultural'),
            ('soc', 'social')
            )

    choice = models.TextField()
    category = models.CharField(max_length=4, choices=tags)

    def __str__(self):
        return self.choice

class Q (models.Model):
    tags = (('pol','politics'),
          ('sprt', 'sports'),
          ('eco', 'economics'),
          ('cul', 'cultural'),
          ('soc', 'social')
          )

    question = models.TextField()
    category = models.CharField(max_length=4,choices=tags)
    answer = models.ForeignKey(A,on_delete=models.CASCADE)



    def __str__(self):
        return self.question


class U (models.Model):

    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name

class Quiz (models.Model):

    user = models.ForeignKey(U,on_delete=models.CASCADE)
    listQ = models.TextField()
    score = models.FloatField(default=0)