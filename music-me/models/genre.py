from odoo import models, fields, api


class Genre(models.Model):
    _name = 'music.genre'
    _rec_name = 'name'

    # user = fields.Char('res.user')
    name = fields.Char(string='Genre')

    # (comodel_name='sis.course', inverse_name='department', string="Courses", readonly=True, copy=True)

