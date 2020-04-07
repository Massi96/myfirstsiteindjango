from django.urls import path, re_path
from . import views as post_views
from django.views.generic import ListView,DetailView
from .models import Post

#Il flusso di dati è: myblog/urls -> post/urls -> (vedi sotto)
#lista dei post| homepage del blog
#post singoli del blog
#sezione contatti
#in questa sezione definiamo le pagine della mia app, ogni path andrà a richiamare
#una funzione di views.py che renderizza,cioè mostra l'html di un modello (models.py)

urlpatterns = [
    path('',ListView.as_view(
        queryset = Post.objects.all().order_by("-data"),
        template_name = "lista_post.html",
        paginate_by = 5),name="lista"),
    
    re_path(r'^(?P<pk>\d+)/(?P<slag>[\w-]+)/$', DetailView.as_view(
        model = Post,
        template_name = "post_singolo.html"),name="singolo"),
    
    path('contatti',post_views.contatti,name="contatti")
] 