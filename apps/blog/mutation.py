import graphene
from django.shortcuts import get_object_or_404

from apps.blog.models import Post
from apps.blog.types import PostType


class CreatePostMutation(graphene.Mutation):

    class Input:
        title = graphene.String(required=True)
        content = graphene.String(required=True)
        author_id = graphene.Int(required=True)

    post = graphene.Field(PostType)

    @staticmethod
    def mutate(root, info, title, content, author_id):
        post = Post(title=title, content=content, author_id=author_id)
        post.save()
        return CreatePostMutation(post=post)


class UpdatePostMutation(graphene.Mutation):
    class Input:
        id = graphene.ID(required=True)
        title = graphene.String()
        content = graphene.String()
        author_id = graphene.Int()

    post = graphene.Field(PostType)

    @staticmethod
    def mutate(root, info, id, title=None, content=None, author_id=None):
        post = get_object_or_404(Post, id=id)
        post.title = title if title else post.title
        post.content = content if content else post.content
        post.author_id = author_id if author_id else post.author_id
        post.save()
        return UpdatePostMutation(post=post)


class DeletePostMutation(graphene.Mutation):
    class Input:
        id = graphene.ID(required=True)

    post = graphene.Field(PostType)

    @staticmethod
    def mutate(root, info, id):
        post = get_object_or_404(Post, id=id)
        post.delete()
        return DeletePostMutation(post=post)


class Mutation(graphene.ObjectType):
    create_post = CreatePostMutation.Field()
    update_post = UpdatePostMutation.Field()
    delete_post = DeletePostMutation.Field()

