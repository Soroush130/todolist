from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import NoteForm
from .models import Note
from django.contrib import messages

# page note
def notes(request):
    notes = Note.objects.filter(user=request.user)
    note_add_form = NoteForm()
    context = {
        'notes':notes,
        'note_add_form':note_add_form,
    }
    return render(request,'app_note/note.html', context)

def add_note(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user=request.user
            new_form.save()
            messages.success(request, 'یادداشت شما با موفقیت اضافه شد')
        else:
            messages.error(request, 'مقادیر نامعتبر هستند')
            
    return redirect(url)

def delete_note(request, note_id):
    url = request.META.get('HTTP_REFERER')
    try:
        Note.objects.get(id=note_id).delete()
        return redirect(url)
    except:
        pass