from django.views.generic import DetailView, CreateView, UpdateView, TemplateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .models import Pet
from .mixins import PageTitleMixin, PetOwnerRequiredMixin
from .forms import PetForm

class PetDetailView(PageTitleMixin, DetailView):
    model = Pet
    template_name = 'pets/pet_detail.html'
    page_title = 'Карточка питомца'

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_authenticated:
            qs = qs.filter(is_public=True)
        return qs
    
class PetCreateView(LoginRequiredMixin, PageTitleMixin, CreateView):
    model = Pet
    form_class = PetForm
    template_name = 'pets/pet_form.html'
    page_title = 'Добавить питомца'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
class PetUpdateView(LoginRequiredMixin, PetOwnerRequiredMixin, PageTitleMixin, UpdateView):
    model = Pet
    form_class = PetForm
    template_name = 'pets/pet_form.html'
    context_object_name = Pet
    page_title = 'Редактировать питомца'

class PetDeleteView(LoginRequiredMixin, PetOwnerRequiredMixin, PageTitleMixin, DeleteView):
    model = Pet
    template_name = 'pets/pet_confirm_delete.html'
    context_object_name = Pet
    page_title = 'Удалить карточку питомца'
    success_url = reverse_lazy('pets:pet_list')

class PetListOwnerView(LoginRequiredMixin, PageTitleMixin, TemplateView):
    template_name = 'pets/pet_list.html'
    page_title = 'Мои питомцы'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pets'] = Pet.objects.filter(owner=self.request.user)
        return context

@method_decorator(cache_page(600), name='dispatch')
class VetClinicDirectoryView(PageTitleMixin, TemplateView):
    template_name = 'pets/vet_clinic.html'
    page_title = 'Справочник ветеринарных клиник'

