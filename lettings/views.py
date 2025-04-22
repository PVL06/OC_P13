from django.shortcuts import render, get_list_or_404, get_object_or_404

from lettings.models import Letting


def index(request):
    """
    View function for displaying the list of all lettings.

    Retrieves all Letting objects from the database and renders them
    in the 'lettings/index.html' template.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML page with the list of lettings.
    """
    lettings_list = get_list_or_404(Letting)
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    View function for displaying the details of a specific letting.

    Retrieves the Letting object matching the provided ID and renders
    its details in the 'lettings/letting.html' template.

    Args:
        request (HttpRequest): The HTTP request object.
        letting_id (int): The ID of the Letting to display.

    Returns:
        HttpResponse: The rendered HTML page with the letting's details.
    """
    letting = get_object_or_404(Letting, id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
