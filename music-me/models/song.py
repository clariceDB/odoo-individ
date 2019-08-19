from odoo import models, fields, api


class Song(models.Model):
    _name = 'music.song'

    name = fields.Char(string='Song name')
    artist = fields.Many2many('music.artist', string='Artist')
    genre = fields.Many2many('music.genre', string='Genre')
    album = fields.Many2one('music.album', string='Album')
