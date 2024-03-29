from django.shortcuts import render
from .models import Message
from .models import Chat

def index(request):
    if request.method == 'POST':
        print("Received data" + request.POST['chatMessage'])
        myChat = Chat.objects.get(id=1)
        Message.objects.create(text=request.POST['chatMessage'], chat=myChat, author=request.user, receiver=request.user)
    chatMessages = Message.objects.filter(chat__id=1)    
    return render(request, 'chat/index.html', {'messages': chatMessages})

def login_view(request):
    return render(request, 'auth/login.html',)
