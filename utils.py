import json


def _take_posts_from_data():
    """Получаем список постов из файла жсон"""
    with open('data/data.json', encoding='utf-8') as f:
        posts = json.load(f)
        if posts:
            return posts
        return []


def _take_comments_from_comments():
    """Получаем из файла жсон все коммантарии"""
    with open('data/comments.json', encoding='utf-8') as f:
        comments = json.load(f)
        if comments:
            return comments
        return []


def get_posts_all():
    """Возвращает список всех постов сразу с комментариями и их количеством"""
    posts = _take_posts_from_data()
    comments = _take_comments_from_comments()
    posts_w_comments = []

    for post in posts:
        post["comments_count"] = 0
        post["comments"] = []
        post['short_content'] = f'{post["content"][:50]}...'
        for comment in comments:
            if comment["post_id"] == post["pk"]:
                post["comments"].append(comment)
                post["comments_count"] += 1
        posts_w_comments.append(post)
    return posts_w_comments

