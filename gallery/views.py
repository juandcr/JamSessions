from django.shortcuts import render
from .models import Gallery
# Create your views here.

def gallery(request):
    photos= Gallery.objects.filter(active=True)
    
    grid=[[],[],[],[]]
    renderGallery=photos.exists()

    while(photos.exists()):        
        count= (4,photos.count()) [photos.count()<4]
        for i in range(count):
            photo= photos.first()
            grid[i].append(photo)            
            photos=photos.exclude(pk=photo.pk)    
    context={
        'grid1':grid[0],
        'grid2':grid[1],
        'grid3':grid[2],
        'grid4':grid[3],
        'renderGallery':renderGallery,
        
    }
    return render(request,'gallery/gallery.html',context)