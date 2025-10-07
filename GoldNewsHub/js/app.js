// Phase 1 : Juste un loader mock pour tester
document.addEventListener('DOMContentLoaded', () => {
    console.log('GoldNewsHub loaded ! 🪙');
    // Demain : fetch('data/mock-news.json').then(data => displayNews(data));
});

function displayNews(news) {
    const container = document.getElementById('news-container');
    container.innerHTML = ''; // Clear
    news.forEach(article => {
        const card = document.createElement('div');
        card.className = 'news-card';
        card.innerHTML = `
            <h3>${article.title}</h3>
            <p>${article.summary}</p>
            <a href="${article.link}">Lire plus</a>
            <small>Source: ${article.source} | ${article.date}</small>
        `;
        container.appendChild(card);
    });
}