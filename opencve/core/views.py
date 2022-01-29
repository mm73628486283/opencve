from django.views.generic import ListView

from core.models import CweModel


class CweView(ListView):
    queryset = CweModel.objects.order_by('-name')
    context_object_name = "cwes"
    template_name = 'core/cwes_list.html'
    paginate_by = 2
