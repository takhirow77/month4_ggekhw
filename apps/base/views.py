from django.shortcuts import render

from apps.base.models import Settings
from apps.secondary.models import Services,Projects,Education,Skills,Parfolio,Review,Blog
# Create your views here.
def index(request):
    settings = Settings.objects.latest('id')
    services = Services.objects.all()
    projects = Projects.objects.latest('id')
    education = Education.objects.all()
    skills = Skills.objects.all()
    parfolio = Parfolio.objects.all()
    review = Review.objects.all()
    blog = Blog.objects.all()

    return render(request, 'base/index.html', locals())

def contact(request):

    return render(request, 'contact.html', locals() )


def blog(request):
    return render(request, 'blog_list.html', locals())



def blog_details(request):
    return render(request, 'blog_details.html', locals())