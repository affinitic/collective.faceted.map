# -*- coding: utf-8 -*-

from Products.Five import BrowserView
from plone import api

import json


class FacetedGeoJSON(BrowserView):
    def data_geo(self, batch):
        """Return the json data for the given batch"""
        elements = [self._generate_point(brain) for brain in batch]
        features = [e for e in elements if e]
        if not features:
            return u""
        return json.dumps({"type": "FeatureCollection", "features": features})

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
                "properties": {
                    "popup": "<a href='{0}' title='{1}'>{1}</a>".format(
                        brain.getURL(),
                        brain.Title,
                    )
                },
            }
