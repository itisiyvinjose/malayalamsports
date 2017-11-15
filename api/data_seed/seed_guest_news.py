from __future__ import unicode_literals

import datetime
import json

from cffi.backend_ctypes import unicode
from django.conf import settings
from django.core.files import File
from api.models import GuestNews


seeding_assets_directory = 'api/data_seed/seeding_assets'
file_name = seeding_assets_directory + '/' + 'guest_news.json'


def seed_data():
    """
    seed isl teams data from file
    :return:
    """
    with open(file_name, encoding='utf-8') as fp:
        contents_of_file = json.load(fp)
        for data in contents_of_file:
            news_date = data['news_date']
            content = data['content']
            source = data['source']
            title = data['title']
            # news_tags = data['news_tags']
            sport = data['sport']
            # is_trending = data['is_trending']
            # trend_scale = data['trend_scale']
            # display_order = data['display_order']
            image = data['image']
            identifier = data['identifier']

            # print(data)

            try:
                news = GuestNews.objects.get(identifier=identifier)
            except GuestNews.DoesNotExist:
                news = GuestNews()

            news.news_date = datetime.datetime.strptime(news_date, "%Y-%m-%d").date()
            news.content = content
            news.source = source
            news.title = title
            news.sport = sport
            news.identifier = identifier
            if image:
                image_path = seeding_assets_directory + '/guest_news/' + image
                # print(image_path)
                image_file =  File(open(image_path, 'rb'))
                # print(image_file)
                news.image = image_file

            news.save()
            print(news.image.url)
            print('added guest news')
