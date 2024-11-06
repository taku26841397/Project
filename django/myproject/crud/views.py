from django.shortcuts import render
from django.views.generic import TemplateView, ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Product
from django.urls import reverse_lazy
from django.urls import reverse

class TopView(TemplateView):
    template_name = "top.html"

class ProductListView(ListView):
    model=Product
    paginate_by=3

class ProductCreateView(CreateView):
    model=Product
    fields = '__all__'

class ProductUpdateView(UpdateView):
    model=Product
    fields='__all__'
    template_name_suffix = '_update_form'


    #新規作成・編集完了時のリダイレクト先
    def get_absolute_url(self):
        return reverse('list')

class ProductDeleteView(DeleteView):
    model=Product
    success_url=reverse_lazy('list')

class ProductDetailView(DetailView):
    model=Product
    template_name = 'crud/product_detail.html'
    context_object_name = 'product'

