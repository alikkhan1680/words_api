from django.db import models



class Iregulars(models.Model):# iregular verblarnni so'zlarni alohida yozish uchun ishlatilingan model
    base = models.CharField(max_length=100, blank=True, verbose_name='Base form (present)')
    past = models.CharField(max_length=50, blank=True, verbose_name="past simple")
    pp = models.CharField(max_length=50, blank=True, verbose_name="Past Participle")
    translation = models.CharField(max_length=100, null=True, blank=True, verbose_name="Translation")
    example = models.TextField(null=True, blank=True, verbose_name="Example sentence")

    def __str__(self):
        return self.base



class Grammar(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    level = models.CharField(max_length=100, null=True, blank=True)
    descriptions = models.ManyToManyField("GrammarDescriptions", blank=True)
    exemple = models.ManyToManyField('GrammarExemple', blank=True)
    picture = models.ManyToManyField('GrammarImg', blank=True)

    def __str__(self):
        return self.title


class GrammarDescriptions(models.Model):
    descriptions = models.TextField()
    name_number = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return self.name_number




class GrammarExemple(models.Model):
    exemple = models.TextField()
    name_number = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return self.name_number



class GrammarImg(models.Model):
    image = models.ImageField(upload_to='grammar_images/', blank=True, null=True)  # Rasm
    name_number = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return self.name_number

