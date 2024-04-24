from django.db import models


class MutuSumu(models.Model):
    mutu_wa_sumu = models.CharField(max_length=255)

    def __str__(self):
        return self.mutu_wa_sumu


class Zina(models.Model):
    mutu_sumu_id = models.ForeignKey(MutuSumu, on_delete=models.CASCADE)
    nambala_ya_sumu = models.IntegerField(default=0)
    zina_la_sumu = models.CharField(max_length=255)
    mlembi = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.zina_la_sumu


class Mizere(models.Model):
    mutu_sumu_id = models.ForeignKey(MutuSumu, on_delete=models.CASCADE, default='')
    zina_id = models.ForeignKey(Zina, on_delete=models.CASCADE)
    nambala = models.IntegerField(default=0)
    mizere = models.TextField()

    def __str__(self):
        return self.mizere
