# -*- coding: utf-8 -*-
from collective.faceted.map import _
from eea.facetednavigation.config import ANNO_FACETED_LAYOUT
from plone import api
from plone.app.layout.viewlets.common import ViewletBase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.annotation.interfaces import IAnnotations
from zope.i18n import translate

import json


class MapViewlet(ViewletBase):
    index = ViewPageTemplateFile("mapviewlet.pt")

    def available(self):
        if not getattr(self.context, "layout", "") == "facetednavigation_view":
            return False
        view_name = IAnnotations(self.context).get(
            ANNO_FACETED_LAYOUT, "faceted-preview-items"
        )
        if not view_name == "faceted-map":
            return False
        return True

    @property
    def map_configuration(self):
        map_layers = api.portal.get_registry_record("geolocation.map_layers") or []
        config = {
            "fullscreencontrol": api.portal.get_registry_record(
                "geolocation.fullscreen_control", default=True
            ),
            "locatecontrol": api.portal.get_registry_record(
                "geolocation.locate_control", default=True
            ),
            "zoomcontrol": api.portal.get_registry_record(
                "geolocation.zoom_control", default=True
            ),
            "minimap": api.portal.get_registry_record(
                "geolocation.show_minimap", default=True
            ),
            "addmarker": api.portal.get_registry_record(
                "geolocation.show_add_marker", default=False
            ),
            "geosearch": api.portal.get_registry_record(
                "geolocation.show_geosearch", default=False
            ),
            "geosearch_provider": api.portal.get_registry_record(
                "geolocation.geosearch_provider", default=[]
            ),
            "default_map_layer": api.portal.get_registry_record(
                "geolocation.default_map_layer", default=[]
            ),
            "map_layers": [
                {"title": translate(_(l), context=self.request), "id": l}
                for l in map_layers
            ],
            "useCluster": False,
        }
        return json.dumps(config)
