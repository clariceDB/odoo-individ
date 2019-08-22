# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Album(models.Model):
    _name = 'musictwo.album'

    name = fields.Char(string='Name')
    album_artist = fields.Many2one('music.artist', string='Artist')
    songs = fields.One2many(comodel_name='music.song', inverse_name='album', string='Song Name')