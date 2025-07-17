#!/bin/bash

# Create pages directory if it doesn't exist
mkdir -p pages

# Function to create a page
create_page() {
    local filename=$1
    local title=$2
    local description=$3
    local content=$4
    
    cat > "pages/$filename" << EOF
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>$title | Independent Clone</title>
    <meta name="description" content="$description">
    <link rel="stylesheet" href="../css/style.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <meta name="color-scheme" content="light">
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
                    <a href="../index.html" class="logo">
                        <h1>Independent</h1>
                        <span>Clone</span>
                    </a>
                    
                    <nav class="main-nav">
                        <ul>
                            <li><a href="../index.html">Главная</a></li>
                            <li><a href="politika.html">Политика</a></li>
                            <li><a href="mir.html">Мир</a></li>
                            <li><a href="sport.html">Спорт</a></li>
                            <li><a href="kultura.html">Культура</a></li>
                            <li><a href="tehnologii.html">Технологии</a></li>
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

    <!-- Page Content -->
    <main class="main-content">
        <div class="container">
            <h1 class="page-title">$title</h1>
            <div class="page-content">
                $content
            </div>
        </div>
    </main>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h3>Разделы</h3>
                    <ul>
                        <li><a href="../index.html">Главная</a></li>
                        <li><a href="politika.html">Политика</a></li>
                        <li><a href="mir.html">Мир</a></li>
                        <li><a href="sport.html">Спорт</a></li>
                        <li><a href="kultura.html">Культура</a></li>
                        <li><a href="tehnologii.html">Технологии</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h3>Компания</h3>
                    <ul>
                        <li><a href="o-nas.html">О нас</a></li>
                        <li><a href="kontakty.html">Контакты</a></li>
                        <li><a href="reklama.html">Реклама</a></li>
                        <li><a href="vakansii.html">Вакансии</a></li>
                        <li><a href="pomoshch.html">Помощь</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h3>Правовая информация</h3>
                    <ul>
                        <li><a href="#">Политика конфиденциальности</a></li>
                        <li><a href="#">Условия использования</a></li>
                        <li><a href="#">Правила комментирования</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h3>Подписаться</h3>
                    <p>Будьте в курсе последних новостей</p>
                    <form class="newsletter-form">
                        <input type="email" placeholder="Ваш email" required>
                        <button type="submit" class="subscribe-btn">Подписаться</button>
                    </form>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2025 Independent Clone. Все права защищены.</p>
            </div>
        </div>
    </footer>

    <script src="../js/script.js"></script>
</body>
</html>
EOF
}

# Create pages
create_page "o-nas.html" "О нас" "Узнайте больше о Independent Clone - вашем надежном источнике новостей" "
<section class='about-section'>
    <h2>Наша миссия</h2>
    <p>Independent Clone - это современное цифровое издание, которое стремится предоставлять своим читателям актуальные, достоверные и объективные новости. Мы верим в силу информации и её способность менять мир к лучшему.</p>
    
    <h2>Наша команда</h2>
    <p>Над созданием контента работают опытные журналисты, редакторы и аналитики, которые придерживаются высоких стандартов журналистики. Наша команда объединяет профессионалов с разным опытом и взглядами, что позволяет нам освещать события с разных сторон.</p>
    
    <h2>Наши принципы</h2>
    <ul>
        <li><strong>Объективность</strong> - мы стремимся к беспристрастному освещению событий</li>
        <li><strong>Достоверность</strong> - вся информация тщательно проверяется перед публикацией</li>
        <li><strong>Открытость</strong> - мы всегда готовы к диалогу с нашими читателями</li>
        <li><strong>Инновации</strong> - мы используем современные технологии для подачи информации</li>
    </ul>
</section>"

create_page "kontakty.html" "Контакты" "Свяжитесь с нами - мы всегда на связи" "
<section class='contacts-section'>
    <div class='contact-info'>
        <h2>Контактная информация</h2>
        <p><i class='fas fa-map-marker-alt'></i> <strong>Адрес:</strong> г. Москва, ул. Примерная, д. 123</p>
        <p><i class='fas fa-phone'></i> <strong>Телефон:</strong> +7 (495) 123-45-67</p>
        <p><i class='fas fa-envelope'></i> <strong>Email:</strong> info@independent-clone.ru</p>
        <p><i class='fas fa-clock'></i> <strong>Режим работы:</strong> Пн-Пт: 9:00 - 18:00</p>
    </div>
    
    <div class='contact-form'>
        <h2>Напишите нам</h2>
        <form>
            <div class='form-group'>
                <label for='name'>Ваше имя</label>
                <input type='text' id='name' name='name' required>
            </div>
            <div class='form-group'>
                <label for='email'>Email</label>
                <input type='email' id='email' name='email' required>
            </div>
            <div class='form-group'>
                <label for='subject'>Тема</label>
                <input type='text' id='subject' name='subject' required>
            </div>
            <div class='form-group'>
                <label for='message'>Сообщение</label>
                <textarea id='message' name='message' rows='5' required></textarea>
            </div>
            <button type='submit' class='btn'>Отправить сообщение</button>
        </form>
    </div>
</section>"

create_page "reklama.html" "Реклама" "Рекламные возможности на Independent Clone" "
<section class='advertising-section'>
    <h2>Реклама на нашем сайте</h2>
    <p>Размещение рекламы на Independent Clone - это эффективный способ донести ваше коммерческое предложение до целевой аудитории. Наш сайт посещает большое количество заинтересованных пользователей, что делает рекламу у нас выгодным вложением.</p>
    
    <h3>Наши преимущества</h3>
    <ul>
        <li>Большая аудитория целевых посетителей</li>
        <li>Гибкие условия размещения</li>
        <li>Возможность таргетинга по интересам</li>
        <li>Детальная статистика показов и кликов</li>
        <li>Профессиональная поддержка</li>
    </ul>
    
    <h3>Форматы рекламы</h3>
    <div class='ad-formats'>
        <div class='ad-format'>
            <h4>Баннерная реклама</h4>
            <p>Размещение графических баннеров в различных частях сайта</p>
        </div>
        <div class='ad-format'>
            <h4>Нативная реклама</h4>
            <p>Органичное размещение рекламных материалов в ленте новостей</p>
        </div>
        <div class='ad-format'>
            <h4>Спонсорские материалы</h4>
            <p>Публикация статей и обзоров о вашей компании или продукте</p>
        </div>
    </div>
    
    <div class='contact-promo'>
        <p>Для уточнения условий сотрудничества свяжитесь с нашим отделом рекламы:</p>
        <p><i class='fas fa-envelope'></i> <a href='mailto:ads@independent-clone.ru'>ads@independent-clone.ru</a></p>
        <p><i class='fas fa-phone'></i> +7 (495) 987-65-43</p>
    </div>
</section>"

create_page "vakansii.html" "Вакансии" "Присоединяйтесь к нашей команде" "
<section class='vacancies-section'>
    <h2>Работа в Independent Clone</h2>
    <p>Мы всегда рады талантливым и увлеченным специалистам, готовым развиваться вместе с нами. Присоединяйтесь к нашей команде профессионалов!</p>
    
    <div class='vacancy-list'>
        <article class='vacancy'>
            <h3>Журналист-новостник</h3>
            <p class='location'><i class='fas fa-map-marker-alt'></i> Москва / Удаленно</p>
            <div class='description'>
                <p>Ищем журналиста для оперативного освещения новостей в различных сферах.</p>
                <h4>Требования:</h4>
                <ul>
                    <li>Опыт работы в СМИ от 2 лет</li>
                    <li>Умение работать в условиях цейтнота</li>
                    <li>Грамотная устная и письменная речь</li>
                    <li>Знание основ журналистики и этики</li>
                </ul>
                <a href='#apply' class='btn'>Откликнуться</a>
            </div>
        </article>
        
        <article class='vacancy'>
            <h3>Верстальщик</h3>
            <p class='location'><i class='fas fa-map-marker-alt'></i> Москва / Удаленно</p>
            <div class='description'>
                <p>Требуется верстальщик для работы над веб-проектами издания.</p>
                <h4>Требования:</h4>
                <ul>
                    <li>Опыт верстки от 1 года</li>
                    <li>Знание HTML5, CSS3, JavaScript</li>
                    <li>Опыт работы с препроцессорами (Sass/Less)</li>
                    <li>Знание основ адаптивной верстки</li>
                </ul>
                <a href='#apply' class='btn'>Откликнуться</a>
            </div>
        </article>
    </div>
    
    <div class='how-to-apply'>
        <h3>Как откликнуться на вакансию?</h3>
        <p>Отправьте свое резюме на <a href='mailto:hr@independent-clone.ru'>hr@independent-clone.ru</a> с указанием желаемой должности в теме письма.</p>
    </div>
</section>"

create_page "pomoshch.html" "Помощь" "Центр поддержки Independent Clone" "
<section class='help-section'>
    <h2>Центр поддержки</h2>
    <p>Мы всегда готовы помочь вам с любыми вопросами, связанными с работой нашего сайта и сервисов.</p>
    
    <div class='help-categories'>
        <div class='help-category'>
            <h3><i class='fas fa-question-circle'></i> Частые вопросы</h3>
            <div class='faq-list'>
                <div class='faq-item'>
                    <h4>Как подписаться на рассылку?</h4>
                    <p>Для подписки на нашу рассылку найдите форму подписки в подвале сайта и укажите свой email-адрес.</p>
                </div>
                <div class='faq-item'>
                    <h4>Как связаться с редакцией?</h4>
                    <p>Вы можете написать нам на почту <a href='mailto:info@independent-clone.ru'>info@independent-clone.ru</a> или воспользоваться <a href='kontakty.html'>формой обратной связи</a>.</p>
                </div>
                <div class='faq-item'>
                    <h4>Как подать новость?</h4>
                    <p>Если у вас есть новость, присылайте её на почту <a href='mailto:news@independent-clone.ru'>news@independent-clone.ru</a> с пометкой "Новость".</p>
                </div>
            </div>
        </div>
        
        <div class='help-category'>
            <h3><i class='fas fa-book'></i> Полезные статьи</h3>
            <ul class='article-list'>
                <li><a href='#'>Как пользоваться нашим сайтом</a></li>
                <li><a href='#'>Правила комментирования</a></li>
                <li><a href='#'>Как отписаться от рассылки</a></li>
                <li><a href='#'>Мобильное приложение: инструкция</a></li>
            </ul>
        </div>
    </div>
    
    <div class='contact-support'>
        <h3>Не нашли ответ на свой вопрос?</h3>
        <p>Напишите нам, и мы постараемся помочь в кратчайшие сроки.</p>
        <a href='kontakty.html' class='btn'>Связаться с поддержкой</a>
    </div>
</section>"

# News category pages
create_page "politika.html" "Политика" "Последние политические новости и события" "
<section class='category-news'>
    <h2>Политические новости</h2>
    <div class='news-list'>
        <article class='news-item'>
            <img src='../images/politics1.jpg' alt='Политическая новость 1'>
            <div class='news-content'>
                <h3>Важное политическое событие</h3>
                <p class='meta'>Сегодня в 10:30</p>
                <p>Краткое описание политического события, которое привлекло внимание общественности.</p>
                <a href='#' class='read-more'>Читать далее</a>
            </div>
        </article>
        <!-- More news items -->
    </div>
</section>"

create_page "mir.html" "Мир" "Международные новости и события" "
<section class='category-news'>
    <h2>Новости мира</h2>
    <div class='news-list'>
        <article class='news-item'>
            <img src='../images/world1.jpg' alt='Мировая новость 1'>
            <div class='news-content'>
                <h3>Важное мировое событие</h3>
                <p class='meta'>Сегодня в 12:45</p>
                <p>Актуальные новости со всего мира, которые влияют на глобальную политику и экономику.</p>
                <a href='#' class='read-more'>Читать далее</a>
            </div>
        </article>
        <!-- More news items -->
    </div>
</section>"

create_page "sport.html" "Спорт" "Свежие спортивные новости и результаты" "
<section class='category-news'>
    <h2>Спортивные новости</h2>
    <div class='news-list'>
        <article class='news-item'>
            <img src='../images/sports1.jpg' alt='Спортивная новость 1'>
            <div class='news-content'>
                <h3>Главное спортивное событие дня</h3>
                <p class='meta'>Сегодня в 15:20</p>
                <p>Обзор матчей, интервью со спортсменами и последние новости из мира спорта.</p>
                <a href='#' class='read-more'>Читать далее</a>
            </div>
        </article>
        <!-- More news items -->
    </div>
</section>"

create_page "kultura.html" "Культура" "Новости культуры, искусства и шоу-бизнеса" "
<section class='category-news'>
    <h2>Культура и искусство</h2>
    <div class='news-list'>
        <article class='news-item'>
            <img src='../images/culture1.jpg' alt='Культурная новость 1'>
            <div class='news-content'>
                <h3>Главное культурное событие недели</h3>
                <p class='meta'>Сегодня в 18:10</p>
                <p>Анонсы выставок, театральных премьер, кинопоказов и других культурных событий.</p>
                <a href='#' class='read-more'>Читать далее</a>
            </div>
        </article>
        <!-- More news items -->
    </div>
</section>"

create_page "tehnologii.html" "Технологии" "Новости технологий и инноваций" "
<section class='category-news'>
    <h2>Технологии и наука</h2>
    <div class='news-list'>
        <article class='news-item'>
            <img src='../images/tech1.jpg' alt='Техническая новость 1'>
            <div class='news-content'>
                <h3>Главное технологическое событие</h3>
                <p class='meta'>Сегодня в 14:30</p>
                <p>Последние новости из мира технологий, обзоры гаджетов и научные открытия.</p>
                <a href='#' class='read-more'>Читать далее</a>
            </div>
        </article>
        <!-- More news items -->
    </div>
</section>"

echo "Все страницы успешно созданы в директории pages/"
