import json

from django.core.files import File

from api.localisation import constants
from api.models import SportsTeam

seeding_assets_directory = 'api/data_seed/seeding_assets'
file_name = seeding_assets_directory + '/' + 'isl_teams.json'


def seed_data():
    """
    seed isl teams data from file
    :return:
    """
    with open(file_name) as fp:
        contents_of_file = json.load(fp)

        for team in contents_of_file:
            team_identifier = team['team_identifier']
            display_name = team['display_name']
            logo = team['logo']

            team_record, created = SportsTeam.objects.get_or_create(team_identifier=team_identifier)
            team_record.display_name = display_name
            team_record.sport = constants.SPORTS_FOOTBALL

            team_logo_path = seeding_assets_directory + '/teams/' + logo
            logo_image = File(open(team_logo_path, 'rb'))
            team_record.logo_image = logo_image
            team_record.save()

            print('updated ' + display_name + 'team details')



            # print('\nISL team data seed  completed')
