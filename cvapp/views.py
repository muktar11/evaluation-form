# cvapp/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from .models import Submission, BookingNotification
from .forms import SubmissionForm, BookingForm
from .utils import render_to_pdf
from django.views.decorators.http import require_http_methods
from django.conf import settings

from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Submission, BookingNotification

def home(request):
    submissions = Submission.objects.order_by('-created_at')
    notifications = BookingNotification.objects.order_by('-created_at')
    # Paginate notifications (5 per page)
    paginator = Paginator(notifications, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'cvapp/home.html', {
        'submissions': submissions,
        'notifications': page_obj,
    })


def create_submission(request):
    if request.method == 'POST':
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            submission = form.save()
            return redirect('cvapp:submission_detail', pk=submission.id)
    else:
        form = SubmissionForm()
    return render(request, 'cvapp/create_submission.html', {'form': form})



from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Submission

def submission_detail(request, pk):
    submission = get_object_or_404(Submission, pk=pk)

    # Use reverse to build an absolute URL cleanly — no concatenation
    preview_url = request.build_absolute_uri(
        reverse('cvapp:preview_submission', kwargs={'pk': submission.id})
    )

    return render(request, 'cvapp/submission_detail.html', {
        'submission': submission,
        'preview_url': preview_url,
    })




from django.utils import timezone

from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.urls import reverse
from xhtml2pdf import pisa
from io import BytesIO

from .models import Submission

def generate_pdf(request, pk):
    submission = get_object_or_404(Submission, pk=pk)
    video_url = submission.video.url if submission.video else None
    if video_url and hasattr(request, 'build_absolute_uri'):
        video_url = request.build_absolute_uri(video_url)
    context = {
        'submission': submission,
        'video_url': video_url,
        'book_url': request.build_absolute_uri(reverse('cvapp:book_submission', kwargs={'pk': submission.id})),
    }
    return render(request, 'cvapp/pdf_template.html', context)

# cvapp/views.py
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Submission

def preview_submission(request, pk):
    submission = get_object_or_404(Submission, pk=pk)

    video_url = submission.video.url if submission.video else None
    if video_url and hasattr(request, 'build_absolute_uri'):
        video_url = request.build_absolute_uri(video_url)

    book_url = reverse('cvapp:book_submission', kwargs={'pk': submission.id})

    context = {
        'submission': submission,
        'video_url': video_url,
        'book_url': book_url,  # redirect to booking page
    }
    return render(request, 'cvapp/preview_submission.html', context)


@require_http_methods(['GET', 'POST'])
def book_submission(request, pk):
    submission = get_object_or_404(Submission, pk=pk)
    if submission.booked:
        # Already booked; show message or redirect
        return render(request, 'cvapp/book_already.html', {'submission': submission})

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booker_name = form.cleaned_data['booker_name']
            booker_phone = form.cleaned_data['booker_phone']

            # record booking on submission
            submission.booked = True
            submission.booked_at = timezone.now()
            submission.booked_by_name = booker_name
            submission.booked_by_phone = booker_phone
            submission.save()

            # create notification
            BookingNotification.objects.create(
                submission=submission,
                booker_name=booker_name,
                booker_phone=booker_phone
            )

            return render(request, 'cvapp/book_success.html', {'submission': submission})
    else:
        form = BookingForm()
    return render(request, 'cvapp/book_form.html', {'form': form, 'submission': submission})




# cvapp/views.py
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from .models import Submission
from .forms import BookingForm, SubmissionForm
from .models import BookingNotification  # if exists


@require_http_methods(['GET', 'POST'])
def preview_submission(request, pk):
    submission = get_object_or_404(Submission, pk=pk)
    video_url = submission.video.url if submission.video else None
    if video_url and hasattr(request, 'build_absolute_uri'):
        video_url = request.build_absolute_uri(video_url)

    form = BookingForm(request.POST or None)

    if request.method == 'POST' and not submission.booked:
        if form.is_valid():
            submission.booked = True
            submission.booked_at = timezone.now()
            submission.booked_by_name = form.cleaned_data['booker_name']
            submission.booked_by_phone = form.cleaned_data['booker_phone']
            submission.save()

            # Create a notification record (optional)
            BookingNotification.objects.create(
                submission=submission,
                booker_name=submission.booked_by_name,
                booker_phone=submission.booked_by_phone
            )

            messages.success(request, f"✅ Successfully booked {submission.name}!")
            form = BookingForm()  # reset form
        else:
            messages.error(request, "❌ Please correct the form errors.")

    context = {
        'submission': submission,
        'video_url': video_url,
        'form': form,
    }
    return render(request, 'cvapp/preview_submission.html', context)
