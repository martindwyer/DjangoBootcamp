from django.views.generic.base import TemplateView

class LandingPageView(TemplateView):

    template_name = "index.html"
