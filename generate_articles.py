import os
import shutil

# Create article template
def create_article_template(title, category, author, image, content, tags):
    return f"""<!DOCTYPE html>
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
                <p>Это полный текст новости. Здесь будет содержаться детальная информация по теме. {content} {content}</p>
                <p>Дополнительные детали и анализ ситуации. {content}</p>
                
                <blockquote>
                    <p>"Важная цитата или высказывание по теме статьи."</p>
                    <cite>— Эксперт в данной области</cite>
                </blockquote>
                
                <p>Заключительная часть статьи с выводами и перспективами. {content}</p>
            </div>
            
            <div class="article-tags">
                {''.join([f'<a href="#" class="tag">{tag}</a>' for tag in tags])}
            </div>
            
            <div class="article-share">
                <span>Поделиться:</span>
                <a href="#" class="social-share" data-platform="facebook"><i class="fab fa-facebook"></i></a>
                <a href="#" class="social-share" data-platform="twitter"><i class="fab fa-twitter"></i></a>
                <a href="#" class="social-share" data-platform="telegram"><i class="fab fa-telegram"></i></a>
                <a href="#" class="social-share" data-platform="whatsapp"><i class="fab fa-whatsapp"></i></a>
            </div>
            
            <div class="article-author-bio">
                <div class="author-avatar">
                    <img src="../../images/authors/0.jpg" alt="{author}">
                </div>
                <div class="author-info">
                    <h4>{author}</h4>
                    <p>Опытный журналист с многолетним стажем работы в ведущих изданиях страны.</p>
                </div>
            </div>
        </article>
        
        <section class="related-articles">
            <h2>Читайте также</h2>
            <div class="related-grid">
                <article class="related-article">
                    <a href="#" class="related-image">
                        <img src="../../images/stock/News from The Independent.avif" alt="Похожая новость 1">
                    </a>
                    <div class="related-content">
                        <span class="related-category">{category}</span>
                        <h3><a href="#">Похожая новость по теме</a></h3>
                        <span class="related-date">Вчера</span>
                    </div>
                </article>
                
                <article class="related-article">
                    <a href="#" class="related-image">
                        <img src="../../images/stock/Independent News Headlines.avif" alt="Похожая новость 2">
                    </a>
                    <div class="related-content">
                        <span class="related-category">{category}</span>
                        <h3><a href="#">Дополнительные материалы</a></h3>
                        <span class="related-date">2 дня назад</span>
                    </div>
                </article>
            </div>
        </section>
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
                    
                    <div class="footer-section">
                        <h3>Компания</h3>
                        <ul>
                            <li><a href="../o-nas.html">О нас</a></li>
                            <li><a href="../kontakty.html">Контакты</a></li>
                            <li><a href="../reklama.html">Реклама</a></li>
                            <li><a href="../vakansii.html">Вакансии</a></li>
                            <li><a href="../pomoshch.html">Помощь</a></li>
                        </ul>
                    </div>
                    
                    <div class="footer-section">
                        <h3>Подписаться</h3>
                        <p>Будьте в курсе последних новостей</p>
                        <form class="footer-subscribe">
                            <input type="email" placeholder="Ваш email" required>
                            <button type="submit">OK</button>
                        </form>
                        <div class="footer-social">
                            <a href="#"><i class="fab fa-facebook"></i></a>
                            <a href="#"><i class="fab fa-twitter"></i></a>
                            <a href="#"><i class="fab fa-instagram"></i></a>
                            <a href="#"><i class="fab fa-youtube"></i></a>
                            <a href="#"><i class="fab fa-telegram"></i></a>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="footer-bottom">
                <p>&copy; {2025} Independent Clone. Все права защищены.</p>
                <div class="footer-legal">
                    <a href="../politika-konfidentsialnosti.html">Политика конфиденциальности</a>
                    <a href="../usloviya-ispolzovaniya.html">Условия использования</a>
                    <a href="../cookies.html">Файлы cookie</a>
                </div>
            </div>
        </div>
    </footer>

    <!-- Policy Popups -->
    <div id="privacy-policy-popup" class="policy-popup">
        <div class="policy-container">
            <button class="close-policy">&times;</button>
            <h3>Политика конфиденциальности</h3>
            <div class="policy-content">
                <p>Ваша конфиденциальность важна для нас. Мы обязуемся защищать ваши личные данные и соблюдать применимое законодательство о защите персональных данных.</p>
                <p>Настоящая Политика конфиденциальности объясняет, как мы собираем, используем, раскрываем и защищаем вашу информацию при использовании нашего веб-сайта.</p>
            </div>
        </div>
    </div>

    <div id="terms-policy-popup" class="policy-popup">
        <div class="policy-container">
            <button class="close-policy">&times;</button>
            <h3>Условия использования</h3>
            <div class="policy-content">
                <p>Используя этот веб-сайт, вы соглашаетесь с нашими Условиями использования. Пожалуйста, внимательно ознакомьтесь с ними перед использованием сайта.</p>
                <p>Мы оставляем за собой право вносить изменения в настоящие Условия в любое время. Продолжение использования вами сайта после внесения изменений означает ваше согласие с такими изменениями.</p>
            </div>
        </div>
    </div>

    <div id="cookies-policy-popup" class="policy-popup">
        <div class="policy-container">
            <button class="close-policy">&times;</button>
            <h3>Использование файлов cookie</h3>
            <div class="policy-content">
                <p>Мы используем файлы cookie для улучшения вашего опыта на нашем сайте. Продолжая использовать наш сайт, вы соглашаетесь на использование файлов cookie в соответствии с нашей Политикой использования файлов cookie.</p>
                <div class="cookie-buttons">
                    <button id="accept-cookies" class="btn btn-primary">Принять все</button>
                    <button id="reject-cookies" class="btn btn-secondary">Отклонить</button>
                    <a href="#" class="cookie-settings">Настройки</a>
                </div>
            </div>
        </div>
    </div>

    <script src="../../js/script.js"></script>
    <script>
        // Update current date
        const options = { year: 'numeric', month: 'long', day: 'numeric', weekday: 'long' };
        document.getElementById('current-date').textContent = new Date().toLocaleDateString('ru-RU', options);
        
        // Social share functionality
        document.querySelectorAll('.social-share').forEach(function(button) {
            button.addEventListener('click', function(e) {
                e.preventDefault();
                const platform = this.getAttribute('data-platform');
                const url = encodeURIComponent(window.location.href);
                const title = encodeURIComponent(document.title);
                let shareUrl = '';
                
                switch(platform) {
                    case 'facebook':
                        shareUrl = `https://www.facebook.com/sharer/sharer.php?u=${url}`;
                        break;
                    case 'twitter':
                        shareUrl = `https://twitter.com/intent/tweet?url=${url}&text=${title}`;
                        break;
                    case 'telegram':
                        shareUrl = `https://t.me/share/url?url=${url}&text=${title}`;
                        break;
                    case 'whatsapp':
                        shareUrl = `https://wa.me/?text=${title}%20${url}`;
                        break;
                }
                
                window.open(shareUrl, '_blank', 'width=600,height=400');
            });
        });
        
        // Initialize policy popups
        document.addEventListener('DOMContentLoaded', function() {
            // This will be handled by the main script.js
        });
    </script>
</body>
</html>
"""

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
            'content': 'Правительство объявило о масштабной реформе системы здравоохранения, направленной на улучшение качества медицинских услуг и сокращение времени ожидания пациентов. В рамках реформы планируется модернизировать оборудование в больницах, увеличить финансирование первичного звена здравоохранения и внедрить цифровые технологии для ускорения процесса диагностики и лечения.',
            'tags': ['здравоохранение', 'реформы', 'политика']
        },
        {
            'title': 'Инфляция достигла нового максимума за последние 5 лет',
            'category': 'Экономика',
            'author': 'Михаил Смирнов',
            'image': 'images/stock/iStock 1765329424.avif',
            'content': 'По данным Центрального банка, годовая инфляция в стране ускорилась до 9.8%, что стало максимальным показателем за последние пять лет. Основной вклад в ускорение инфляции внесли рост цен на продовольственные товары, топливо и жилищно-коммунальные услуги. Эксперты прогнозируют дальнейший рост цен в ближайшие месяцы.',
            'tags': ['инфляция', 'экономика', 'финансы']
        },
        {
            'title': 'Новый прорыв в области искусственного интеллекта',
            'category': 'Технологии',
            'author': 'Алексей Иванов',
            'image': 'images/stock/News Image.avif',
            'content': 'Ученые из ведущего технологического университета представили революционную модель искусственного интеллекта, способную обучаться новым задачам в разы быстрее существующих аналогов. Новая архитектура нейронной сети демонстрирует беспрецедентную эффективность при решении комплексных задач, что открывает новые перспективы в таких областях, как медицина, климатическое моделирование и разработка новых материалов.',
            'tags': ['ии', 'технологии', 'инновации']
        },
        {
            'title': 'Сборная страны готовится к чемпионату мира',
            'category': 'Спорт',
            'author': 'Дмитрий Козлов',
            'image': 'images/stock/Reading Festival 2024 by Luke Dyson.avif',
            'content': 'Национальная сборная по футболу начала интенсивную подготовку к предстоящему чемпионату мира. Главный тренер команды представил расширенный список игроков, вызванных на сбор. В тренировочном лагере особое внимание уделяется тактической подготовке и физической форме футболистов. Первый матч турнира сборная сыграет против действующих чемпионов мира.',
            'tags': ['футбол', 'чемпионат мира', 'спорт']
        },
        {
            'title': 'Международный саммит по климату принял важные решения',
            'category': 'Мир',
            'author': 'Елена Соколова',
            'image': 'images/stock/SEI 259131270.avif',
            'content': 'Участники международного климатического саммита договорились о сокращении выбросов парниковых газов на 50% к 2030 году. В рамках соглашения развитые страны обязуются выделить 100 миллиардов долларов ежегодно на поддержку развивающихся государств в борьбе с изменением климата. Лидеры также договорились о создании международного фонда для компенсации ущерба от климатических катастроф.',
            'tags': ['климат', 'экология', 'международные отношения']
        },
        {
            'title': 'Ученые открыли новый метод лечения рака',
            'category': 'Наука',
            'author': 'Ольга Новикова',
            'image': 'images/stock/Harriet Haynes.avif',
            'content': 'Группа исследователей из ведущих медицинских центров мира объявила о разработке инновационного метода иммунотерапии онкологических заболеваний. Новая методика показала эффективность в 85% случаев при лечении ранее неизлечимых форм рака. Клинические испытания начнутся в ближайшие месяцы, а массовое внедрение технологии ожидается в течение трех лет.',
            'tags': ['медицина', 'рак', 'наука']
        },
        {
            'title': 'Новый фильм российского режиссера получил международное признание',
            'category': 'Культура',
            'author': 'Анна Кузнецова',
            'image': 'images/stock/News from The Independent.avif',
            'content': 'Картина молодого российского режиссера удостоилась специального приза жюри на Каннском кинофестивале. Фильм, снятый в жанре социальной драмы, рассказывает историю жизни в провинциальном городе. Критики отмечают сильную режиссерскую работу, глубокий сценарий и выдающуюся игру актеров. Премьера фильма в российском прокате запланирована на осень.',
            'tags': ['кино', 'культура', 'фестиваль']
        },
        {
            'title': 'Крупнейшая IT-компания объявила о новых инвестициях',
            'category': 'Бизнес',
            'author': 'Сергей Петров',
            'image': 'images/stock/Independent News Headlines.avif',
            'content': 'Ведущая мировая IT-корпорация объявила о планах инвестировать 10 миллиардов долларов в развитие искусственного интеллекта и облачных технологий. В рамках инициативы будет создано более 10 тысяч новых рабочих мест в сфере высоких технологий. Компания также анонсировала открытие новых исследовательских центров в нескольких странах мира.',
            'tags': ['бизнес', 'технологии', 'инвестиции']
        }
    ]
    
    # Create article pages
    for article in articles:
        slug = create_slug(article['title'])
        filename = f"{articles_dir}/{slug}.html"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(create_article_template(**article))
        
        print(f"Created: {filename}")
    
    print("\nAll articles have been created successfully!")

if __name__ == "__main__":
    main()
