from django.db import models

# Create your models here.
class User(models.Model):

    username = models.CharField(max_length=120)
    password = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = ("User")
        verbose_name_plural = ("Users")

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("User_detail", kwargs={"pk": self.pk})


class NotesDb(models.Model):
    title = models.CharField(max_length=25, blank=True, null=True)
    content = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notes_db'