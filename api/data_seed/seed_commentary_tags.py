import json

from django.core.files import File

from api.localisation import constants
from api.models import CommentaryTagImage

seeding_assets_directory = 'api/data_seed/seeding_assets'
file_name = seeding_assets_directory + '/' + 'commentary_tags.json'


def seed_data():
    """
    seed isl teams data from file
    :return:
    """
    with open(file_name) as fp:
        contents_of_file = json.load(fp)

        for commentary in contents_of_file:
            tag = commentary['tag']
            image = commentary['image']

            commentary_record, created = CommentaryTagImage.objects.get_or_create(tag=tag)

            team_logo_path = seeding_assets_directory + '/commentary_tags/' + image
            logo_image = File(open(team_logo_path, 'rb'))
            commentary_record.image = logo_image
            commentary_record.save()

            print('updated ' + tag + 'commentary_tag_image details')