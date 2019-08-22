from odoo import models, fields, api


class LikedList(models.Model):
    _name = 'music.liked_list'
    _rec_name = 'liked_albums'

    @api.depends('liked_albums')
    def _get_album_names(self):
        print('####\t_get_album_names\t####')

        self.album_name = self.liked_albums.name
        print('******\nAlbumName:\t', self.album_name)

    liked_albums = fields.Many2one('music.album', string='Liked albums')
    album_name = fields.Char(compute=_get_album_names, readonly=True)
    album_artist = fields.Char(string='Artist', compute='_get_artist', default="Davy")

    @api.multi
    def _get_artist(self):
        for record in self:
            record.album_artist = self.liked_albums.album_artist
        # test1 = self.liked_albums.album_artist
        # print(test1)



