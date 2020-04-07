from django.contrib import admin

# Register your models here. Qui puoi creare delle classi specifiche per ciascuno dei nostri modelli

from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ["__str__","data"]
    list_filter = ["data"]
    search_fields = ["titolo","contenuto"]
    prepopulated_fields = {"slag": ("titolo",)}
    
class Meta:  #Fornisce alla post admin info sul modello che stiamo utilizzando
    model = Post
    
admin.site.register(Post,PostAdmin) #Aggiungi al pennello di controllo la tua app
