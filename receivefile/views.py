import uuid

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def upload(request):
    random_file_name = str(uuid.uuid4())[0:3]

    uploaded_file = request.FILES['file']
    print("[+] request upload", uploaded_file)


    if request.method == "POST":
        print(request.FILES.get('file'))
        byte_data = request.FILES['file'].read()
        with open("upload/" + random_file_name + "_" + uploaded_file.name, "wb+") as f:
            f.write(byte_data)
            print("[+] file is upload success!")

        return HttpResponse("ok")
    else:
        return HttpResponse("only post call")
