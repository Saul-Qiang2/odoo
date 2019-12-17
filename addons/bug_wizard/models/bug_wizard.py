# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
import logging
_logger = logging.getLogger(__name__)

# 注意这里的父类不同，向导应用的特色
class bugWizard(models.TransientModel):
    _name = 'bug.wizard'

    bug_ids = fields.Many2many('bm.bug', string='Bug')
    new_is_closed = fields.Boolean('是否关闭')
    wizard_user_id = fields.Many2one('res.users', string='负责人')

    @api.model
    def default_get(self, field_names):
        defaults = super(bugWizard, self).default_get(field_names)
        defaults['bug_ids'] = self.env.context['active_ids']
        return defaults

    @api.multi
    def update_batch(self):
        # 每次处理一个实例
        self.ensure_one()
        if not (self.new_is_closed or self.wizard_user_id):
            raise exceptions.ValidationError('无数据要更新')
        _logger.debug('批量bug更新操作 %s', self.bug_ids.ids)
        print('批量bug更新操作 %s' % self.bug_ids.ids)
        vals = {}
        if self.new_is_closed:
            vals['is_closed'] = self.new_is_closed
        if self.wizard_user_id:
            vals['user_id'] = self.wizard_user_id
        if vals:
            print(vals)
            print(self.bug_ids[0].user_id)
            self.bug_ids.write(vals)
        return True

    @api.multi
    def count_bugs(self):
        bug = self.env['bm.bug']
        count = bug.search_count([])
        raise exceptions.Warning('有 %d 条bug' % count)

    @api.multi
    def helper_form(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'res_id': self.id,
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new',
        }

    @api.multi
    def get_bugs(self):
        self.ensure_one()
        bug = self.env['bm.bug']
        all_bugs = bug.search([('is_closed', '=', False)])
        self.bug_ids = all_bugs
        return self.helper_form()
