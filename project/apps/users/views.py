from django.views.generic.base import TemplateView


class TestPageView(TemplateView):
    template_name = "test.html"
