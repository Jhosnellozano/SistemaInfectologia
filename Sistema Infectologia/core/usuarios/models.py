from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import model_to_dict

SEXO_CHOICES = [
        ("M", 'Masculino'),
        ("F", 'Femenino'),
    ]

class Usuario(AbstractUser):
    cedula = models.PositiveIntegerField(null=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=True)
    nivel = models.IntegerField(null=True) 

    @classmethod
    def numeroRegistrados(self):
        return int(self.objects.all().count())
    
    def full_name(self):
        return f"{self.nombre} {self.apellido}"

    def toJSON(self):
        item = model_to_dict(self, exclude=['password', 'user_permissions', 'groups', 'last_login'])
        if self.last_login:
            item['last_login'] = self.last_login.strftime('%Y-%m-%d')
        item['sexo'] = {'value': self.sexo, 'label': self.get_sexo_display()}
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        item['full_name'] = self.get_full_name()
        #item['groups'] = [{'id': g.id, 'name': g.name} for g in self.groups.all()]
        return item
