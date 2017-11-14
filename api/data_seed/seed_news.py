from __future__ import unicode_literals

import datetime
import json

from cffi.backend_ctypes import unicode
from django.conf import settings
from django.core.files import File

from api.models import News

# def seed_data():
#     image_path = settings.BASE_DIR + '/api/data_seed/seeding_assets/index.png'
#     print(image_path)
#     logo_image = File(open(image_path, 'rb'))
#     news = News.objects.all().order_by('created_at')[0]
#     news.image = logo_image
#     news.save()
#     print(news.image.url)


seeding_assets_directory = 'api/data_seed/seeding_assets'
file_name = seeding_assets_directory + '/' + 'news.json'


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
            news_tags = data['news_tags']
            sport = data['sport']
            is_trending = data['is_trending']
            trend_scale = data['trend_scale']
            display_order = data['display_order']
            image = data['image']
            identifier = data['identifier']

            try:
                news = News.objects.get(identifier=identifier)
            except News.DoesNotExist:
                news = News()

            news.news_date = datetime.datetime.strptime(news_date, "%Y-%m-%d").date()
            news.content = content
            news.source = source
            news.title = title
            news.news_tags = news_tags
            news.sport = sport
            news.is_trending = is_trending
            news.trend_scale = trend_scale
            news.display_order = display_order
            news.identifier = identifier

            news.save()
            print('added news')
