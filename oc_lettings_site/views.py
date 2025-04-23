from django.shortcuts import render


def index(request):
    """
    View function for rendering the homepage.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered homepage HTML.
    """
    return render(request, 'index.html')


def error_500(request):
    raise Exception("Error 500")
