from django.db import models


class MutuNyimbo(models.Model):
    mutu_wa_nyimbo = models.CharField(max_length=255)

    def __str__(self):
        return self.mutu_wa_nyimbo


class Dzina(models.Model):
    mutu_nyimbo_id = models.ForeignKey(MutuNyimbo, on_delete=models.CASCADE)
    nambara_ya_nyimbo = models.IntegerField(default=0)
    dzina_la_nyimbo = models.CharField(max_length=255)
    olemba = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.dzina_la_nyimbo


class Ndime(models.Model):
    mutu_nyimbo_id = models.ForeignKey(MutuNyimbo, on_delete=models.CASCADE, default='')
    dzina_id = models.ForeignKey(Dzina, on_delete=models.CASCADE)
    nambara = models.IntegerField(default=0)
    ndime = models.TextField()

    def __str__(self):
        return self.ndime
