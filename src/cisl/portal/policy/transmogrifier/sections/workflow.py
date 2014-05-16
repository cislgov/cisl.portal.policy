# -*- coding:utf-8 -*-
from collective.transmogrifier.interfaces import ISection
from collective.transmogrifier.interfaces import ISectionBlueprint
from zope.interface import classProvides
from zope.interface import implements


class WorkflowRefactorSection(object):
    classProvides(ISectionBlueprint)
    implements(ISection)

    def __init__(self, transmogrifier, name, options, previous):
        self.previous = previous

    def __iter__(self):
        for item in self.previous:
            if '_workflow_history' in item:
                self.transmogrify(item)
            yield item

    def fix_actions(self, wh):
        new_wh = []
        mapping_actions = {
            'publicar como destaque': 'publish',
            'submit': 'submit',
            'reject': 'reject',
            'submeter': 'submit',
            'publicar': 'publish',
            'rejeitar': 'reject',
            'retirar': 'retract',
            'restringir': 'publish',
            None: None,
        }
        mapping_states = {
            'destaque': 'published',
            'pendente': 'pending',
            'devolvido': 'private',
            'publicado_todos': 'published',
            'rascunho': 'pending',
            'aguardando_revisao': 'pending',
            'publicado_restrito': 'published',
        }
        for wf in wh:
            for action in wh[wf]:
                action['action'] = mapping_actions.get(
                    action['action'],
                    action['action']
                )
                action['review_state'] = mapping_states.get(
                    action['review_state'],
                    action['review_state']
                )
                new_wh.append(action)
        new_wh.sort(key=lambda x: x['time'])
        return new_wh

    def transmogrify(self, item):
        wh = item['_workflow_history']
        wh['simple_publication_workflow'] = self.fix_actions(wh)
        if 'SERPROSCWorkflow' in wh:
            del(wh['SERPROSCWorkflow'])
        if 'plone_workflow' in wh:
            del(wh['plone_workflow'])
