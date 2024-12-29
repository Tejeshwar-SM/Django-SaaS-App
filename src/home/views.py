import pathlib
from django.shortcuts import render
from django.http import HttpResponse

from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent # gives the path to the parent directoryf

def home_page_view(request, *args, **kwargs):

    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)

    html_ = ""
    my_title = "My Page"
    my_context = {
        "page_title": my_title,
        "page_visit_count": page_qs.count(),
        "total_visit_count": qs.count()
    }
    html_template = "home.html"

    # path = request.path
    # print(path)

    PageVisit.objects.create(path = request.path)
    return render(request, html_template, my_context)

def my_old_home_page_view(request, *args, **kwargs):
    # print(this_dir)

    my_title = "The Page"
    my_context = {
        "page_title": my_title
    }

    html_ = """
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>{page_title} this anything</h1>
</body>
</html>

""".format(**my_context)
#these are multiline strings
    # html_file_path = this_dir/"home.html"
    # html_ = html_file_path.read_text()

    return HttpResponse(html_)