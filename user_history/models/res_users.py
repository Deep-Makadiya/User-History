# -*- coding: utf-8 -*-
from odoo import models


class ResUsers(models.Model):
    _inherit = 'res.users'

    def write(self, vals):
        self_groups = self.read()[0]
        res = super(ResUsers, self).write(vals)
        for group1 in vals:
            if group1 in self_groups:
                if vals[group1] != self_groups[group1]:
                    updated_groups = self.env['res.groups'].browse(int(group1.split('_')[-1]))
                    if not updated_groups.category_id or updated_groups.category_id.name == "Technical" or updated_groups.category_id.name == "Extra Rights" or updated_groups.category_id.name == "Other Extra Rights":
                        old_value = ""
                        new_value = ""
                        if vals[group1] == True:
                            old_value = "False"
                            new_value = "True"
                        else:
                            old_value = "True"
                            new_value = "False"
                        group_name = updated_groups.name
                    else:
                        new_group = self.env['res.groups'].browse(vals[group1])
                        new_value = new_group.name if new_group else 'None'
                        old_group = self.env['res.groups'].browse(self_groups[group1])
                        old_value = old_group.name if old_group else 'None'
                        group_name = updated_groups.name
                    output_dict = {'user_id': self.env.user.id, 'modification_user_id': self.id,
                                   'group_id': updated_groups.id,
                                   'old_value': old_value, 'new_value': new_value, 'group_name': group_name}
                    self.env['user.history'].sudo().create(output_dict)

        return res
