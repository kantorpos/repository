import logging
from django.shortcuts import redirect, render, reverse
from django.views import generic
from .forms import RepoModelForm, RepoModelUpdateForm
from .models import Repo
from django.contrib.auth.mixins import LoginRequiredMixin

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

class RepoUploadView(LoginRequiredMixin,generic.CreateView):
    template_name = "main/upload.html"
    form_class = RepoModelForm
    
    def get_success_url(self):
        logger.info("Redirect To List")
        return reverse("main:repo-list")
    
    def form_valid(self, form):
        logger.info("The Form is valid")
        logger.info("Upload Successfuly")
        return super(RepoUploadView, self).form_valid(form)
    
class RepoListView(generic.ListView):
    template_name = "main/list.html"
    queryset = Repo.objects.all()
    context_object_name = "repos"
    
class AdminListView(LoginRequiredMixin,generic.ListView):
    template_name = "main/admin_list.html"
    queryset = Repo.objects.all()
    context_object_name = "repos"
    
class RepoUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "main/update.html"
    form_class = RepoModelUpdateForm
    queryset = Repo.objects.all()

    def get_success_url(self):
        return reverse("main:repo-admin")
    
def repo_update_status(request, pk):
    repo = Repo.objects.get(id=pk)
    form = RepoModelForm(instance=repo)
    if request.method == "POST":
        print('Receiving a post request')
        form = RepoModelForm(request.POST, instance=repo)
        if form.is_valid():
            logger.info("The Form is valid")
            form.save()
            logger.info("The Repo has ben update")
            return redirect("/admin")
    context = {
        "form": form,
        "repo": repo
    }
    return render(request, "main/repo_update.html", context)
    