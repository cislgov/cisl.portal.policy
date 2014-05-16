# -*- coding: utf-8 -*-

from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implements

PROJECTNAME = 'cisl.portal.policy'


class HiddenProfiles(object):
    implements(INonInstallable)

    def getNonInstallableProfiles(self):
        return [
            u'cisl.portal.policy:uninstall',
            u'cisl.portal.policy:initcontent',
            u'cisl.portal.policy.upgrades.v1010:default'
        ]
