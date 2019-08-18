from odoo import models, fields, api


class LikedList(models.Model):
    _name = 'music.liked_list'

    user = fields.Char('res.users')
    artist = fields.Many2many('music.artist')
    genre = fields.Many2many('music.genre')
    album = fields.Many2many('music.album')

    # (comodel_name='sis.course', inverse_name='department', string="Courses", readonly=True, copy=True)

