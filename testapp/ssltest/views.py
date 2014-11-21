from pprint import pformat
from django.http import HttpResponse
from django.views.generic import View
from django_ssl_auth.fineid import user_dict_from_dn


class Fineid(View):
    def get(self, request, **kwargs):
        ctx = dict(
            user_data=user_dict_from_dn(request.META[
                'HTTP_X_SSL_USER_DN']),
            authentication_status=request.META['HTTP_X_SSL_AUTHENTICATED'],
            user=str(request.user))
        return HttpResponse(pformat(ctx), content_type="text/plain")

class Test(View):
    def get(self, request, **kwargs):
        ctx = dict(
            user_dn=request.META[
                'HTTP_X_SSL_USER_DN'],
            authentication_status=request.META['HTTP_X_SSL_AUTHENTICATED'],
            user=str(request.user))
        return HttpResponse(pformat(ctx), content_type="text/plain")
