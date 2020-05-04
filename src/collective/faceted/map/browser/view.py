# -*- coding: utf-8 -*-
from plone import api
from Products.Five import BrowserView
from zope.component import queryMultiAdapter

import json


class FacetedGeoJSON(BrowserView):
    def data_geo(self, batch):
        """Return the json data for the given batch"""
        elements = [self._generate_point(brain) for brain in batch]
        features = [e for e in elements if e]
        if not features:
            return json.dumps({"type": "FeatureCollection", "features": []})
        return json.dumps({"type": "FeatureCollection", "features": features})

    def _template(self, brain):
        view = queryMultiAdapter(
            (self.context, self.request), name="faceted-map-geojson-popup", default=None
        )
        if view:
            return view.popup(brain)
        else:
            return ""

    def _generate_point(self, brain):
        catalog = api.portal.get_tool(name="portal_catalog")
        data = catalog.getIndexDataForRID(brain.getRID())
        if data.get("longitude") and data.get("latitude"):
            return {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [data["longitude"], data["latitude"]],
                },
                "id": brain.id,
                "properties": {"popup": self._template(brain), "color": "green"},
            }


class FacetedGeoJSONPopup(BrowserView):
    def popup(self, brain):
        obj = brain.getObject()
        if obj.get("image", None):
            img_url = "{0}/@@images/image/thumb".format(brain.getURL())
            template = (
                "<a href='{0}' title='{1}'><img src='{2}' alt='{1}' />"
                "<div style='width: 128px;text-align: center;"
                "margin-top: 0.5em;'>{1}</div></a>"
            )
            return template.format(brain.getURL(), brain.Title, img_url)
        else:
            return "<a href='{0}' title='{1}'>{1}</a>".format(
                brain.getURL(), brain.Title
            )
