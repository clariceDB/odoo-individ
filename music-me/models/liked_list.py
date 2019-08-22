from odoo import models, fields, api


class LikedList(models.Model):
    _name = 'music.liked_list'
    _rec_name = 'liked_albums'

    @api.depends('liked_albums')
    def _get_album_names(self):
        print('####\t_get_album_names\t####')

        # for i in self.albums:
        #     print('***********\nAlbum name:\t')
        #     print(i)
        #     self.album_name = i.name
        self.album_name = self.liked_albums.name
        print('******\nAlbumName:\t', self.album_name)

        # for i in self.liked_albums.artist.name:
            # print('*********\nArtist:\t', i)


        # test = self.liked_albums.album_artist
        # print('AFTER ASSIGNMENT')
        # for i in test:
        #     print(i)
        #
        # self.album_artist = "placeholder"


    # @api.depends('albums')
    # # def _get_album_names(self):
    # #     #     for i in self.albums:
    # #     #         print('***********\nAlbum name:\t')
    # #     #         print(i)
    # #     #         self.album_name = i.name

    # user = fields.Char('res.user')
    liked_albums = fields.Many2one('music.album', string='Liked albums')
    album_name = fields.Char(compute=_get_album_names, readonly=True)
    album_artist = fields.Char(string='Artist', compute='_get_artist')

    # (comodel_name='sis.course', inverse_name='department', string="Courses", readonly=True, copy=True)

    #     Create method to populate fields for artist, genre based on selected

    @api.multi
    def populate_fields(self):
        pass

    @api.depends('liked_albums')
    def _get_artist(self):
        print('^^^^')
        # test1 = self.liked_albums.album_artist
        # print(test1)

    class LikedListArtist(models.Model):
        _name


