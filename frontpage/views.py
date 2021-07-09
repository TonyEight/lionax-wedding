from django.views import generic


class IndexView(generic.TemplateView):
    template_name = 'index.html'


class InformationView(generic.TemplateView):
    template_name = 'information.html'


class WeddingListView(generic.TemplateView):
    template_name = 'information.html'