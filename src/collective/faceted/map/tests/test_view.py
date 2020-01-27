# -*- coding: utf-8 -*-
from collective.faceted.map.testing import COLLECTIVE_FACETED_MAP_INTEGRATION_TESTING
from collective.faceted.map.utils import add_behavior
from eea.facetednavigation.interfaces import IFacetedNavigable
from plone import api
from plone.app.testing import applyProfile
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.formwidget.geolocation.geolocation import Geolocation
from zope.interface import directlyProvides

import unittest


class TestView(unittest.TestCase):

    layer = COLLECTIVE_FACETED_MAP_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        self.request = self.layer["request"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])

    def test_map_view(self):
        coll = api.content.create(
            type="Collection", container=self.portal, id="collection"
        )
        view = coll.restrictedTraverse("faceted-map")
        directlyProvides(coll, IFacetedNavigable)
        self.assertIn("faceted-map", view())

    def test_geojson_map_view(self):
        coll = api.content.create(
            type="Collection", container=self.portal, id="collection"
        )
        view = coll.restrictedTraverse("faceted-map-geojson")
        directlyProvides(coll, IFacetedNavigable)
        self.assertEqual(view.data_geo(coll.queryCatalog()), "")
        applyProfile(self.portal, "collective.geolocationbehavior:default")
        add_behavior(
            "Document", "collective.geolocationbehavior.geolocation.IGeolocatable"
        )
        doc = api.content.create(type="Document", container=self.portal, id="doc")
        doc.geolocation = Geolocation(latitude="50.498863", longitude="4.719407")
        doc.reindexObject()
        feature = view.data_geo(api.content.find(portal_type="Document"))
        self.assertEqual(
            feature,
            '{"type": "FeatureCollection", "features": [{"type": "Feature", "geometry": {"type": "Point", "coordinates": [4.719407, 50.498863]}, "id": "doc", "properties": {"popup": "<a href=\'http://nohost/plone/doc\' title=\'\'></a>", "color": "green"}}]}',
        )
