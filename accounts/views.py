# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, redirect, reverse
from posts.models import Post
from posts.forms import PostForm
from comments.models import Comment
from comments.forms import CommentForm
from django.views.generic import RedirectView

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,

)
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import UserLoginForm, UserRegisterForm, ProfileForm
from . models import Profile
# Create your views here.
User = get_user_model()

def account_edit(request, slug=None):
    user = get_object_or_404(User, username=slug)
    if request.user == user:
        instance = get_object_or_404(Profile, user=request.user)
        form = ProfileForm(request.POST or None, request.FILES or None, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            # message success
            # messages.success(request, "item saved")
            return HttpResponseRedirect(instance.get_absolute_url())

        return render(request, "form.html", context={"form": form, "title": "edit"})
    else:
        raise Http404

def account_detail(request, slug=None):
    user = get_object_or_404(User, username=slug)
    query_list_posts = Post.objects.filter(to_user=user).filter(wait=False)

    paginator = Paginator(query_list_posts, 2)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger or EmptyPage:
        contacts = paginator.page(1)

    form_post = PostForm(request.POST or None)
    form_comment = CommentForm(request.POST or None)
    if request.method == 'POST' and 'btnform2' in request.POST:
        if form_comment.is_valid() and request.user.is_authenticated():
            comment_parent_id = request.POST.get("comment_parent")
            # comment_parent = get_object_or_404(Post, id=int(comment_parent_id))
            comment = form_comment.save(commit=False)
            comment.from_user = request.user
            comment.to_user = user
            comment.parent = int(comment_parent_id)
            comment.save()
            return redirect(reverse("accounts:detail", kwargs={"slug": slug}))
    elif request.method == 'POST' and 'btnform1' in request.POST:
        if form_post.is_valid() and request.user.is_authenticated():
            post = form_post.save(commit=False)
            post.from_user = request.user
            post.to_user = user
            post.save()
        return redirect(reverse("accounts:detail", kwargs={"slug": slug}))
    # comments = Comment.objects.filter(to_user=user)
    context = {
        "user": user,
        "posts": query_list_posts,
        'form_post': form_post,
        'form_comment': form_comment,
        "contacts": contacts,
    }
    return render(request, "account.html", context)


def wait_list(request, slug=None):
    user = get_object_or_404(User, username=slug)
    if (request.user.is_authenticated() and request.user == user):
        query_list = Post.objects.filter(to_user=user).filter(wait=True)
        context = {
            "user": user,
            "posts": query_list,
        }
        return render(request, "wait.html", context)
    else:
        raise Http404


def home(request):
    return render(request, "main.html", context=None)


def login_view(request):
    if (not request.user.is_authenticated()):
        # next = request.GET.get('next')
        title = "Login"
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            # if next:
            #     return redirect(next)
            return redirect("/")
        return render(request, "form.html", {"form": form, "title": title})
    else:
        redirect("/")


def register_view(request):
    if (not request.user.is_authenticated):
        # next = request.GET.get('next')
        title = "Register"
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            new_user = authenticate(username=user.username, password=password)
            login(request, new_user)
            # if next:
            #     return redirect(next)
            return redirect("/")
    else:
        return redirect("/")
    context = {
        "form": form,
        "title": title
    }
    return render(request, "form.html", context)


def logout_view(request):
    logout(request)
    return redirect("/")
