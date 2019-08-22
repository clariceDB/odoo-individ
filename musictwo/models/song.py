from odoo import models, fields, api


class Song(models.Model):
    _name = 'musictwo.song'

    name = fields.Char(string='Song name')
    album = fields.Many2one('musictwo.album', string='Album')
    genre = fields.Many2one('musictwo.genre', string='Genre')
    status = fields.Boolean(default = False)

    # (comodel_name='sis.course', inverse_name='department', string="Courses", readonly=True, copy=True)

    @api.multi
    def _liked_pressed(self):
        # Set status to liked
        for rec in self:
            rec.write({'status': True})
        # Add to liked songs
        self.add_to_liked()

        # recommended songs
        self.generate_rec_list()


    @api.multi
    def add_to_liked(self):
        self.env['musictwo.liked'].create({
            'name': self.name,
            'genre': self.genre,
        })

    @api.multi
    def generate_rec_list(self):
        # for song in self.env['musictwo.song'].search(['status', '=', True]):
        for rec in self.env['musictwo.liked']:
            print(rec.genre)
        pass
