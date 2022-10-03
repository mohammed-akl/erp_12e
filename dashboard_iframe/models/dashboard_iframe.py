# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.addons.board.controllers.main import Board


class Dashboard_iframe(models.Model):
    _name = 'dashboard_iframe'

    desc = fields.Char(required=True)
    url = fields.Char(required=True)
    height = fields.Integer(default=300)

    @api.model
    def create(self, vals):
        rec = super(Dashboard_iframe, self).create(vals)
        # add kanban view to users dashboard

        print('\n------------rec------>',rec)
        print('\n------------create_uid------>',rec.create_uid)
        print('\n------------_context------>',rec.create_uid._context)

        context_to_save = {
            "uid": rec.create_uid._context["uid"],
            "dashboard_merge_domains_contexts": False,
            "tz": rec.create_uid._context["tz"],
            #"params": {"action": rec.create_uid._context["params"]["action"]},
            "group_by": [],
            "lang": rec.create_uid._context["lang"]
        }

        B = Board()
        B.add_to_dashboard(context_to_save=context_to_save,
                           domain=[['id', '=', rec.id], ['id', '=', rec.id]],
                           #action_id=context_to_save["params"]["action"],
                           name=vals["desc"],
                           view_mode='kanban')
        return rec

