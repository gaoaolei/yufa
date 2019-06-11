from django.shortcuts import render
# from django.views.decorators import csrf

def search_post(request):
    context = {}
    if request.POST:
        print(request.GET)
        print(request.POST)
        print(request.path)
        print(request.method)
        context['rlt'] = request.POST['q']
    return render(request, 'post.html', context)

