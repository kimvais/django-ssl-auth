from pprint import pformat
from django.http import HttpResponse
from django.views.generic import View


class Main(View):
    def get(self, request, **kwargs):
        ctx = dict(
            user_dn=request.META['HTTP_X_SSL_USER_DN'],
            authentication_status=request.META['HTTP_X_SSL_AUTHENTICATED'],
            user=str(request.user))
        return HttpResponse(pformat(ctx), mimetype="text/plain")

