# -*- coding: utf-8 -*-
from django.core.cache.backends.dummy import DummyCache


class FakeRedisCache(DummyCache):  # pragma: no cover
    def __init__(self, *args, **kwargs):
        DummyCache.__init__(self, *args, **kwargs)
        self.setex = None
        self.lrem = None
        self.zadd = None
        self.pipeline = None
        self.ttl = None

    @property
    def client(self):
        return self

    def close(self, **kwargs):
        pass

