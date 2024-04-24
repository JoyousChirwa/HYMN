from django.db import models


class Header(models.Model):
    header_text = models.CharField(max_length=255)

    def __str__(self):
        return self.header_text


class Title(models.Model):
    header_id = models.ForeignKey(Header, on_delete=models.CASCADE)
    hymn_number = models.IntegerField(default=0)
    hymn_title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.hymn_title


class Stanza(models.Model):
    header_id = models.ForeignKey(Header, on_delete=models.CASCADE, default='')
    title_id = models.ForeignKey(Title, on_delete=models.CASCADE)
    stanza_number = models.IntegerField(default=0)
    stanza_text = models.TextField()

    def __str__(self):
        return self.stanza_text
