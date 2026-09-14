from django.contrib.auth.mixins import AccessMixin
from django.core.exceptions import PermissionDenied

class PageTitleMixin:
    '''для автоматической передачи title в контекст'''
    page_title = 'PetCard'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title']=self.page_title
        return context
    
class PetOwnerRequiredMixin(AccessMixin):
    '''проверка прав на редактирование'''
    def dispatch(self, request, *args, **kwargs):
        # получаем объект к которому идут обращение
        self.object = self.get_object()
        if self.object.owner != request.user:
            raise PermissionDenied('Вы не являетесь владельцем этого питомца')
        return super().dispatch(request, *args, **kwargs)
    
