from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import util
import markdown
from django import forms

def index(request):
    entries = util.list_entries()

    if request.method == "GET":
        query = request.GET.get("q")
        if query:
            for entry in entries:
                if entry.lower() == query.lower():
                    return HttpResponseRedirect(reverse("displayPage", kwargs={'name': query}))

            filtered_entries = [entry for entry in entries if query.lower() in entry.lower()]
            return render(request, "encyclopedia/index.html", {
                "entries": filtered_entries
            })

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
    })

def displayPage(request, name):
    page = util.get_entry(name)
    if page:
        html_content = markdown.markdown(page)
        return render(request, "encyclopedia/markdown_template.html", {
            "content": html_content
        })
    return render(request, "encyclopedia/error.html")

def createNewPage(request):
    return render(request, "encyclopedia/newPage.html")