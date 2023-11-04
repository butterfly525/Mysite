from django.db import models

# Create your models here.

class StyleCard(models.Model):
    nameStyle = models.CharField('Название', max_length=50)
    codeHTML = models.TextField('HTML')
    codeCSS = models.TextField('CSS')
    codeJS = models.TextField('JS')
    dateCreation = models.DateField('Дата создания карточки')

    def __str__(self):
        return self.nameStyle

    class Meta:
        verbose_name = 'Карточка стиля'  #единственное число названия класса для отображения на русском языке
        verbose_name_plural = 'Карточки стилей' #единственное число названия класса для отображения на русском языке

