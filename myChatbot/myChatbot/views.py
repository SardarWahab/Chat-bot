from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages

def home(request):
    return render(request, 'index.html')

from .chatbot import get_ai_answer
def chatbot(request):
    if request. method == 'POST':
        question = request.POST.get("message")
        answer = get_ai_answer(question)
        messages.info(request,answer)

      
    
    return redirect('home')