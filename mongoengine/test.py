# -*- coding:utf-8 -*-

from mongoengine import (
    connect,
    Document,
    EmbeddedDocument,
    StringField,
    ReferenceField,
    ListField,
    EmbeddedDocumentField,
    CASCADE,
)

conn = connect('blog')


class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)

    meta = {
        'indexes': [{'fields': ('email',), 'unique': True}, ]
    }


class Comment(EmbeddedDocument):
    content = StringField()
    name = StringField(max_length=120)


class Post(Document):
    title = StringField(max_length=120, required=True)
    author = ReferenceField(User, reverse_delete_rule=CASCADE)
    tags = ListField(StringField(max_length=30))
    Comments = ListField(EmbeddedDocumentField(Comment))

    meta = {'allow_inheritance': True}


class TextPost(Post):
    content = StringField()


class ImagePost(Post):
    image_path = StringField()


class LinkPost(Post):
    link_url = StringField()


def add_user(email, first_name, last_name):
    user = User(email=email, first_name=first_name, last_name=last_name)
    user.save()
    return user


def add_textpost(title, author, content, tags=[]):
    post = TextPost(title=title, author=author, content=content, tags=tags)
    post.save()
    return post


if __name__ == '__main__':
    user = User.objects.first()
    if not user:
        user = add_user('test@gmail.com', 'first', 'last')
    add_textpost('hello', user, 'mongodb', tags=[])
    post = Post.objects.first()
    print type(post.author)
    print post.author
