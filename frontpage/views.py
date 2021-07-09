from django.views import generic


class FrontPageGenericView(generic.TemplateView):
    index_template = 'index.html'
    information_template = 'information.html'
    wedding_list_template = 'wedding-list.html'

    def get_template_names(self):
        template_names = []
        from django.urls import reverse
        if self.request.path == reverse('frontpage:index'):
            template_names.append(self.index_template)
        if self.request.path == reverse('frontpage:information'):
            template_names.append(self.information_template)
        if self.request.path == reverse('frontpage:wedding-list'):
            template_names.append(self.wedding_list_template)
        return template_names
