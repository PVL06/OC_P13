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
    """
    Handle 500 server error.

    This view function is called when a 500 server error occurs. It raises an
    exception to simulate the error.

    Args:
        request (HttpRequest): The HTTP request object.

    Raises:
        Exception: Always raises an exception with the message "Error 500".
    """
    raise Exception("Error 500")
