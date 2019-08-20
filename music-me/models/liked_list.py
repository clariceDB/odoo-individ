from odoo import models, fields, api


class LikedList(models.Model):
    _name = 'music.liked_list'
    _rec_name = 'liked_albums'

    @api.depends('liked_albums')
    def _get_album_names(self):
        print('####\t_get_album_names\t####')
        for rec in self.liked_albums:
            print(rec)
        # for i in self.albums:
        #     print('***********\nAlbum name:\t')
        #     print(i)
        #     self.album_name = i.name
        self.album_name = self.liked_albums.name
        print('******\nAlbumName:\t', self.album_name)

    # @api.depends('albums')
    # # def _get_album_names(self):
    # #     #     for i in self.albums:
    # #     #         print('***********\nAlbum name:\t')
    # #     #         print(i)
    # #     #         self.album_name = i.name

    # user = fields.Char('res.user')
    liked_albums = fields.Many2one(comodel_name='music.album', inverse_name='liked_list', string='Liked albums')
    album_name = fields.Char(compute=_get_album_names, readonly=True)

    # (comodel_name='sis.course', inverse_name='department', string="Courses", readonly=True, copy=True)

    #     Create method to populate fields for artist, genre based on selected

    @api.multi
    def populate_fields(self):
        pass


