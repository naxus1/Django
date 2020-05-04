from django.db import models

# Create your models here.
class Toy(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150, blank=False, default='')
    description = models.CharField(max_length=250, blank=True, default='')
    toy_category = models.CharField(max_length=200, blank=False, default='')
    release_date = models.DateTimeField()
    was_inluded_in_home = models.BooleanField(default=False)

    

    class Meta:
        verbose_name = ("Toy")
        verbose_name_plural = ("Toys")
        ordering = ('name',)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Toy_detail", kwargs={"pk": self.pk})
