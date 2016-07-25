# -*- coding: utf-8 -*-

import traceback as tb
import falcon
from . import encoders
from . import exceptions


class JsonGenericHandler(object):
    serializer_class = None
    model_base = None

    def get(self, request, **kwargs):
        return ''

    def on_get(self, request, response, **kwargs):
        try:
            _response = self.get(request, **kwargs)

            if not _response:
                return

            if not self.serializer_class:
                raise exceptions.ImproperlyConfigured('You should assign serializer_class for {}'.format(type(self)))

            if not self.model_base:
                raise exceptions.ImproperlyConfigured('You should assign model_base for {}'.format(type(self)))

            final_response = encoders.sqlalchemy_json_encode(_response, self.model_base, serializer_class=self.serializer_class, serializer_context={'request': request})
            response.status = falcon.HTTP_200
            response.body = final_response
            response.set_header('Content-Type', 'application/json')
        except exceptions.APIException as exc:
            response.status = falcon.HTTP_400
            response.body = encoders.json_encode({'cause': str(exc), 'detail': tb.format_exc()})
            response.set_header('Content-Type', 'application/json')
