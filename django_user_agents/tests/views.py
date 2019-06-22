from django.shortcuts import render


def test(request):
    return render(request, "test.html", {'user_agent': request.user_agent})


def test_filters(request):
    return render(request, "test_filters.html", {'request': request})
