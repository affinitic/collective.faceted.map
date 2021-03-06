# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.faceted.map


class CollectiveFacetedMapLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(name="testing.zcml", package=collective.faceted.map)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "collective.faceted.map:default")


COLLECTIVE_FACETED_MAP_FIXTURE = CollectiveFacetedMapLayer()


COLLECTIVE_FACETED_MAP_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_FACETED_MAP_FIXTURE,),
    name="CollectiveFacetedMapLayer:IntegrationTesting",
)


COLLECTIVE_FACETED_MAP_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_FACETED_MAP_FIXTURE,),
    name="CollectiveFacetedMapLayer:FunctionalTesting",
)


COLLECTIVE_FACETED_MAP_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_FACETED_MAP_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name="CollectiveFacetedMapLayer:AcceptanceTesting",
)
