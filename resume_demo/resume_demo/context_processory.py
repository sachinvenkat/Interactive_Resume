from django.contrib.auth.models import user

def project_context(request):
    context = {
        'me': User.objects.first(),

    }

    return context
