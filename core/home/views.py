from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def home(request):
    peoples=[
        {'name':'Minhaz Mahmud', 'Age':24},
        {'name':'Rahim Ali', 'Age':25},
        {'name':'Yasin Ali', 'Age':29}
        
    ]

    text = """
    Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellendus itaque ducimus
    non soluta assumenda ullam ad at magni excepturi, tenetur pariatur, 
    delectus maiores et, dolores placeat officia quis enim aut.
    """
    return render(request,"index.html",context = {'peoples' : peoples,'text' :text})

def success_page(request):
    print('*' * 10)
    return HttpResponse("Hey this is a success page.")  
  

# def login_page(request):
#     return render(request,'login.html')
