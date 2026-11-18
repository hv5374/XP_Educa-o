from django.db import models

# Create your models here.
class tasks(models.Model):
    TODO = 'in progress'
    IN_PROGRESS = 'in progress'
    DONE = 'done'

    STATUS_CHOICES = [
        (TODO, 'Para fazer'),
        (IN_PROGRESS, 'Em andamento'),
        (DONE, 'Concluído')
    ]

    title = models.CharField('Título', max_length=100)
    description = models.TextField('Descrição', blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=TODO)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    def __str__(self):
        return f'{self.title} [{self.status}]'