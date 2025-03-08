from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Message
from django.db.models import Q
from django.http import JsonResponse

@login_required
def ChatRoom(request, username):
    r = User.objects.filter(username=username).first()
    messages = Message.objects.filter(
        Q(sender=request.user, receiver=r) | Q(sender=r, receiver=request.user)
    ).order_by("timestamp")

    if request.method == 'POST':
        msg = request.POST.get('msg')
        if msg:
            Message.objects.create(
                sender=request.user, 
                receiver=r, 
                message=msg
            )
        return redirect('chat', username=username)  # Redirect to refresh the page

    return render(request, 'chat/chat.html', {'r': r, 'messages': messages})

@login_required
def get_messages(request, username):
    r = User.objects.filter(username=username).first()
    if not r:
        return JsonResponse({"error": "User not found"}, status=404)

    messages = Message.objects.filter(
        Q(sender=request.user, receiver=r) | Q(sender=r, receiver=request.user)
    ).order_by("timestamp")

    messages_data = [
        {
            "sender": msg.sender.username,
            "message": msg.message,
            "timestamp": msg.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        }
        for msg in messages
    ]
    return JsonResponse({"messages": messages_data})