function http_get_stock_reading() {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", 'http://127.0.0.1:8000/api/stock_readings/', true);
    xmlHttp.send();
    return JSON.parse(xmlHttp.responseText);
}

function http_post_stock_reading(data) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open('POST', 'http://127.0.0.1:8000/api/stock_readings/', true);
    xmlHttp.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    xmlHttp.onload = function () {
        // do something to response
        console.log(this.responseText);
    };
    var data = JSON.stringify(
        {"email": "hey@mail.com",
        "password": "101010"}
    );

    xmlHttp.send('user=person&pwd=password&organization=place&requiredkey=key');
    return JSON.parse(xmlHttp.responseText);
}

function create_stock_reading_list() {
    ul = document.createElement('ul');

    document.getElementById('myItemList').appendChild(ul);

    let items = [
            'Blue',
            'Red',
            'White',
            'Green',
            'Black',
            'Orange'
        ],
    items.forEach(function (item) {
        let li = document.createElement('li');
        ul.appendChild(li);

        li.innerHTML += item;
    });
}
