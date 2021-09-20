from django.forms import ModelForm
from journal.models import Resourcelist

# Create the form class.
class ResourcelistForm(ModelForm):

    class Meta:
        model = Resourcelist
        fields = ['name', 'url', 'resource_description']

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super().form_valid(form)



