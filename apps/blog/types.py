from datetime import datetime

import graphene
from graphene_django.types import DjangoObjectType

from apps.blog.models import Author, Post


class AuthorType(DjangoObjectType):

    class Meta:
        model = Author
        fields = '__all__'


class PostType(DjangoObjectType):
    id = graphene.Int()
    date_posted = graphene.Int()

    class Meta:
        model = Post
        fields = '__all__'

    def resolve_date_posted(self, info, **kwargs):
        return int(datetime.today().timestamp())
