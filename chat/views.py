from django.shortcuts import render
from chat.models import Message, Chat

def index(request):
    if request.method == 'POST':
        print("Received data" + request.POST['chatMessage'])
        myChat = Chat.objects.get(id=1)
        Message.objects.create(text=request.POST['chatMessage'], chat=myChat, author=request.user, receiver=request.user)
    chatMessages = Message.objects.filter(chat__id=1)    
    return render(request, 'chat/index.html', {'name': 'lv'}, {'messages':chatMessages},)