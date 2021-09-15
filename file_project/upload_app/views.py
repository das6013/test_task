from django.shortcuts import render
from PIL import Image
from .models import wimag
from django.core.files.storage import FileSystemStorage
from django.views.generic import CreateView
from .forms import IForm
class Bcreate(CreateView):
    model=wimag
    form_class = IForm
    template_name = 'work.html'
    success_url = '/kek'


def hex_to_rgb(string):
    string=string.lstrip('#')
    return list(int(string[i:i+2], 16) for i in (0, 2, 4))
def count_color(img,color):
    count=0
    height, width = img.size
    rgb_img = img.convert('RGB')
    for i in range(0, height):
        for j in range(0, width):
            r, g, b = rgb_img.getpixel((i,j))
            if color==[r,g,b]:
                count+=1
    return count
def white_or_black(img):  #White-0 Black-1 ==2
    if count_color(img,[255,255,255])> count_color(img,[0,0,0]):
        return 'Больше белых пикселей'
    elif count_color(img,[255,255,255])< count_color(img,[0,0,0]):
        return 'Больше черных пикселей'
    else:
        return 'черных и белых пикселей одинаковое колличество'


def home_page(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = IForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            im=Image.open(img_obj.cover)
            count=white_or_black(im)
            color=hex_to_rgb(img_obj.Hex)
            color_c=count_color(im,color)


            return render(request, 'home_page.html', {'form': form, 'img_obj': img_obj,'count':count,"color_c":color_c,})
    else:
        form = IForm()


    return render(request, 'home_page.html', {'form': form})
