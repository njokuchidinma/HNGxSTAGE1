from django.http import JsonResponse
from datetime import datetime,timezone


def jsonview(request):
    slack_name = request.GET.get("slack_name")
    date_time = datetime.now(timezone.utc)
    current_day_digit = date_time.weekday()
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    current_day = days[current_day_digit]
    utc_time = date_time.replace(tzinfo=timezone.utc)
    track = request.GET.get("track")
   
    return JsonResponse(
        {'slack_name': slack_name,
         'current_day': current_day,
         'utc_time': utc_time, 
         'track': track,
         'github_file_url': '',
         'github_repo_url': 'https://github.com/njokuchidinma/HNGxSTAGE1.git',
         'status_code': 200,
        }
    )
