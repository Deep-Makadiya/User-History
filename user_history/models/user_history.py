# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class UserHistory(models.Model):
    _name = 'user.history'
    _description = 'USer History'
    _order = 'id desc'

    user_id = fields.Many2one('res.users', string="USer Id")
    modification_user_id = fields.Many2one('res.users', String="Modification User Id ")
    group_id = fields.Many2one('res.groups', string="Group Id")
    old_value = fields.Char(string="Old Value")
    new_value = fields.Char(string="New Value")
    group_name = fields.Char(string="Group Name")
