from django.shortcuts import render, redirect
from .models import TodoList, Category
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User

@login_required
def index(request):

    current_user = request.user
    todos = TodoList.objects.filter(creator__id=current_user.id)
    categories = Category.objects.all()
    # users = User.objects.all()

    if request.method == 'POST':

        if 'taskAdd' in request.POST:
            title = request.POST['description']
            date = str(request.POST['date'])
            category = request.POST['category_select']
            content = title + "--" + date + " " + category
            Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category),\
                 creator=User.objects.get(id=int(current_user.id)))
            Todo.save()
            return redirect('TodoList')

        if 'taskEdit' in request.POST:
            todo_id = request.POST['id']
            title = request.POST['description']
            date = str(request.POST['date'])
            category = request.POST['category_select']
            content = title + "--" + date + " " + category
            
            todo = TodoList.objects.get(id=int(todo_id))
            todo.title = title
            todo.due_date = date
            todo.category = Category.objects.get(name=category)
            todo.content = content
            todo.save(update_fields=['title', 'due_date', 'category', 'content'])

            return redirect('TodoList')
        
        if 'taskDelete' in request.POST:
            TodoList.objects.filter(id__in=request.POST.getlist('checkedbox')).delete()
    
    return render(request, 'index.html', {'todos': todos, 'categories': categories})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
