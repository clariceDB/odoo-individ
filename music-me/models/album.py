# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Album(models.Model):
    _name = 'music.album'

    name = fields.Char()
    genre = fields.Many2many('music.genre')
    artist = fields.Many2one('music.artist')
    song = fields.One2many(comodel_name='music.song', inverse_name='album', string='Song Name')
    liked_list = fields.Many2many('music.liked_list')

    # (comodel_name='sis.course', inverse_name='department', string="Courses", readonly=True, copy=True)
