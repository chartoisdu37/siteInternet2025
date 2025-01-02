# pages/views.py
from django.views.generic import TemplateView
from blog.models import Post
from django.forms import ModelForm
from django.shortcuts import render


# Créer le formulaire directement à partir du modèle si non défini dans forms.py
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['thematique', 'title', 'author', 'body']

def post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()  # Enregistre directement l'objet dans la base de données
            return render(request, '#')  # Page de confirmation ou redirection
    else:
        form = PostForm()

    return render(request, 'home.html', {'form': form})


class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'





