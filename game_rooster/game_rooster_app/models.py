from django.db import models

# Good - serves
class Service(models.Model):
    # CharField(_(""), max_length=50)
    # IntengerField()
    # DateField
    # DateTimeField()
    # FilePathField() - путь до файла

    service_title = models.CharField(max_length = 100)# название
    service_price = models.IntegerField()# цена 
    service_description = models.TextField()# описание
    service_image = models.ImageField()# картинка 

    def __str__(self):
        return f'{self.service_title}'