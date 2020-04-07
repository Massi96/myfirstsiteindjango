from django.db import models
from django.urls import reverse

# Create your models here.In questo file definiamo come la nostra app sia,è giusto pensare a ciascun modello
#come una tabella del nostro database e ogni campo non è altro che una colonna

class Post(models.Model):
    titolo = models.CharField(max_length=120)       #Per il tipo di campo guarda la doc
    contenuto = models.TextField()
    data = models.DateTimeField(auto_now=False, auto_now_add=True)
    slag = models.SlugField()
    
    def __str__(self):
        return self.titolo
    
    #ottenere l'url di un post singolo
    def get_absolute_url(self):
        return reverse("singolo", kwargs={"pk": self.pk,"slag": self.slag})
    