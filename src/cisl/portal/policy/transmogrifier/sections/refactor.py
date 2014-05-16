# -*- coding:utf-8 -*-
from collective.transmogrifier.interfaces import ISection
from collective.transmogrifier.interfaces import ISectionBlueprint
from zope.interface import classProvides
from zope.interface import implements


class RefactorSection(object):
    classProvides(ISectionBlueprint)
    implements(ISection)

    def __init__(self, transmogrifier, name, options, previous):
        self.previous = previous

    def __iter__(self):
        for item in self.previous:
            # Fix path
            item['_path'] = str(item['_path'])
            if not self.filter_contents(item['_path']):
                continue
            self.transmogrify(item)
            yield item

    def filter_contents(self, path):
        allowed = ['/noticias', ]
        for fragment in allowed:
            if fragment in path:
                return True
        return False

    def _fix_default_page(self, value):
        return str(value)

    def transmogrify(self, item):
        pt = item['_type']
        # Default page
        if pt not in ('Folder', 'Collection') and '_defaultpage' in item:
            del(item['_defaultpage'])

        for key in ['_defaultpage', '_layout']:
            if key in item:
                value = self._fix_default_page(item[key])
                if value:
                    item[key] = value
                else:
                    del(item[key])

        properties = item.get('_properties', [])
        new_properties = []
        for line in properties:
            if line[0] in ['default_page', 'layout']:
                value = self._fix_default_page(line[1])
                if value:
                    line[1] = value
                else:
                    continue
            new_properties.append(line)

        item['_properties'] = new_properties
