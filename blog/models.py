from django.conf import settings
from django.db import models
from django.urls import reverse
# à voir par la suite s'il est nécessaire d'importer reverse

class Post(models.Model): #l'auteur sera défini par d'autres données dont un pseudo qui apparaîtra sur l article
    thematique = models.CharField(max_length=100) # il va falloir se referer à une foreign key aussi pour la thematique.
    title = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk}) #A revoir par la suite










