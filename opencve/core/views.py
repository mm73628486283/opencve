from django.views.generic import ListView, TemplateView

from core.models import CweModel


class HomeView(TemplateView):
    template_name = "core/home.html"


class CweView(ListView):
    queryset = CweModel.objects.order_by("-name")
    context_object_name = "cwes"
    template_name = "core/cwes_list.html"
    paginate_by = 20
