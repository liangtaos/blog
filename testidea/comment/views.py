from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import TemplateView
from .forms import CommentForm


class CommentView(TemplateView):
    # http_method_names = ['POST']
    template_name = 'comment/result.html'


    def get(self, request, *args, **kwargs):
        return super(CommentView, self).get(request, *args, **kwargs)


    def post(self, request,*args, **kwargs):
        target = request.POST.get('target')
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            ins = comment_form.save(commit=False)
            ins.target = target
            # print(ins.content)
            ins.save()
            succeed = True
        else:
            succeed = False
        context = {
            'succeed': succeed,
            'form': comment_form,
            'target': target,
        }
        return self.render_to_response(context)
