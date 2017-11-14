import datetime
import json
from api.localisation import constants
from api.models import MatchSeries, FootBallMatchDetails, SportsTeam

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
            sport = series['sport']

            try:
                match_series = MatchSeries.objects.get(identifier=identifier)
            except MatchSeries.DoesNotExist:
                match_series = MatchSeries()

            match_series.starting_date = datetime.datetime.strptime(starting_date, "%Y-%m-%d").date()
            match_series.display_name = display_name
            match_series.identifier = identifier
            match_series.country = country
            match_series.sport = sport
            match_series.save()

            for match in series['matches']:

                # print(match)
                match_starting_date = match['match_starting_date']
                match_starting_time = match['match_starting_time']
                match_status = match['match_status']
                match_status_text = match['match_status_text']
                venue = match['venue']
                sport = match['sport']
                should_show_on_home_page = match['should_show_on_home_page']
                team_one_identifier = match['team_one_identifier']
                team_two_identifier = match['team_two_identifier']
                identifier = match['identifier']

                team_one = SportsTeam.objects.get(team_identifier=team_one_identifier)
                team_two = SportsTeam.objects.get(team_identifier=team_two_identifier)

                try:
                    football_match = FootBallMatchDetails.objects.get(identifier=identifier)
                except FootBallMatchDetails.DoesNotExist:
                    football_match = FootBallMatchDetails()

                football_match.match_starting_date = datetime.datetime.strptime(match_starting_date, "%Y-%m-%d").date()
                football_match.team_one = team_one
                football_match.team_two = team_two
                football_match.match_status = match_status
                football_match.match_status_text = match_status_text
                football_match.venue = venue
                football_match.sport = sport
                football_match.match_series = match_series
                football_match.should_show_on_home_page = should_show_on_home_page
                football_match.save()




            print('updated ' + display_name + 'match series details')



            # print('\nISL team data seed  completed')
