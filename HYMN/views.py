from django.shortcuts import render


def index(request):
    return render(request, 'home.html', {'brand_name': "HYMNS OF MALAWI", 'brand_url': "/", })  # 'bg_color': "bg-home"})
