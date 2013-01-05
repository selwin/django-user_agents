from django.shortcuts import render


def test(request):
    return render(request, "test.html", {'user_agent': request.user_agent})