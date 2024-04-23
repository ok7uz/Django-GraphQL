import graphene

from apps.blog.models import Author, Post
from apps.blog.mutation import Mutation
from apps.blog.types import PostType, AuthorType


class Query(graphene.ObjectType):
    posts = graphene.List(PostType)
    post_by_id = graphene.Field(PostType, id=graphene.Int())
    authors = graphene.List(AuthorType)

    def resolve_posts(self, info, **kwargs):
        return Post.objects.all()

    def resolve_post_by_id(self, info, id):
        return Post.objects.get(id=id)

    def resolve_authors(self, info, **kwargs):
        return Author.objects.all()


schema = graphene.Schema(query=Query, mutation=Mutation)
