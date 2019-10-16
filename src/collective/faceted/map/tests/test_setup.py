# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from Products.CMFPlone.utils import get_installer
from collective.faceted.map.testing import COLLECTIVE_FACETED_MAP_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.faceted.map is properly installed."""

    layer = COLLECTIVE_FACETED_MAP_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = get_installer(self.portal, self.layer['request'])

    def test_product_installed(self):
        """Test if collective.faceted.map is installed."""
        self.assertTrue(self.installer.is_product_installed(
            'collective.faceted.map'))

    def test_browserlayer(self):
        """Test that ICollectiveFacetedMapLayer is registered."""
        from collective.faceted.map.interfaces import (
            ICollectiveFacetedMapLayer)
        from plone.browserlayer import utils
        self.assertIn(
            ICollectiveFacetedMapLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_FACETED_MAP_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = get_installer(self.portal, self.layer['request'])
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstall_product('collective.faceted.map')
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if collective.faceted.map is cleanly uninstalled."""
        self.assertFalse(self.installer.is_product_installed(
            'collective.faceted.map'))

    def test_browserlayer_removed(self):
        """Test that ICollectiveFacetedMapLayer is removed."""
        from collective.faceted.map.interfaces import \
            ICollectiveFacetedMapLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            ICollectiveFacetedMapLayer,
            utils.registered_layers())
