// 1
class Circle {
    constructor(radius) {
        this._radius = radius;
    }

    get radius() {
        return this._radius;
    }

    set radius(newRadius) {
        this._radius = newRadius;
    }

    get diameter() {
        return this._radius * 2;
    }

    calculateArea() {
        return Math.PI * this._radius ** 2;
    }

    calculatePerimeter() {
        return 2 * Math.PI * this._radius;
    }
}

const myCircle = new Circle(5);

console.log(`Radius: ${myCircle.radius}`);
console.log(`Diameter: ${myCircle.diameter}`);

myCircle.radius = 7;
console.log(`New Radius: ${myCircle.radius}`);


console.log(`Area: ${myCircle.calculateArea().toFixed(2)}`);


console.log(`Perimeter: ${myCircle.calculatePerimeter().toFixed(2)}`);

// 2

class HtmlElement {
    constructor(tagName, selfClosing = false, content = '') {
        this.tagName = tagName;
        this.selfClosing = selfClosing;
        this.content = content;
        this.attributes = [];
        this.styles = [];
        this.children = [];
    }

    setAttribute(name, value) {
        this.attributes.push({ name, value });
    }

    setStyle(property, value) {
        this.styles.push({ property, value });
    }

    appendChild(childElement) {
        this.children.push(childElement);
    }

    prependChild(childElement) {
        this.children.unshift(childElement);
    }

    getHtml() {
        let elementHtml = `<${this.tagName}`;

        for (const attribute of this.attributes) {
            elementHtml += ` ${attribute.name}="${attribute.value}"`;
        }

        if (this.styles.length > 0) {
            elementHtml += ` style="`;
            for (const style of this.styles) {
                elementHtml += `${style.property}: ${style.value}; `;
            }
            elementHtml += `"`;
        }

        elementHtml += this.selfClosing ? " />" : ">";
        
        if (!this.selfClosing) {
            if (this.content) {
                elementHtml += this.content;
            }
        
            for (const child of this.children) {
                elementHtml += child.getHtml();
            }
            
            elementHtml += `</${this.tagName}>`;
        }

        return elementHtml;
    }
}

// Создаем блок div с классом и вложенным элементом
const div = new HtmlElement('div', false);
div.setAttribute('class', 'container');

const p = new HtmlElement('p', false, 'Hello, World!');
p.setStyle('color', 'blue');

div.appendChild(p);

// Добавляем созданный блок на страницу
document.write(div.getHtml());

// 3

class CssClass {
    constructor(className) {
        this.className = className;
        this.styles = [];
    }

    setStyle(property, value) {
        this.styles.push({ property, value });
    }

    removeStyle(property) {
        this.styles = this.styles.filter(style => style.property !== property);
    }

    getCss() {
        let cssCode = `.${this.className} {`;

        for (const style of this.styles) {
            cssCode += `${style.property}: ${style.value}; `;
        }

        cssCode += `}`;

        return cssCode;
    }
}

// Создаем CSS класс с названием 'highlight'
const highlightClass = new CssClass('highlight');
highlightClass.setStyle('background-color', 'yellow');
highlightClass.setStyle('color', 'black');

// Удаляем стиль 'background-color'
highlightClass.removeStyle('background-color');

// Выводим CSS код для класса 'highlight'
console.log(highlightClass.getCss());

// 4
class CssClass {
    constructor(className) {
        this.className = className;
        this.styles = [];
    }

    setStyle(property, value) {
        this.styles.push({ property, value });
    }

    removeStyle(property) {
        this.styles = this.styles.filter(style => style.property !== property);
    }

    getCss() {
        let cssCode = `.${this.className} {`;

        for (const style of this.styles) {
            cssCode += `${style.property}: ${style.value}; `;
        }

        cssCode += `}`;

        return cssCode;
    }
}

class HtmlElement {
    constructor(tagName, selfClosing = false, content = '') {
        this.tagName = tagName;
        this.selfClosing = selfClosing;
        this.content = content;
        this.attributes = [];
        this.styles = [];
        this.children = [];
    }

    setAttribute(name, value) {
        this.attributes.push({ name, value });
    }

    setStyle(property, value) {
        this.styles.push({ property, value });
    }

    appendChild(childElement) {
        this.children.push(childElement);
    }

    getHtml() {
        let elementHtml = `<${this.tagName}`;

        for (const attribute of this.attributes) {
            elementHtml += ` ${attribute.name}="${attribute.value}"`;
        }

        if (this.styles.length > 0) {
            elementHtml += ` style="`;
            for (const style of this.styles) {
                elementHtml += `${style.property}: ${style.value}; `;
            }
            elementHtml += `"`;
        }

        elementHtml += this.selfClosing ? " />" : ">";

        if (!this.selfClosing) {
            if (this.content) {
                elementHtml += this.content;
            }

            for (const child of this.children) {
                elementHtml += child.getHtml();
            }

            elementHtml += `</${this.tagName}>`;
        }

        return elementHtml;
    }
}

class HtmlBlock {
    constructor() {
        this.styles = [];
        this.rootElement = null;
    }

    addCssClass(cssClass) {
        this.styles.push(cssClass);
    }

    setRootElement(element) {
        this.rootElement = element;
    }

    getCode() {
        let htmlCode = '';

        // Generating CSS code
        for (const cssClass of this.styles) {
            htmlCode += `<style>${cssClass.getCss()}</style>`;
        }

        // Generating HTML code
        if (this.rootElement) {
            htmlCode += this.rootElement.getHtml();
        }

        return htmlCode;
    }
}

// Создаем HtmlBlock
const htmlBlock = new HtmlBlock();

// Создаем CSS класс с названием 'highlight'
const highlightClass = new CssClass('highlight');
highlightClass.setStyle('background-color', 'yellow');
highlightClass.setStyle('color', 'black');

// Создаем блок div с классом 'container'
const div = new HtmlElement('div', false);
div.setAttribute('class', 'container');

const p = new HtmlElement('p', false, 'Hello, World!');
p.setStyle('font-size', '20px');

div.appendChild(p);

// Добавляем CSS класс и корневой элемент в HtmlBlock
htmlBlock.addCssClass(highlightClass);
htmlBlock.setRootElement(div);

// Добавляем созданный блок на страницу
document.write(htmlBlock.getCode());