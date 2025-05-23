from django.shortcuts import render, get_list_or_404, get_object_or_404

from profiles.models import Profile


def index(request):
    """
    View function for displaying the list of all profiles.

    Retrieves all Profile objects from the database and renders them
    in the 'profiles/index.html' template.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML page with the list of profiles.
    """
    profiles_list = get_list_or_404(Profile)
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    View function for displaying the details of a specific profile.

    Retrieves the Profile object linked to the user with the given username
    and renders its details in the 'profiles/profile.html' template.

    Args:
        request (HttpRequest): The HTTP request object.
        username (str): The username of the associated user.

    Returns:
        HttpResponse: The rendered HTML page with the profile's details.
    """
    profile = get_object_or_404(Profile, user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
