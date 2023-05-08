def register_views():
    from blog import models
    from blog.admin.views import TagAdminView, ArticleAdminView, UserAdminView
    from blog.extensions import db, ad

    ad.add_view(ArticleAdminView(models.Article, db.session, category='Models'))
    ad.add_view(TagAdminView(models.Tag, db.session, category='Models'))
    ad.add_view(UserAdminView(models.User, db.session, category='Models'))