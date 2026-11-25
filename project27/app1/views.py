from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, FormView, ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import SchoolMF
from .models import School
from django.urls import reverse_lazy
"""
class stringCbv(View):
    def get(self, request):
        ESMO = SchoolMF()
        d = {"ESMO":ESMO}

        return render(request, "createschool.html", d)

    def post(self, request):
        DSMO = SchoolMF(request.POST)
        if DSMO.is_valid():
            DSMO.save()
            return HttpResponse("Created Successfully")
        return HttpResponse("Invalid Data")


class InsertByTV(TemplateView):
    template_name = "createschool.html"

    def get_context_data(self, **kwargs):
        ECDO = super().get_context_data(**kwargs)
        ESMO = SchoolMF()
        ECDO["ESMO"] = ESMO
        return ECDO

    def post(self, request):
        DSMO = SchoolMF(request.POST)

        if DSMO.is_valid():
            DSMO.save()
            return HttpResponse("Created Successfully")
        return HttpResponse("Invalid Data")


class InsertByFV(FormView):
    template_name = "insertschool.html"
    form_class = SchoolMF
    def form_valid(self, form):
        form.save()
        return HttpResponse("Created Sccessfully..")

"""
class SchoolList(ListView):
    model = School
    # template_name = "school_list.html"
    context_object_name = "schools"


class SchoolCreate(CreateView):
    model = School
    fields = "__all__"


class SchoolDetails(DetailView):
    model = School
    context_object_name = "school"
    # template_name = "app1/schooldetails.html"


class SchoolUpdate(UpdateView):
    model = School
    fields = "__all__"


class SchoolDelete(DeleteView):
    model = School
    fields = "__all__"