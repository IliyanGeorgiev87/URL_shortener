from django.shortcuts import render, redirect, get_object_or_404
import uuid
from .models import LinkInfo
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def add(request):
    if request.method == "POST":
        link = request.POST['link']
        link_id = str(uuid.uuid4())[:5]
        new_link = LinkInfo(link=link, link_id=link_id)
        new_link.save()

        return HttpResponse(link_id)

def shorten(request, pk):
    link_info = get_object_or_404(LinkInfo, link_id=pk)
    return redirect(link_info.link)