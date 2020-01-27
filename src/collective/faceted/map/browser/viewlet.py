# -*- coding: utf-8 -*-
from eea.facetednavigation.config import ANNO_FACETED_LAYOUT
from plone.app.layout.viewlets.common import ViewletBase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.annotation.interfaces import IAnnotations


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
