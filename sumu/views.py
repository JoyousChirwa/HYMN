from django.shortcuts import render

from sumu.models import MutuSumu, Zina


def index(request):
    sumu = MutuSumu.objects.all
    return render(request, 'sumu/index.html', {'sumu': sumu, 'bg_color': "bg-success", 'brand_name': "SUMU ZA UKHRISTU", 'brand_url': "/sumu/"})


def fumba(request):
    try:
        fumbo = request.POST['fumbo']
        if fumbo != '':
            sumu = Zina.objects.get(nambala_ya_sumu=fumbo)
            return render(request, 'sumu/result.html', {'sumu': sumu, 'bg_color': "bg-success", 'brand_name': "SUMU ZA UKHRISTU", 'brand_url': "/sumu/"})
    except Zina.DoesNotExist:
        return render(request, 'sumu/result.html', {'suzgo': "SUMU " + fumbo + " MULIJE PANYAKE MULIVE", 'bg_color': "bg-success", 'brand_name': "SUMU ZA UKHRISTU", 'brand_url': "/sumu/"})
