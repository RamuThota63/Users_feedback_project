from django.shortcuts import render, redirect, get_object_or_404
from .models import Feedback
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


BAD_WORDS = ["stupid", "idiot", "dumb", "moron", "useless", "nonsense", "lame",
    "worthless", "terrible", "garbage", "trash", "pathetic",  "hate", "disgusting", "annoying", "horrible", "worst", "sucks", 
    "awful", "crap", "painful", "bastard", "screw", "damn", "piss", "bad","waste of money"]

@login_required
def feedback_view(request):
    if request.method == 'POST':
        rating = int(request.POST['rating'])
        text = request.POST['text']
        emoji = request.POST['emoji']

        found_bad_words = [word for word in BAD_WORDS if word in text.lower()]
        has_bad = len(found_bad_words) > 0

        fb = Feedback.objects.create(
            user=request.user,
            rating=rating,
            comment=text,
            emoji=emoji,
            contains_bad_words=has_bad,
            bad_words_used=", ".join(found_bad_words) if has_bad else ""
        )

        return redirect('thank_you', feedback_id=fb.id)
    return render(request, 'feedbackapp/feedback.html')

@login_required
def thank_you(request, feedback_id):
    feedback = Feedback.objects.get(id=feedback_id)
    return render(request, 'feedbackapp/thank_you.html', {'feedback': feedback})

def admin_dashboard(request):
    feedbacks = Feedback.objects.all()
    harsh_words = ['bad', 'worst', 'stupid', 'nonsense']  # Add your own list

    for fb in feedbacks:
        comment_words = fb.comment.split()
        highlighted = []
        for word in comment_words:
            if word.lower().strip('.,!?') in harsh_words:
                highlighted.append(f'<span style="color:red;font-weight:bold;">{word}</span>')
            else:
                highlighted.append(word)
        fb.highlighted_comment = format_html(' '.join(highlighted))

    return render(request, 'feedbackapp/admin_dashboard.html', {'feedbacks': feedbacks})

@login_required
def admin_dashboard(request):
    if not request.user.is_admin:
        return redirect('landing')

    feedbacks = Feedback.objects.all().order_by('-created_at')
    return render(request, 'feedbackapp/admin_dashboard.html', {'feedbacks': feedbacks})


@login_required
def delete_feedback(request, feedback_id):
    feedback = get_object_or_404(Feedback, id=feedback_id)
    feedback.delete()
    return redirect('admin_dashboard')

def admin_logout(request):
    logout(request)
    return redirect('admin_login')