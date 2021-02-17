from django.db import models
from django.urls import reverse

class Task(models.Model):
    task = models.CharField(max_length=240)   
    inclusion_date = models.DateField( auto_now=False, auto_now_add=True)
    finish_date = models.DateField(blank=True, null=True)


    class Meta:
        verbose_name = ("Task")
        verbose_name_plural = ("Tasks")

    def __str__(self):
        return self.task

    def get_absolute_url(self):
        return reverse("Task_detail", kwargs={"pk": self.pk})
