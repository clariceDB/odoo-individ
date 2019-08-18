from odoo import models, fields, api


class Song(models.Model):
    _name = 'music.song'

    name = fields.Char(name='Song name')
    artist = fields.Many2many('music.artist')
    genre = fields.Many2many('music.genre')
    album = fields.Many2one('music.album')
