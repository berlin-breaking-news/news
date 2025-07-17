import os

def create_article(title, category, author, image, content, tags):
    """
    Create an article HTML file with the given content
    """
    # Create a simple article template
    template = f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Independent Clone</title>
    <meta name="description" content="{content[:150]}...">
    <link rel="stylesheet" href="../../css/style.css">
    <link rel="stylesheet" href="../../css/article.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
</head>
<body>
    <!-- Header -->
    <header class="header">
        <div class="header-top">
            <div class="container">
                <div class="header-top-content">
                    <div class="date-time">
                        <span id="current-date"></span>
                    </div>
                    <div class="social-links">
                        <a href="#"><i class="fab fa-facebook"></i></a>
                        <a href="#"><i class="fab fa-twitter"></i></a>
                        <a href="#"><i class="fab fa-instagram"></i></a>
                        <a href="#"><i class="fab fa-youtube"></i></a>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="header-main">
            <div class="container">
                <div class="header-main-content">
                    <a href="../../index.html" class="logo">
                        <h1>Independent</h1>
                        <span>Clone</span>
                    </a>
                    
                    <nav class="main-nav">
                        <ul>
                            <li><a href="../../index.html">Главная</a></li>
                            <li><a href="../politika.html">Политика</a></li>
                            <li><a href="../mir.html">Мир</a></li>
                            <li><a href="../sport.html">Спорт</a></li>
                            <li><a href="../kultura.html">Культура</a></li>
                            <li><a href="../tehnologii.html">Технологии</a></li>
                        </ul>
                    </nav>
                    
                    <div class="header-actions">
                        <button class="search-btn"><i class="fas fa-search"></i></button>
                        <button class="subscribe-btn">Подписаться</button>
                    </div>
                </div>
            </div>
        </div>
    </header>

    <main class="main-content">
        <article class="article-container">
            <header class="article-header">
                <span class="article-category">{category}</span>
                <h1 class="article-title">{title}</h1>
                <div class="article-meta">
                    <span class="article-author">{author}</span>
                    <span class="article-date full-updated-date">0</span>
                    <span class="article-reading-time">5 мин чтения</span>
                </div>
            </header>
            
            <div class="article-image">
                <img src="../../{image}" alt="{title}">
                <p class="image-caption">Фото: Independent Clone</p>
            </div>
            
            <div class="article-content">
                <p class="lead">{content}</p>
                <p>Это полный текст новости. Здесь будет содержаться детальная информация по теме. {content}</p>
                <p>Дополнительные детали и анализ ситуации. {content}</p>
            </div>
            
            <div class="article-tags">
                {"
                ".join(['<a href="#" class="tag">' + tag + '</a>' for tag in tags])}
            </div>
            
            <div class="article-share">
                <span>Поделиться:</span>
                <a href="#" class="social-share" data-platform="facebook"><i class="fab fa-facebook"></i></a>
                <a href="#" class="social-share" data-platform="twitter"><i class="fab fa-twitter"></i></a>
                <a href="#" class="social-share" data-platform="telegram"><i class="fab fa-telegram"></i></a>
            </div>
        </article>
    </main>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-logo">
                    <h2>Independent</h2>
                    <span>Clone</span>
                </div>
                
                <div class="footer-links">
                    <div class="footer-section">
                        <h3>Разделы</h3>
                        <ul>
                            <li><a href="../../index.html">Главная</a></li>
                            <li><a href="../politika.html">Политика</a></li>
                            <li><a href="../mir.html">Мир</a></li>
                            <li><a href="../sport.html">Спорт</a></li>
                            <li><a href="../kultura.html">Культура</a></li>
                            <li><a href="../tehnologii.html">Технологии</a></li>
                        </ul>
                    </div>
                </div>
            </div>
            
            <div class="footer-bottom">
                <p>&copy; 2025 Independent Clone. Все права защищены.</p>
            </div>
        </div>
    </footer>

    <script src="../../js/script.js"></script>
    <script>
        // Update current date
        const options = { year: 'numeric', month: 'long', day: 'numeric', weekday: 'long' };
        document.getElementById('current-date').textContent = new Date().toLocaleDateString('ru-RU', options);
    </script>
</body>
</html>
"""
    return template

def create_slug(title):
    # Convert to lowercase and replace spaces with hyphens
    slug = title.lower()
    # Remove special characters
    slug = ''.join(c if c.isalnum() or c == ' ' else ' ' for c in slug)
    # Replace spaces with hyphens and remove double hyphens
    slug = '-'.join(slug.split())
    return slug

def main():
    # Create articles directory if it doesn't exist
    articles_dir = 'pages/articles'
    os.makedirs(articles_dir, exist_ok=True)
    
    # List of articles to create
    articles = [
        {
            'title': 'Премьер-министр объявил о крупных реформах в системе здравоохранения',
            'category': 'Политика',
            'author': 'Анна Петрова',
            'image': 'images/stock/Starmer PMQs.avif',
            'content': 'Правительство объявило о масштабной реформе системы здравоохранения, направленной на улучшение качества медицинских услуг и сокращение времени ожидания пациентов.',
            'tags': ['здравоохранение', 'реформы', 'политика']
        },
        {
            'title': 'Инфляция достигла нового максимума за последние 5 лет',
            'category': 'Экономика',
            'author': 'Михаил Смирнов',
            'image': 'images/stock/iStock 1765329424.avif',
            'content': 'По данным Центрального банка, годовая инфляция в стране ускорилась до 9.8%, что стало максимальным показателем за последние пять лет.',
            'tags': ['инфляция', 'экономика', 'финансы']
        },
        {
            'title': 'Новый прорыв в области искусственного интеллекта',
            'category': 'Технологии',
            'author': 'Алексей Иванов',
            'image': 'images/stock/News Image.avif',
            'content': 'Ученые представили революционную модель искусственного интеллекта, способную обучаться новым задачам в разы быстрее существующих аналогов.',
            'tags': ['ии', 'технологии', 'инновации']
        },
        {
            'title': 'Сборная страны готовится к чемпионату мира',
            'category': 'Спорт',
            'author': 'Дмитрий Козлов',
            'image': 'images/stock/Reading Festival 2024 by Luke Dyson.avif',
            'content': 'Национальная сборная по футболу начала интенсивную подготовку к предстоящему чемпионату мира.',
            'tags': ['футбол', 'чемпионат мира', 'спорт']
        }
    ]
    
    # Create article pages
    for article in articles:
        slug = create_slug(article['title'])
        filename = f"{articles_dir}/{slug}.html"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(create_article(**article))
        
        print(f"Created: {filename}")
    
    print("\nAll articles have been created successfully!")

if __name__ == "__main__":
    main()
