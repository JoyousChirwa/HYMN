from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import (
    Header, Title, Stanza,
    #MutuSumu, Zina,
    #MutuNyimbo, Dzina
)

def index(request):
    hymns = Header.objects.all
    return render(request, 'hymns/index.html', {'hymns': hymns, 'bg_color': "bg-primary", 'brand_name': "HYMNS", 'brand_url': "/hymns/"})

def create(request):
    pass

def search(request):
    #try:
    search_text = request.POST['search']
    #if search_text != '':
        #hymn = get_object_or_404(Title, hymn_number=search_text)
        #return render(request, 'hymns/details.html', {'hymn': hymn})
    #except Title.DoesNotExists:
    if search_text != '': #or error:
        try:
            hymn_s = Title.objects.get(hymn_number=search_text)
        except Title.DoesNotExist:
            hymn_s = ""
        # try:
        #     sumu = Zina.objects.get(nambala_ya_sumu=search_text)
        # except Zina.DoesNotExist:
        #     sumu = ""
        # try:
        #     nyimbo = Dzina.objects.get(nambara_ya_nyimbo=search_text)
        # except Dzina.DoesNotExist:
        #     nyimbo = ""
        # Need to check individual variables if they are empty if not send them to template  'sumu': sumu, 'nyimbo': nyimbo,
        return render(request, 'hymns/details.html', {'hymn_s': hymn_s,  'bg_color': "bg-primary", 'brand_name': "HYMNS", 'brand_url': "/hymns/"})
    else:
        return render(request, 'hymns/details.html', {'error': "Please enter a number or text", 'bg_color': "bg-primary", 'brand_name': "HYMNS", 'brand_url': "/hymns/"})
        #return redirect(reverse('hymns:home'))

# def sumu(request):
#     sumu = MutuSumu.objects.all
#     return render(request, '/sumu/templates/sumu/index.html', {'sumu': sumu})
#
# def nyimbo(request):
#     nyimbo = MutuNyimbo.objects.all
#     return render(request, '/nyimbo/templates/nyimbo/index.html', {'nyimbo': nyimbo})

def details(request, header_id):
    hymn = get_object_or_404(Header, pk=header_id)
    return render(request, 'hymns/details.html', {'hymn': hymn})