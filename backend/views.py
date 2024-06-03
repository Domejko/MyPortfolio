from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Project, Tag, User
from .tools import render_css


def home(request: HttpRequest) -> HttpResponse:
    context: dict
    image_urls: list = []
    project_title: list = []
    project_description: list = []
    project_link: list = []
    user_image_urls: list = []

    projects = Project.objects.all()
    user = User.objects.filter(is_active=True).first()

    print(user.images)

    for project in projects:
        images = project.images.all()
        project_title.append(project.title)
        project_description.append(project.description)
        project_link.append(project.link)

        for image in images:
            image_urls.append(image.image.url)

    for image in user.images.all():
        user_image_urls.append(image.image.url)

    render_css(user_image_urls[0])

    context = {'projects': projects,
               'user': user,
               'image_urls': image_urls,
               'project_title': project_title,
               'project_description': project_description,
               'project_link': project_link}

    return render(request, 'index.html', context)
