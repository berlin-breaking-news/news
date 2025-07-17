const fs = require('fs');
const path = require('path');

const articlesDir = path.join(__dirname, 'pages/articles');
const outputFile = path.join(__dirname, 'pages/articles-list.json');

// Get all HTML files in the articles directory
const articleFiles = fs.readdirSync(articlesDir)
    .filter(file => file.endsWith('.html') && file !== 'template.html');

const articles = [];

articleFiles.forEach(file => {
    try {
        const filePath = path.join(articlesDir, file);
        const content = fs.readFileSync(filePath, 'utf8');
        
        // Extract title
        const titleMatch = content.match(/<title>(.*?)<\/title>/i);
        const title = titleMatch ? titleMatch[1].replace('| Independent Clone', '').trim() : '';
        
        // Extract description
        const descMatch = content.match(/<meta\s+name="description"\s+content="([^"]*)"\s*\/?>/i);
        const description = descMatch ? descMatch[1] : '';
        
        // Extract date
        const dateMatch = content.match(/<span class="article-date[^"]*">([^<]+)<\/span>/i);
        const date = dateMatch ? dateMatch[1] : '';
        
        // Extract tags
        const tagsMatch = content.match(/<div class="article-tags">([\s\S]*?)<\/div>/i);
        let tags = [];
        if (tagsMatch) {
            const tagMatches = tagsMatch[1].match(/<a[^>]*>([^<]+)<\/a>/g) || [];
            tags = tagMatches.map(tag => tag.replace(/<[^>]+>/g, '').trim());
        }
        
        // Get the URL relative to site root (without leading ./)
        const url = `articles/${file}`;
        
        articles.push({
            url,
            title,
            description,
            date,
            tags
        });
    } catch (error) {
        console.error(`Error processing ${file}:`, error);
    }
});

// Write the articles to a JSON file
fs.writeFileSync(outputFile, JSON.stringify(articles, null, 2));
console.log(`Generated ${articles.length} articles in ${outputFile}`);
