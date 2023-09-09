from django.http import JsonResponse
from datetime import datetime,timezone


def api(request):
    slack_name = request.GET.get("slack_name")
    date = datetime.now(timezone.utc)
    date_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    current_day_digit = date.weekday()
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    current_day = days[current_day_digit]
    # utc_time = date_time.replace(tzinfo=timezone.utc)
    utc_time = date_time

    track = request.GET.get("track")
   
    return JsonResponse(
        {'slack_name': slack_name,
         'current_day': current_day,
         'utc_time': utc_time, 
         'track': track,
         'github_file_url': 'https://github.com/njokuchidinma/HNGxSTAGE1/tree/main/Getrequest',
         'github_repo_url': 'https://github.com/njokuchidinma/HNGxSTAGE1',
         'status_code': 200,
        }
    )

    datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")