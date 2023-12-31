from django.shortcuts import HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,ListView,UpdateView,DetailView,TemplateView,DeleteView
from VideoSystem.models import *
from VideoSystem.forms import CommentForm,SearchForm
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
from django.shortcuts import render

class Upload_Video(LoginRequiredMixin,CreateView):
    model = VideoUpload
    template_name = 'VideoSystem/videoupload.html'
    fields = ('Video_title','Upload_Thumbnail','Video_description','Upload_video')

    def form_valid(self,form):
        videoobj = form.save(commit=False)
        videoobj.Upload_user = self.request.user
        title = videoobj.Video_title
        videoobj.slug = title.replace(" ","-")+"-"+str(uuid.uuid4())
        videoobj.save()
        return HttpResponseRedirect(reverse('home'))

class Video_list(LoginRequiredMixin,ListView):
    context_object_name = 'videos'
    model = VideoUpload
    template_name = 'VideoSystem/video_list.html'

@login_required
def VideoView(request,slug):
    video = VideoUpload.objects.get(slug=slug)
    # comment = VideoComment.objects.get(TheVideo = video)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.TheUser = request.user
            comment.TheVideo = video
            comment.save()
            HttpResponseRedirect(reverse('VideoSystem_APP:VideoView',kwargs={'slug' : slug}))
    return render(request,'VideoSystem/VideoView.html',context={'video':video,'commentform' : form})

@login_required
def Video_search(request):
    query = request.GET.get('q')
    videos = VideoUpload.objects.all()

    if query:
        videos = videos.filter(Video_title__icontains=query)

    return render(request, 'VideoSystem/search.html', {'videos': videos, 'query': query})
