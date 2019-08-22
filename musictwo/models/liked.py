from odoo import models, fields, api


class LikedList(models.Model):
    _name = 'musictwo.liked'

    name = fields.Char(string="Name", readonly=True)
    genre = fields.Many2one('musictwo.genre', string="Name", readonly=True)