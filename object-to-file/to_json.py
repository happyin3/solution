import datetime
import json
import pickle
from collections import defaultdict


class Post(object):
    def __init__(self, date, title, rst_text, tags):
        self.date = date
        self.title = title
        self.rst_text = rst_text
        self.tags = tags

    def as_dict(self):
        return dict(
            date=str(self.date),
            title=self.title,
            underline='-'*len(self.title),
            rst_text=self.rst_text,
            tag_text=' '.join(self.tags),
        )


class Blog(object):
    def __init__(self, title, posts=None):
        self.title = title,
        self.entries = posts if posts is not None else []

    def append(self, post):
        self.entries.append(post)

    def by_tag(self):
        tag_index = defaultdict(list)
        for post in self.entries:
            for tag in post.tags:
                tag_index[tag].append(post.as_dict())
        return tag_index

    def as_dict(self):
        return dict(
            title=self.title,
            underline='='*len(self.title),
            entries=[p.as_dict() for p in self.entries]
        )


def blog_encode(obj):
    if isinstance(obj, datetime.datetime):
        return dict(
            __class__='datetime.datetime',
            __args__=[],
            __kw__=dict(
                year=obj.year,
                month=obj.month,
                day=obj.day,
                hour=obj.hour,
                minute=obj.minute,
                second=obj.second,
            )
        )

    elif isinstance(obj, Post):
        return dict(
            __class__='Post',
            __args__=[],
            __kw__=dict(
                date=obj.date,
                title=obj.title,
                rst_text=obj.rst_text,
                tags=obj.tags,
            )
        )

    elif isinstance(obj, Blog):
        return dict(
            __class__='Blog',
            __args__=[
                obj.title,
                obj.entries
            ],
            __kw__={},
        )


if __name__ == '__main__':
    travel = Blog('Travel')

    post = Post(
        date=datetime.datetime(2018, 6, 9, 9, 54, 11),
        title='test',
        rst_text='test test',
        tags=('111', '222', '333'),
    )
    travel.append(post)

    post = Post(
        date=datetime.datetime(2018, 6, 8, 9, 54, 11),
        title='test test',
        rst_text='test test test',
        tags=('111', '222', '333', '444'),
    )
    travel.append(post)

    print(json.dumps(travel.as_dict(), indent=4))
    print(json.dumps(travel, indent=4, default=blog_encode))

    with open('travel_blog.p', 'wb') as target:
        pickle.dump(travel, target)

    copy_travel = None
    with open('travel_blog.p', 'rb') as source:
        copy_travel = pickle.load(source)

    print(type(copy_travel))
