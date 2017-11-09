import json
from api.models import News, NewsRelationsShip


class RelationshipManager(object):

    def __init__(self, news, tags):
        self.news = news
        self.tags = [tag.lower for tag in tags]
        self.related_news = dict()
        self.news.save(relationship_update=True)

    def find_and_update_news_relationship(self):
        self.__find_related_news()
        self.__update_relationship()

    def __find_related_news(self):
        print('finding related news')
        all_news = News.objects.all()
        related_news_count = 0

        for news in all_news:

            if news.tags:
                current_news_tags = json.loads(news.tags)
                current_news_tags = [tag.lower for tag in current_news_tags]
                common_tags = list( set(self.tags) & set(current_news_tags) )

                if len(common_tags) > 0:
                    relationship = dict()
                    relationship['news_id'] = news.id
                    relationship['common_tags'] = common_tags

                    # add to dictionary
                    self.related_news[news.id] = relationship

                    # counter
                    related_news_count += 1

        print('found ' + str(related_news_count) + 'related news')

    def __update_relationship(self):
        print('\nupdating relationships')
        # remove existing
        NewsRelationsShip.objects.filter(news__id=self.news.id).delete()
        for related_news_id in self.related_news:

            tags = self.related_news[related_news_id]['common_tags']
            tags_string = json.dumps(tags)

            # create record
            relationship = NewsRelationsShip()
            relationship.news_id = self.news.id
            relationship.related_news_id = related_news_id
            relationship.relation_index = len(tags)
            relationship.common_tags = tags_string
            relationship.save()
