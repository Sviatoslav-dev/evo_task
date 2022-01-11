'use strict';

document.addEventListener('DOMContentLoaded', () => {
  const inputName = document.getElementById('input-name');
  const sayHello = document.getElementById('say-hello-button');
  const massage = document.getElementById('massage');

  sayHello.onclick = function() {
    fetch('/say_hello', {
        method: 'POST',
        body: JSON.stringify({"name": inputName.value}),
        cache: 'no-cache',
        headers: new Headers({
          'content-type': 'application/json',
        }),
    }).then(response => {
        return response.json()
    }).then(text => {
        massage.innerText = text[0]["result"]
        inputName.value = ""
    })
  };
})