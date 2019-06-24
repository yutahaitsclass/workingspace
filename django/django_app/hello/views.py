from django.shortcuts import render
from django.http import HttpResponse

# def index(request, id, name):
    # return HttpResponse("Hello Django")
    # if "msg" in request.GET:
    #     msg = request.GET["msg"]
    #     result="url:http://localhost:8000/hello/?msg=" + msg
    # else:
    #     result = "please send id and name parameter"
        
    # return HttpResponse(result)
    # result = "url: http://localhost:8000/hello/" + str(id) + name
    # return HttpResponse(result)
def index(request):
    params = {
        "title": "hello/index",
        "msg": "messgae",
        # "goto": "next",
        
    }

    return render(request,"hello/index.html",params)
def next(request):
    params = {
        "title": "hello/next",
        "msg": "message2",
        # "goto":"index",
        }
    return render(request, "hello/index.html", params)
    
def form(request):
    msg = request.POST["msg"]
    params = {
            "title": "hello/form",
            "msg": msg,
        }
    return render(request, "hello/index.html", params)
    

