from odoo import models, fields, api


class Song(models.Model):
    _name = 'music.song'

    name = fields.Char(string='Song name')
    album = fields.Many2one('music.album', string='Album')

    # (comodel_name='sis.course', inverse_name='department', string="Courses", readonly=True, copy=True)

