from django.shortcuts import render


def display(request):
    context ={
        'name':'patil'
    }
    return render(request, 'index.html', context=context)