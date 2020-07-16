# -*- coding: utf-8 -*-
from Products.Five import BrowserView


class MapView(BrowserView):

    @property
    def current_index(self):
        if not hasattr(self, "_current_index"):
            self._current_index = -1
        return self._current_index

    @current_index.setter
    def current_index(self, value):
        self._current_index = value

    def get_index(self, brain):
        if self.is_geolocated(brain):
            self.current_index += 1
            return self.current_index

    def is_geolocated(self, brain):
        return isinstance(brain.latitude, float) and isinstance(brain.longitude, float)

    def css_class(self, brain):
        base = "faceted-map-text faceted-map-item {0}"
        if self.is_geolocated(brain):
            return base.format("geolocated")
        return base.format("not-geolocated")
