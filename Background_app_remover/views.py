# views.py

from django.shortcuts import render
from .forms import ImageUploadForm
from PIL import Image as PILImage
from rembg import remove
from django.http import HttpResponse
import io

def remove_background(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            original_image = request.FILES['image']
            img = PILImage.open(original_image)
            img = img.convert("RGBA")
            img = remove(img)
            processed_image_io = io.BytesIO()
            img.save(processed_image_io, format='PNG')
            processed_image_io.seek(0)

            filename = 'processed_image.png'

            # Create an HTTP response with the processed image
            response = HttpResponse(processed_image_io, content_type='image/png')

            # Set the Content-Disposition header to prompt download with the specified filename
            response['Content-Disposition'] = f'attachment; filename="{filename}"'

            return response
            
    else:
        form = ImageUploadForm()
    return render(request, 'image_processing_app/process_image.html', {'form': form})




def Home(request):
    return render(request, 'index.html')