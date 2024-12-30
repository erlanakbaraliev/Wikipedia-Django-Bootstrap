from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from . import util
import markdown
from django import forms

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
    })

def entry(request, title):
    html_content = markdown_to_html(title)
    if html_content is not None:
        
        return render(request, "encyclopedia/entry.html", {  # Return HttpResponse
            "title": title,
            "content": html_content
        })
    else:
        return render(request, "encyclopedia/error.html", {  # Return HttpResponse
            "message": "The requested entry was not found."
        })


def markdown_to_html(title):
    content = util.get_entry(title)
    markdowner = markdown.Markdown()
    if content == None:
        return None
    else:
        html_content = markdowner.convert(content)
        return html_content
    
def search(request):
    if request.method == "GET":
        title = request.GET['q']
        html_content = markdown_to_html(title)
        if html_content:
            return render(request, "encyclopedia/entry.html", {
                "title": title,
                "content": html_content
            })
        else:
            found_entries = []
            entries = util.list_entries()
            for entry in entries:
                if title.lower() in entry.lower():
                    found_entries.append(entry)
            if len(found_entries) > 0:
                return render(request, "encyclopedia/index.html", {
                    "entries": found_entries
                })
            return render(request, "encyclopedia/error.html", {  # Return HttpResponse
                "message": "The requested entry was not found."
            })

def newPage(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            if util.get_entry(title) is not None:
                return render(request, "encyclopedia/error.html", {
                    "message": "Page already exists 😘"
                })
            util.save_entry(title, content)
            return entry(request, title)
    else:
        return render(request, "encyclopedia/newPage.html", {
            "content": NewEntryForm()
        })

class NewEntryForm(forms.Form):
    title = forms.CharField(
        label="Title", max_length=50, 
        widget=forms.TextInput(
            attrs={
                'style': 'width: 300px',
            }
        )
    )
    content = forms.CharField(
        label="Markdown content",
        required=True,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Enter markdown content',
                'class': 'col-sm-11',
                'style': 'height: 600px; width: 100%;', 
            }
        )
    )

def edit(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = util.get_entry(title)
        form = NewEntryForm(initial={
            "title": title,
            "content": content
        })

        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": form
        })
    
def save_edit(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        util.save_entry(title, content)
        return entry(request, title)