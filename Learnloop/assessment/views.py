from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt # Use only for API endpoints
import json

from .models import CodeChallenge, CodeSubmission
from .tasks import process_submission

# Helper to create a dummy challenge if none exists
def create_dummy_challenge():
    """Ensures at least one challenge exists for the demo."""
    challenge, created = CodeChallenge.objects.get_or_create(
        title="Python Data Structure Optimization",
        defaults={
            'description': (
                "Write a Python function `process_list(data)` that efficiently "
                "filters out all negative numbers from the input list `data` "
                "and returns the result. Focus on using Pythonic, efficient structures."
            )
        }
    )
    return challenge

def assessment_view(request, challenge_id=None):
    """Renders the main assessment page with the challenge details."""
    if not CodeChallenge.objects.exists():
        create_dummy_challenge()
    
    # Use the first challenge if no ID is provided, or fetch the specific one
    if challenge_id is None:
        challenge = CodeChallenge.objects.first()
    else:
        challenge = get_object_or_404(CodeChallenge, pk=challenge_id)
        
    context = {'challenge': challenge}
    return render(request, 'assessment.html', context)


@require_http_methods(["POST"])
@csrf_exempt # WARNING: CSRF exempt is used for simplicity. Use CSRF tokens in production.
def submit_code(request):
    """Handles the AJAX submission, saves the code, and starts the processing task."""
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Authentication required.'}, status=401)
    
    try:
        data = json.loads(request.body)
        challenge_id = data.get('challenge_id')
        code_snippet = data.get('code_snippet')
        
        challenge = get_object_or_404(CodeChallenge, pk=challenge_id)
        
        # 1. Create the submission entry
        submission = CodeSubmission.objects.create(
            user=request.user,
            challenge=challenge,
            code_snippet=code_snippet,
            execution_status='PENDING'
        )
        
        # 2. Start the asynchronous processing task
        # NOTE: In production, this would be: process_submission.delay(submission.id)
        # We use a synchronous call here to simplify the demo environment.
        process_submission(submission.id) 
        
        return JsonResponse({
            'status': 'Processing started',
            'submission_id': submission.id
        })
        
    except CodeChallenge.DoesNotExist:
        return JsonResponse({'error': 'Challenge not found.'}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON format.'}, status=400)
    except Exception as e:
        return JsonResponse({'error': f'Submission failed: {e}'}, status=500)


@require_http_methods(["GET"])
def get_submission_status(request, submission_id):
    """API endpoint to retrieve the status and results of a submission."""
    try:
        submission = get_object_or_404(CodeSubmission, pk=submission_id)
        
        response_data = {
            'status': submission.execution_status,
            'score': submission.seniority_score,
            'feedback': submission.feedback,
            'features': submission.ml_features,
            'title': submission.challenge.title
        }
        return JsonResponse(response_data)
        
    except CodeSubmission.DoesNotExist:
        return JsonResponse({'error': 'Submission not found.'}, status=404)
