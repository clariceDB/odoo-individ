# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Genre(models.Model):
    _name = 'musictwo.genre'

    name = fields.Char(string='Name')

