# -*- coding: utf-8 -*-

from cisl.portal.policy.config import PROJECTNAME
from plone.app.upgrade.utils import loadMigrationProfile

import logging


def apply_profile(context):
    """Atualiza perfil para versao 1010."""
    logger = logging.getLogger(PROJECTNAME)
    profile = 'profile-cisl.portal.policy.upgrades.v1010:default'
    loadMigrationProfile(context, profile)
    logger.info('Atualizado para versao 1010')
