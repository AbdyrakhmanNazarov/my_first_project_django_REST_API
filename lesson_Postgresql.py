# Posgresql

# 1. PostgreSQL — это:

# Реляционная база данных (RDBMS)
# То есть данные хранятся в таблицах, которые связаны между собой.

# PostgreSQL =

# open-source
# надёжная
# очень мощная
# используется в production проектах (Netflix, Instagram, Reddit)



# 2. PostgreSQL vs SQLite
# | SQLite               | PostgreSQL                          |
# | -------------------- | ----------------------------------- |
# | Файл на диске        | Сервер                              |
# | Для обучения         | Для production                      |
# | 1 пользователь       | Много пользователей                 |
# | Нет ролей            | Роли и права                        |
# | Минимум возможностей | Триггеры, индексы, JSON, транзакции |



# 3. Основные понятия PostgreSQL

# Database — база данных
# Table — таблица
# Row — строка (запись)
# Column — колонка
# Primary Key — уникальный ID
# Foreign Key — связь между таблицами
# Index — ускорение поиска



# 4. Как Django работает с PostgreSQL

# Python code → ORM → SQL → PostgreSQL


# 6. Создание пользователя и базы

# linux/macos: sudo -u postgres psql 
# windwos: psql -U postgres

# CREATE DATABASE nurzaman;
# CREATE USER hadzhi WITH PASSWORD '2003hoji';
# ALTER ROLE hadzhi SET client_encoding TO 'utf8';
# ALTER ROLE hadzhi SET default_transaction_isolation TO 'read committed';
# ALTER ROLE hadzhi SET timezone TO 'UTC';
# GRANT ALL PRIVILEGES ON DATABASE nurzaman TO hadzhi;

# News.objects.all() -> SELECT * FROM news



# 7. Установка драйвера для Django

# pip install psycopg2-binary



# 8. Подключение PostgreSQL в Django

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'nurzaman',
#         'USER': 'hadzhi',
#         'PASSWORD': '2003hoji',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

# ENGINE — тип БД
# HOST — где БД запущена
# PORT — стандартный порт PostgreSQL


# 1. Создать базу данных
# CREATE DATABASE shop_db;

# 2. Удалить базу данных
# DROP DATABASE shop_db;

# 3. Создать таблицу
# CREATE TABLE users (
#     id SERIAL PRIMARY KEY,
#     email VARCHAR(255) UNIQUE NOT NULL,
#     age INT,
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );

# 4. Удалить таблицу
# DROP TABLE users;

# 5. Добавить данные в таблицу
# INSERT INTO accounts_user (email, password, first_name)
# VALUES ('test@mail.com', '2003', 'Hoji');
# ORM
# Users.object.create("email":"test@mail.com", "password":"2003", "first_name":"Hoji")

# 6. Добавить несколько записей
# INSERT INTO users (email, age)
# VALUES 
# ('a@mail.com', 20),
# ('b@mail.com', 30);

# 7. Выбрать все данные
# SELECT * FROM users;
# get_users = Users.object.all()
# print(get_user)

# 8. Выбрать конкретные колонки
# SELECT email, age, FROM users;
# Users.objects.values_list('email', 'age')

# 9. Фильтрация с WHERE
# SELECT * FROM users WHERE age > 18;
# Users.object.filter(age__gte=18)

# 10. Несколько условий (AND)
# SELECT * FROM users WHERE age > 18 AND age < 30;
# Users.object.filter(age__range=[18 ,30])

# 11. Логическое ИЛИ (OR)
# SELECT * FROM users WHERE age = 20 OR age = 30;
# Users.objects.filter(age__in=[20, 30])

# 12. Сортировка данных
# SELECT * FROM users ORDER BY age DESC;             # DESC < # ASC >
# User.objects.filter(age__lte=18)

# 13. Ограничение количества строк
# SELECT * FROM users LIMIT 5;
# No

# 14. Пропуск строк (пагинация)
# SELECT * FROM users LIMIT 5 OFFSET 5;
# No

# 15. Обновление данных
# UPDATE users SET age = 26 WHERE email = 'test@mail.com';
# Users.objects.filter(email='test@mail.com').update(age=26)

# 16. Удаление записи
# DELETE FROM users WHERE email = 'test@mail.com';
# Users.objects.filter(email='test@mail.com').delete()

# 17. Подсчёт количества строк
# SELECT COUNT(*) FROM users;
# Users.object.count()
# count = len(users)

# 18. Уникальные значения
# SELECT DISTINCT age FROM users;
# User.objects.distinct(age)       

# 19. Диапазон значений
# SELECT * FROM users WHERE age BETWEEN 20 AND 30;
# Users.object.filter(age__range=[20 ,30]) Диапазон

# 20. Поиск по шаблону
# SELECT * FROM users WHERE email LIKE '@gmail.com';
# Users.objects.filter(email__endswith='@gmail.com')

# 21. Проверка на список значений
# SELECT * FROM users WHERE age IN (20, 25, 30);
# Users.objects.filter(age__in=[20, 25, 30]) Точные возрасты

# 22. Проверка на NULL
# SELECT * FROM users WHERE age IS NULL; 
# Users.objects.filter(age__isnull=True)

# 23. Создание таблицы с внешним ключом
# CREATE TABLE orders (
#     id SERIAL PRIMARY KEY,
#     user_id INT REFERENCES users(id),
#     total_price DECIMAL(10,2)
# );
# No

# 24. JOIN (объединение таблиц)
# SELECT users.email, orders.total_price
# FROM users
# JOIN orders ON users.id = orders.user_id;
# No

# 25. GROUP BY + COUNT
# SELECT age, COUNT(*)
# FROM users
# GROUP BY age;
# No



# -- PSQL SHELL / pgAdmin — БАЗА
# -- =========================================
# psql -U postgres
# \l
# \c project_db
# \dt
# \d users
# \du
# \q

# -- =========================================
# -- DATABASE
# -- =========================================
# CREATE DATABASE project_db;
# DROP DATABASE project_db;

# -- =========================================
# -- TABLE
# -- =========================================
# CREATE TABLE users (
#     id SERIAL PRIMARY KEY,
#     username VARCHAR(100) NOT NULL,
#     email VARCHAR(100) UNIQUE NOT NULL,
#     age INT,
#     created_at TIMESTAMP DEFAULT NOW()
# );

# DROP TABLE users;
# TRUNCATE TABLE users;

# -- =========================================
# -- CRUD
# -- =========================================
# INSERT INTO users (username, email, age)
# VALUES ('admin', 'admin@mail.com', 25);

# SELECT * FROM users;
# SELECT id, email FROM users;
# SELECT * FROM users WHERE age > 18;
# SELECT * FROM users WHERE email LIKE '%gmail%';

# UPDATE users
# SET age = 30
# WHERE id = 1;

# DELETE FROM users WHERE id = 1;

# -- =========================================
# -- SORT / LIMIT
# -- =========================================
# SELECT * FROM users ORDER BY id DESC;
# SELECT * FROM users LIMIT 5;
# SELECT * FROM users OFFSET 5 LIMIT 5;

# -- =========================================
# -- AGGREGATES
# -- =========================================
# SELECT COUNT(*) FROM users;
# SELECT AVG(age) FROM users;
# SELECT MIN(age) FROM users;
# SELECT MAX(age) FROM users;

# -- =========================================
# -- RELATIONS
# -- =========================================
# CREATE TABLE orders (
#     id SERIAL PRIMARY KEY,
#     user_id INT REFERENCES users(id),
#     total INT
# );

# SELECT * FROM orders;

# -- =========================================
# -- JOIN
# -- =========================================
# SELECT users.username, orders.total
# FROM users
# JOIN orders ON users.id = orders.user_id;

# -- =========================================
# -- INDEX
# -- =========================================
# CREATE INDEX idx_users_email ON users(email);
# DROP INDEX idx_users_email;



# ORM codes
# =========================
# 1️⃣ CRUD — создание, чтение, обновление, удаление
# =========================

# Django
# User.objects.create(name="Ali", age=25)       # CREATE
# user = User(name="Asel", age=22)
# user.save()

# User.objects.all()                             # SELECT *
# User.objects.get(id=1)                         # SELECT 1 запись
# User.objects.filter(age=18)                     # SELECT с фильтром
# User.objects.exclude(age=18)                    # SELECT с исключением
# User.objects.order_by('age')                    # сортировка ASC
# User.objects.order_by('-age')                   # сортировка DESC
# User.objects.distinct()                         # уникальные записи
# User.objects.values('name')                     # только поле name
# User.objects.values_list('name', flat=True)    # список значений
# User.objects.filter(email__isnull=True)        # NULL
# User.objects.filter(email__isnull=False)       # NOT NULL

# user = User.objects.get(id=1)
# user.age = 30
# user.save()                                    # UPDATE
# User.objects.filter(age=18).update(age=19)

# user = User.objects.get(id=1)
# user.delete()                                  # DELETE
# User.objects.filter(age__lt=18).delete()

# User.objects.count()                           # COUNT всех
# User.objects.filter(age__gte=18).count()       # COUNT с фильтром

# # SQLAlchemy (async пример)
# from sqlalchemy import select, func, distinct, and_, or_, not_
# from sqlalchemy.orm import relationship

# # SELECT все
# stmt = select(User)
# result = await session.execute(stmt)
# users = result.scalars().all()

# # SELECT с условием
# stmt = select(User).where(User.age>=18)
# stmt = select(User).where(User.name.ilike('%ali%'))

# # DISTINCT
# stmt = select(distinct(User.age))
# result = await session.execute(stmt)
# ages = [row[0] for row in result.all()]

# # COUNT / SUM / AVG / MAX / MIN
# stmt = select(func.count(User.id))
# stmt = select(func.avg(User.age))
# stmt = select(func.max(User.age))
# stmt = select(func.sum(User.age))
# result = await session.execute(stmt)
# count = result.scalar()

# # CREATE
# user = User(name="Ali", age=25)
# session.add(user)
# await session.commit()

# # UPDATE
# user = await session.get(User, 1)
# user.age = 30
# await session.commit()

# # DELETE
# user = await session.get(User, 1)
# await session.delete(user)
# await session.commit()

# # ORDER BY
# stmt = select(User).order_by(User.age.asc())
# stmt = select(User).order_by(User.age.desc())

# # NULL
# stmt = select(User).where(User.email.is_(None))
# stmt = select(User).where(User.email.is_not(None))

# # IN / BETWEEN
# stmt = select(User).where(User.age.in_([18,20,25]))
# stmt = select(User).where(User.age.between(18,30))

# # LIKE / ILIKE
# stmt = select(User).where(User.name.ilike('%ali%'))

# # Сложные условия (AND / OR / NOT)
# stmt = select(User).where(and_(User.age>=18, User.name.ilike('%ali%')))
# stmt = select(User).where(or_(User.age<18, User.name.ilike('%bob%')))
# stmt = select(User).where(not_(User.age==18))

# # =========================
# # 2️⃣ JOIN / связи
# # =========================
# # Django
# Post.objects.filter(user__name='Ali')       # JOIN через ForeignKey
# User.objects.prefetch_related('posts')      # ManyToMany / OneToMany

# # SQLAlchemy
# stmt = select(Post).join(Post.user).where(User.name=='Ali')
# result = await session.execute(stmt)
# posts = result.scalars().all()

# # =========================
# # 3️⃣ Агрегация
# # =========================
# # Django
# from django.db.models import Count, Sum, Avg, Max, Min

# User.objects.aggregate(Avg('age'))
# User.objects.aggregate(Max('age'))
# User.objects.annotate(posts_count=Count('post'))

# # SQLAlchemy
# stmt = select(func.count(User.id))
# stmt = select(func.avg(User.age))
# stmt = select(func.max(User.age))
# stmt = select(func.sum(User.age))
# result = await session.execute(stmt)
# value = result.scalar()

# # =========================
# # 4️⃣ Q-условия / сложные фильтры
# # =========================
# # Django
# from django.db.models import Q

# User.objects.filter(Q(age__gte=18) & Q(name__icontains='ali'))  # AND
# User.objects.filter(Q(age__lt=18) | Q(name__icontains='bob'))   # OR

# # SQLAlchemy
# stmt = select(User).where(and_(User.age>=18, User.name.ilike('%ali%')))
# stmt = select(User).where(or_(User.age<18, User.name.ilike('%bob%')))
