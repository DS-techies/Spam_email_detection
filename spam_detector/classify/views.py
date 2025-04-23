from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EmailForm
from .spam import predict_spam

def classify_email(request):
    """
    View function to classify an email as spam or not spam.
    
    Args:
    request (HttpRequest): The current request object.
    
    Returns:
    HttpResponse: A rendered HTML template with the classification result.
    """
    
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email_text = form.cleaned_data['email_text']
            result = predict_spam(email_text)
            messages.success(request, f"Email classified as: {result}")
            return redirect('classify_email')
    else:
        form = EmailForm()
    
    return render(request, 'classify.html', {'form': form})
