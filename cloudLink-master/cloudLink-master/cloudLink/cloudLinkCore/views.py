from django.shortcuts import render, redirect
from .forms import ShortenURLForm
from .models import ShortenedURL
import hashlib
from django.utils import timezone
import secrets
# Create your views here.

def generate_short_code(long_url):
    # Generate a hash of the long URL
    hash_object = hashlib.md5(long_url.encode())
    # Use the first 10 characters as the short code
    return hash_object.hexdigest()[:10]  

def shorten_url(request):
    if request.method == 'POST':
        form = ShortenURLForm(request.POST)
        if form.is_valid():
            long_url = form.cleaned_data['long_url']

            # Check if the long_url already exists in the database
            existing_short_url = ShortenedURL.objects.filter(long_url=long_url).first()
            if existing_short_url:
                return render(request, 'cloudLinkCore/success.html', {'short_url': existing_short_url})

            short_code = generate_short_code(long_url)
            short_url = ShortenedURL.objects.create(long_url=long_url, short_code=short_code)
            return render(request, 'cloudLinkCore/success.html', {'short_url': short_url})
    else:
        form = ShortenURLForm()

    return render(request, 'cloudLinkCore/shorten.html', {'form': form})

def delete_old_records():   #for 1 week
    one_week_ago = timezone.now() - timezone.timedelta(days=7)
    old_records = ShortenedURL.objects.filter(created_at__lte=one_week_ago)
    deleted_count = old_records.count()
    old_records.delete()
    return deleted_count

def delete_records_created_before_two_days():   #for 2 days
    two_days_ago = timezone.now() - timezone.timedelta(days=2)
    old_records = ShortenedURL.objects.filter(created_at__lte=two_days_ago)
    deleted_count = old_records.count()
    old_records.delete()
    return deleted_count

from django.shortcuts import get_object_or_404

def redirect_to_long_url(request, short_code):
    short_url = get_object_or_404(ShortenedURL, short_code=short_code)
    return redirect(short_url.long_url)


#from cloudLinkCore.views import delete_records_created_before_two_days
#from cloudLinkCore.views import delete_old_records
