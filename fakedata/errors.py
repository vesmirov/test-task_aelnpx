from django.shortcuts import render


def page_not_found(request, exception):
    return render(
        request, 'misc/404.html', {'path': request.path}, status=404)


def forbidden(request, exception):
    return render(request, 'misc/403.html', status=403)


def server_error(request):
    return render(request, 'misc/500.html', status=500)
