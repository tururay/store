from django.db import models

class StaticPages(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name="Título")
    content = models.TextField(null=False, blank=False, verbose_name="Conteúdo")
    page_id = models.CharField(max_length=15, unique=True, null=False, blank=False, verbose_name="Identificador")