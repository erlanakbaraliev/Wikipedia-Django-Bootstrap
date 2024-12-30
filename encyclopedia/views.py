from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import util
import markdown
from django import forms

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
    })

def displayPage(request, name):
    page = util.get_entry(name)
    if page:
        html_content = markdown.markdown(page)
        return render(request, "encyclopedia/markdown_template.html", {
            "content": html_content,
            "title": name,
        }) 
    return render(request, "encyclopedia/error.html", {
        "message": "Error 404 : Page Not Found😭"
    })

def search(request):
    entries = util.list_entries()

    if request.method == "GET":
        query = request.GET.get("q")
        if query:
            if util.get_entry(query) is not None:
                return displayPage(request, query)

            filtered_entries = [entry for entry in entries if query.lower() in entry.lower()]
            if len(filtered_entries) > 0:
                return render(request, "encyclopedia/index.html", {
                    "entries": filtered_entries
                })
            return render(request, "encyclopedia/error.html", {
                "message": "Error 404 : Page Not Found😭"
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
    body = forms.CharField(
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

def createNewPage(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            body = form.cleaned_data["body"]
            if util.get_entry(title) is not None:
                return render(request, "encyclopedia/error.html", {
                    "message": "Page already exists 😘"
                })
            util.save_entry(title, body)
            return displayPage(request, title)
        else:
            return render(request, "encyclopedia/new")
    else:
        return render(request, "encyclopedia/newPage.html", {
            "TitleContentForm": NewEntryForm()
        })

# class EditPageForm(forms.Form):
#     pagename = forms.CharField(label="Title",disabled = False,required = False,
#     widget= forms.HiddenInput
#     (attrs={'class':'col-sm-12','style':'bottom:1rem'}))
   
#     body = forms.CharField(label="Markdown content",help_text="<p class='text-secondary'>Please refer <a class='text-info' href = https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax> GitHub’s Markdown guide</a> </p>",
#     widget= forms.Textarea
#     (attrs={"rows":20, "cols":80,'class':'col-sm-11','style':'top:2rem'}))

class EditPageForm(forms.Form):
    name = forms.CharField(label='Title', 
                            widget=forms.HiddenInput
                            (attrs={
                                'class':'col-sm-11'
                            }))
    body = forms.CharField(label='Content',
                           widget=forms.Textarea
                            (attrs={
                                'placeholder': 'Enter markdown content',
                                'class': 'col-sm-11',
                                'style': 'height: 600px; width: 100%;',                             
                            }))

def edit(request, name):
    content = util.get_entry(name)
    edit_form = NewEntryForm(initial={'name': name, 'body': content})
    if edit_form.is_valid():
        render(request, "encyclopedia/editPage.html", {
            "content": edit_form
        })
    return HttpResponse(content)
#     edit_form = forms.EditPageForm(initial={'pagename': pagename, 'body':content})

#     if edit_form.is_valid():
#         return render (request, "encyclopedia/edit_page.html",{
#                 "title": pagename,
#                 "form":NewEntryForm,
#                 "edit_form":edit_form
#             })
#     else:
#         return render (request, "encyclopedia/edit_page.html",{
#                 "title": pagename,
#                 "form":form,
#                 "edit_form":edit_form        

#         })