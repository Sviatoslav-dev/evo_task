'use strict';

document.addEventListener('DOMContentLoaded', () => {
    const page = parseInt(document.getElementById('page').innerText);
    const pages = parseInt(document.getElementById('pages').innerText);
    const prev = document.getElementById('prev');
    const next = document.getElementById('next');
    const sayHello = document.getElementById('say-hello');

    sayHello.onclick = function() {
        document.location.href = "/"
    }

    if (page === 1) {
        prev.style.visibility = "hidden";
    }

    if (page === pages) {
        next.style.visibility = "hidden";
    }

    next.onclick = function() {
        document.location.href = "/all_names/" + (page + 1).toString()
    }

    prev.onclick = function() {
        document.location.href = "/all_names/" + (page - 1).toString()
    }
})