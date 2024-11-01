from nanodjango import Django
from django.template.response import TemplateResponse

app = Django(
    EXTRA_APPS=["django_cotton"]
)

@app.route("/")
def index(request):
    return TemplateResponse(request, "index.html")
