from django.shortcuts import render
from django.http import JsonResponse
import google.generativeai as genai

# Configure the Gemini API
genai.configure(api_key="apikey")

# Initialize the model
model = genai.GenerativeModel('gemini-1.5-pro-latest')

def chatbot(request):
    if request.method == 'POST':
        user_input = request.POST.get('message')
        try:
            response = model.generate_content(user_input)
            return JsonResponse({'response': response.text})
        except Exception as e:
            return JsonResponse({'error': str(e)})
    return render(request, 'chatbot/chatbot.html')