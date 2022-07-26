from django.utils.timezone import now


class LatestUserActivityMiddleWare:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.user.is_authenticated:
            # last_login and last_activity will be the same cuz user provides JWT (logging in)
            # and all of the activities are protected with IsAuthenticated
            request.user.last_login = now()
            request.user.last_activity = now()
            request.user.save()
        return response
