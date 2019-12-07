import os

import face_recognition
from PIL import Image, ImageDraw
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
def dressing(request):
    if request.method == 'POST':
        r = int(request.POST.get('r',0))
        g = int(request.POST.get('g',0))
        b = int(request.POST.get('b',0))
        img = request.FILES.get('img',None)
        print(img)
        print(type(img))
        if not img:
            print(1)
            return JsonResponse({"result": -3, "data": "error"})
        print(img.name)
        key = str(request.POST.get('key'))+os.path.splitext(img.name)[1]
        print(2)
        path = default_storage.save(img.name, ContentFile(img.read()))
        print(path)
        print(3)
        tmp_file = os.path.join('./', path)
        image = face_recognition.load_image_file(img)
        face_landmarks_list = face_recognition.face_landmarks(image)

        for face_landmarks in face_landmarks_list:
            pil_image = Image.fromarray(image)
            d = ImageDraw.Draw(pil_image, 'RGBA')
            d.polygon(face_landmarks['left_eyebrow'], fill=(r, g, b, 25))
            d.polygon(face_landmarks['right_eyebrow'], fill=(r, g, b, 25))
            d.polygon(face_landmarks['top_lip'], fill=(r, g, b, 25))
            d.polygon(face_landmarks['bottom_lip'], fill=(r, g, b, 25))
        pil_image.save(key)
        with open(key, 'rb') as f:
            response = HttpResponse(f,content_type="image/"+os.path.splitext(img.name)[1][1:])
            response['Content-Disposition'] = 'attachment; filename='+key
        os.remove(key)
        os.remove(img.name)
        return response

    return JsonResponse({"result": 0, "data": "error"})