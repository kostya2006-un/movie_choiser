from django.shortcuts import render
from app.top500 import kino
from django.views import View


class IndexView(View):
    template_name = 'app/index.html'

    def get(self,request):
        return render(request,self.template_name)
