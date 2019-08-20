# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Album(models.Model):
    _name = 'music.album'

    name = fields.Char(string='Name')
    artist = fields.Many2one('music.artist', string='Artist')
    songs = fields.One2many(comodel_name='music.song', inverse_name='album', string='Song Name')
    genre = fields.Many2one('music.genre', string='Genre')
    liked_list = fields.Many2one('music.liked_list', readonly=True)

    # (comodel_name='sis.course', inverse_name='department', string="Courses", readonly=True, copy=True)
