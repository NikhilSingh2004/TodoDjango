from django.db import models
from datetime import datetime

# ToDo Model that holds the Todo Data

class ToDo(models.Model):

    Date = models.DateTimeField(default = datetime.now(), null=False)

    Discreption = models.TextField(null= True)