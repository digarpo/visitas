from django.db import models
from django.template.defaultfilters import slugify
from django.conf import settings
from datetime import date
from ..usuarios.models import User


class Docs(models.Model):
    name = models.CharField(max_length=500)
    validate = models.BooleanField(default = False)


class DocUser(models.Model):
    ANEXO = (
                ('FA', 'FA'),
                ('FB', 'FB'),
                ('F1','F1'),
                ('F2','F2'),
                ('F3','F3'),
                ('F4','F4'),
                ('F5','F5'),
                ('F6','F6'),
                ('F7','F7'),
                ('F8','F8'),
                ('F9','F9'),
                ('F10','F10'),
                ('F11','F11'),
                ('F12','F12'),
                ('F13','F13'),
                ('F14','F14'),
                ('F15','F15'),
                ('F16','F16'),
                ('F17','F17'),
                ('F18','F18'),
                ('F19','F19'),
                ('F20','F20'),
                ('F21','F21'),
                ('F22','F22'),
                ('F23','F23'),
                ('F24','F24'),
                ('F25','F25'),
                ('F26','F26'),
                ('IA','IA'),
                ('IB','IB'),
                ('I1','I1'),
                ('I2','I2'),
                ('I3','I3'),
                ('I4','I4'),
                ('I5','I5'),
                ('I6','I6'),
                ('I7','I7'),
                ('IA8','IA8'),
                ('IA9','IA9'),
                ('IA10','IA10'),
                ('IA11','IA11'),
                ('IA12','IA12'),
                ('IA13','IA13'),
                ('IA14','IA14'),
                ('IA15','IA15'),
                ('IA16','IA16'),
                ('IA17','IA17'),
                ('IA18','IA18'),
                ('IA19','IA19'),
                ('IA20','IA20'),
                ('IA20','IA20'),
                ('IA21','IA21'),
                ('IA22','IA22'),
                ('IA23','IA23'),
                ('IA24','IA24'),
                ('IA25','IA25'),
                ('IA26','IA26'),
                ('IA27','IA27'),
                ('IA28','IA28'),
                ('IA29','IA29'),
                ('IA30','IA30'),

    )
    doc = models.ForeignKey(Docs)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,blank=True, null=True)
    type_doc = models.CharField(max_length=2,choices=ANEXO, default='FA')
    docfile = models.FileField(upload_to='docfile',blank=True)
    read = models.BooleanField(default = False)









