from django.shortcuts import render
from .forms import EntryForm
from .models import EntryModel,SiteModel


# Create your views here.
def home_view(request):
    form = EntryForm()
    context = {
        "form":form,
        "sites":SiteModel.objects.all()
    }
    if request.method == "POST":
        form = EntryForm(request.POST)
        if form.is_valid():
            name    = form.cleaned_data["name"]
            url     = form.cleaned_data["url"]
            email   = form.cleaned_data["email"]
            price   = form.cleaned_data["price"]
            site = SiteModel.objects.filter(name=name).first()
            EntryModel.objects.create(site=site,url=url,price=price,email=email)
    return render(request,"index.html",context)