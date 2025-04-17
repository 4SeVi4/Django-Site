from blog.models import Category, Post

# Створення категорій
category1 = Category.objects.create(name="Технології", description="Все про новітні технології")
category2 = Category.objects.create(name="Подорожі", description="Поради для мандрівників")

# Створення публікацій
post1 = Post.objects.create(
    title="Що нового в світі технологій?",
    content="Останні новини та відкриття в світі технологій.",
    image=None  # Без зображення
)
post1.categories.add(category1)

post2 = Post.objects.create(
    title="Подорож до Японії",
    content="Мій досвід подорожі в Японію, культурні особливості та цікаві місця.",
    image=None
)
post2.categories.add(category2)
