# -*- coding: utf-8 -*-

import simplejson as json
from sqlalchemy.orm.query import Query


def sqlalchemy_json_encode(obj, model_base, serializer_class=None):
    def default_encoder(o):
        if isinstance(o, model_base):
            return serializer_class(o).data
        elif isinstance(o, Query):
            return serializer_class(o, many=True).data
        raise TypeError()

    return json.dumps(obj, default=default_encoder)


def json_encode(obj):
    return json.dumps(obj)
