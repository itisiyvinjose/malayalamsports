import json
from api.models import News, NewsRelationsShip


# class RelationshipManager(object):
#
#     def __init__(self, news):
#         self.news = news
#         self.tags = [tag.tag_name.lower() for tag in self.news.related_tags.all()]
#         self.related_news = dict()
#
#     def find_and_update_news_relationship(self):
#         self.__find_related_news()
#         self.__update_relationship()
#
#     def __find_related_news(self):
#         print('finding related news')
#         all_news = News.objects.exclude(id=self.news.id).all()
#         related_news_count = 0
#
#         for news in all_news:
#
#             if len(news.related_tags.all()) > 0:
#                 current_news_tags = [tag.tag_name.lower() for tag in news.related_tags.all()]
#                 current_news_tags = [tag for tag in current_news_tags]
#                 common_tags = list( set(self.tags) & set(current_news_tags) )
#
#                 if len(common_tags) > 0:
#                     relationship = dict()
#                     relationship['news_id'] = news.id
#                     relationship['common_tags'] = common_tags
#
#                     # add to dictionary
#                     self.related_news[news.id] = relationship
#
#                     # counter
#                     related_news_count += 1
#
#         print('found ' + str(related_news_count) + ' related news')
#
#     def __update_relationship(self):
#         print('\nupdating relationships')
#         # remove existing
#         NewsRelationsShip.objects.filter(news__id=self.news.id).delete()
#         for related_news_id in self.related_news:
#
#             tags = self.related_news[related_news_id]['common_tags']
#             tags_string = json.dumps(tags)
#
#             # create record
#             relationship = NewsRelationsShip()
#             relationship.news_id = self.news.id
#             relationship.related_news_id = related_news_id
#             relationship.relation_index = len(tags)
#             relationship.common_tags = tags_string
#             relationship.save()
#
#             # reverse relationship
#             reverse_relationship = NewsRelationsShip()
#             reverse_relationship.news_id = related_news_id
#             reverse_relationship.related_news_id = self.news.id
#             reverse_relationship.relation_index = len(tags)
#             reverse_relationship.common_tags = tags_string
#             reverse_relationship.save()


class RelationshipManager(object):

    def __init__(self, news):
        self.news = news
        self.tags = self.get_tags(news.news_tags)
        self.related_news = dict()

    @staticmethod
    def get_tags(news_tags):

        tags = news_tags.split(" ")
        tags = [str(tag).strip() for tag in tags]
        tags = [tag.lower() for tag in tags if tag]
        return tags

    def find_and_update_news_relationship(self):
        self.__find_related_news()
        self.__update_relationship()

    def __find_related_news(self):

        print('finding related news')
        all_news = News.objects.exclude(id=self.news.id).all()
        related_news_count = 0

        for news in all_news:

            if news.news_tags:
                current_news_tags = self.get_tags(news.news_tags)
                common_tags = list( set(self.tags) & set(current_news_tags) )

                if len(common_tags) > 0:
                    relationship = dict()
                    relationship['news_id'] = news.id
                    relationship['common_tags'] = common_tags

                    # add to dictionary
                    self.related_news[news.id] = relationship

                    # counter
                    related_news_count += 1

        print('found ' + str(related_news_count) + ' related news')

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

            # reverse relationship
            if not NewsRelationsShip.objects.filter(news_id=related_news_id, related_news_id=self.news.id).exists():
                reverse_relationship = NewsRelationsShip()
                reverse_relationship.news_id = related_news_id
                reverse_relationship.related_news_id = self.news.id
                reverse_relationship.relation_index = len(tags)
                reverse_relationship.common_tags = tags_string
                reverse_relationship.save()

        print('\n updated relationship')

