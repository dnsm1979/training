const rectangle = {
    topLeft: { x: 0, y: 4 },
    bottomRight: { x: 6, y: 0 }
};

//1
function printRectangleInfo(rect) {
    console.log(`Top Left: (${rect.topLeft.x}, ${rect.topLeft.y})`);
    console.log(`Bottom Right: (${rect.bottomRight.x}, ${rect.bottomRight.y})`);
}

// 2
function calculateWidth(rect) {
    return rect.bottomRight.x - rect.topLeft.x;
}

// 3
function calculateHeight(rect) {
    return rect.topLeft.y - rect.bottomRight.y;
}

// 4
function calculateArea(rect) {
    return calculateWidth(rect) * calculateHeight(rect);
}

// 5
function calculatePerimeter(rect) {
    return 2 * (calculateWidth(rect) + calculateHeight(rect));
}

// 6
function changeWidth(rect, amount) {
    rect.bottomRight.x += amount;
}

// 7
function changeHeight(rect, amount) {
    rect.topLeft.y += amount;
}

// 8
function changeSize(rect, widthAmount, heightAmount) {
    changeWidth(rect, widthAmount);
    changeHeight(rect, heightAmount);
}

// 9
function moveX(rect, amount) {
    rect.topLeft.x += amount;
    rect.bottomRight.x += amount;
}

// 10
function moveY(rect, amount) {
    rect.topLeft.y -= amount;
    rect.bottomRight.y -= amount;
}

// 11
function moveXY(rect, amountX, amountY) {
    moveX(rect, amountX);
    moveY(rect, amountY);
}

// 12
function isPointInside(rect, point) {
    return point.x >= rect.topLeft.x && point.x <= rect.bottomRight.x &&
           point.y <= rect.topLeft.y && point.y >= rect.bottomRight.y;
}