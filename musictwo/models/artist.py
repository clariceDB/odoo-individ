# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Artist(models.Model):
    _name = 'musictwo.artist'

    name = fields.Char(string='Artist Name')
    # albums = fields.One2many(comodel_name='music.album', inverse_name='artist', string='Album')
    # songs = fields.One2many(comodel_name='music.song', inverse_name='artist', string='song')

    # (comodel_name='sis.course', inverse_name='department', string="Courses", readonly=True, copy=True)

