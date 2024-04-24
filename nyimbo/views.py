from django.shortcuts import render

from nyimbo.models import MutuNyimbo, Dzina


def index(request):
    nyimbo = MutuNyimbo.objects.all
    return render(request, 'nyimbo/index.html', {'nyimbo': nyimbo, 'bg_color': "bg-info", 'brand_name': "NYIMBO ZA MULUNGU", 'brand_url': "/nyimbo/"})


def funsa(request):
    try:
        funso = request.POST['funso']
        if funso != '':
            nyimbo = Dzina.objects.get(nambara_ya_nyimbo=funso)
            return render(request, 'nyimbo/result.html', {'nyimbo': nyimbo, 'bg_color': "bg-info", 'brand_name': "NYIMBO ZA MULUNGU", 'brand_url': "/nyimbo/"})
    except Dzina.DoesNotExist:
        return render(request, 'nyimbo/result.html', {'vuto': "NYIMBO " + funso + " MULIBE", 'bg_color': "bg-info", 'brand_name': "NYIMBO ZA MULUNGU", 'brand_url': "/nyimbo/"})

