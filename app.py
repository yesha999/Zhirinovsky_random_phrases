from flask import Flask, render_template, request

from utils import get_posts_all

app = Flask('Johnny Catswill')


@app.route("/")
def page_index():
    all_posts = get_posts_all()
    return render_template("index.html", posts=all_posts)


@app.route("/posts/<int:postid>")
def page_post(postid):
    all_posts = get_posts_all()
    for post in all_posts:
        if int(post['pk']) == postid:
            return render_template("post.html", post=post)
    return "Ошибка, пост не найден"


@app.route("/search/")
def search_page():
    s = request.args.get("s")
    all_posts = get_posts_all()
    ten_posts = all_posts[:10]
    if s is None:
        return render_template("search.html", posts=ten_posts, posts_count=len(all_posts))
    s = s.lower()
    founded_posts = [post for post in all_posts if s in post['content'].lower()]
    if len(founded_posts):
        ten_posts = founded_posts[:10]
        return render_template("search.html", posts=ten_posts, posts_count=len(founded_posts))
    return render_template("search_none.html")


@app.route("/users/<username>")
def user_feed_page(username):
    all_posts = get_posts_all()
    users_posts = []
    for post in all_posts:
        if post['poster_name'] == username:
            users_posts.append(post)
    if len(users_posts):
        return render_template("user-feed.html", posts=users_posts)
    return render_template("no_user.html")


if __name__ == "__main__":
    app.run()
