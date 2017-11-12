import datetime
import json
from api.localisation import constants
from api.models import MatchSeries

seeding_assets_directory = 'api/data_seed/seeding_assets'
file_name = seeding_assets_directory + '/' + 'football_match_series.json'


def seed_data():
    """
    seed isl teams data from file
    :return:
    """
    with open(file_name) as fp:
        contents_of_file = json.load(fp)

        for series in contents_of_file:
            display_name = series['display_name']
            identifier = series['identifier']
            country = series['country']
            starting_date = series['starting_date']
            ending_date = series['ending_date']

            match_series_record, created = MatchSeries.objects.get_or_create(identifier=identifier)
            match_series_record.display_name = display_name
            match_series_record.identifier = identifier
            match_series_record.country = country
            match_series_record.sport = constants.SPORTS_FOOTBALL
            match_series_record.starting_date = datetime.datetime.strptime(starting_date,
                                                                           "%Y-%m-%d").date() if starting_date else None
            match_series_record.ending_date = datetime.datetime.strptime(ending_date,
                                                                         "%Y-%m-%d").date() if ending_date else None
            match_series_record.save()

            print('updated ' + display_name + ' match series details')



            # print('\nISL team data seed  completed')
