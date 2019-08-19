from odoo import models, fields, api


class Genre(models.Model):
    _name = 'music.genre'

    # user = fields.Char('res.user')
    name = fields.Char(string='Genre')
    album = fields.Many2many('music.album')
    song = fields.Many2many('music.song')

    # (comodel_name='sis.course', inverse_name='department', string="Courses", readonly=True, copy=True)

