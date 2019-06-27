from django.shortcuts import render
# from django.views.decorators import csrf

def search_post(request):
    context = {}
    if request.POST:
        print(request.GET)
        print(request.POST)
        print(request.path)
        print(request.method)
        print(request.scheme)
        print(request.body)
        context['rlt'] = request.POST['q']
    return render(request, 'search_post.html', context)

