// 1
class PrintMachine {
    constructor(size, color, type) {
        this.size = size;
        this.color = color;
        this.type = type;
    }
    print(text) {
        document.write('<p style="size: ${this.size}; color: ${this.color}; type: ${this.type};">${text}</p>');
    }

}

let printer = new PrintMachine('16px', 'red', 'Arial');

printer.print('Hello World');

// 2
class News {
    constructor(title, text, tags, date) {
        this.title = title;
        this.text = text;
        this.tags = tags;
        this.date = new Date(publicationDate);
    }

    print() {
        const currentDate = new Date();
        const timeDiff = currentDate - this.publicationDate;
        const oneDay = 24 * 60 * 60 * 1000;
        const daysDiff = Math.floor(timeDiff / oneDay);

        if (daysDiff < 1) {
            console.log(`Title: ${this.title}`);
            console.log(`Text: ${this.text}`);
            console.log(`Tags: ${this.tags.join(', ')}`);
            console.log('Publication Date: сегодня');
        } else if (daysDiff < 7) {
            console.log(`Title: ${this.title}`);
            console.log(`Text: ${this.text}`);
            console.log(`Tags: ${this.tags.join(', ')}`);
            console.log(`Publication Date: ${daysDiff} дней назад`);
        } else {
            const formattedDate = `${String(this.publicationDate.getDate()).padStart(2, '0')}.${String(this.publicationDate.getMonth() + 1).padStart(2, '0')}.${this.publicationDate.getFullYear()}`;
            console.log(`Title: ${this.title}`);
            console.log(`Text: ${this.text}`);
            console.log(`Tags: ${this.tags.join(', ')}`);
            console.log(`Publication Date: ${formattedDate}`);
        }
    }
}


const newsToday = new News('Последние новости сегодня', 'Это новостная статья, опубликованная сегодня.', ['news', 'today'], new Date());
const newsYesterday = new News('Вчерашние новости', 'Это новостная статья, опубликованная вчера.', ['news', 'yesterday'], new Date(Date.now() - (24 * 60 * 60 * 1000)));
const newsWeekAgo = new News('Новости недельной давности', 'Это новостная статья, опубликованная неделю назад.', ['news', 'past'], new Date(Date.now() - (7 * 24 * 60 * 60 * 1000)));


newsToday.print();
newsYesterday.print();
newsWeekAgo.print();

// 3
class NewsFeed {
    constructor() {
        this.news = [];
    }

    get count() {
        return this.news.length;
    }

    displayAllNews() {
        this.news.forEach((item, index) => {
            console.log(`News ${index + 1}:`);
            console.log(`Title: ${item.title}`);
            console.log(`Text: ${item.text}`);
            console.log(`Tags: ${item.tags.join(', ')}`);
            console.log(`Publication Date: ${item.publicationDate}`);
            console.log('------------------------');
        });
    }

    addNews(title, text, tags, publicationDate) {
        this.news.push({ title, text, tags, publicationDate });
    }

    deleteNews(index) {
        if (index >= 0 && index < this.news.length) {
            this.news.splice(index, 1);
            console.log(`Новость ${index} успешно удалена.`);
        } else {
            console.log('Неверный индекс. Не удалось удалить новость.');
        }
    }

    sortByDate() {
        this.news.sort((a, b) => new Date(b.publicationDate) - new Date(a.publicationDate));
    }

    searchByTag(tag) {
        return this.news.filter(item => item.tags.includes(tag));
    }
}


const newsFeed = new NewsFeed();


newsFeed.addNews('Последние новости', 'Это статья последних новостей.', ['news', 'breaking'], '2024-05-30');
newsFeed.addNews('Новости технологий', 'На этой неделе выпущены новые технические гаджеты.', ['tech', 'gadgets'], '2024-05-29');
newsFeed.addNews('Новости спорта', 'Интересные результаты матчей за выходные.', ['sports', 'results'], '2024-05-28');


newsFeed.displayAllNews();


newsFeed.deleteNews(1);


newsFeed.sortByDate();
newsFeed.displayAllNews();


const techNews = newsFeed.searchByTag('tech');
console.log('Tech News:');
techNews.forEach((item, index) => {
    console.log(`Title: ${item.title}`);
});