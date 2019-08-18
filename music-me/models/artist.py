# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Artist(models.Model):
    _name = 'music.songs'

    name = fields.Char()
    album = fields.One2many(comodel_name='music.album', inverse_name='artist', string='Album')
    song = fields.Many2many('music.song')

    # (comodel_name='sis.course', inverse_name='department', string="Courses", readonly=True, copy=True)

