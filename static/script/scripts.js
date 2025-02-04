function form_handler(event) {
    event.preventDefault();
  }
  let show = document.getElementById('show');
  let hide = document.getElementById('hide');
  let menu = document.getElementById('menu');
  let parentDiv= document.getElementById('parentDiv');
  show.addEventListener('click', function() {
      show.classList.toggle('hidden');
      hide.classList.toggle('hidden');
      menu.classList.toggle('hidden');
      parentDiv.classList.add('flex-col');
  });

  hide.addEventListener('click', function() {
    show.classList.toggle('hidden');
    hide.classList.toggle('hidden');
    menu.classList.toggle('hidden');
    parentDiv.classList.remove('flex-col');
  });

  function send_data(event) {
    document.querySelector("form").addEventListener("submit", form_handler);
    var fd = new FormData(document.querySelector("form"));
    console.log(fd);
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/predict", true);
    document.getElementById("prediction").innerHTML =
      "Wait Predicting Price";
    xhr.onreadystatechange = function () {
      if (xhr.readyState == XMLHttpRequest.DONE) {
        var prediction = parseInt(xhr.responseText).toLocaleString();
        document.getElementById("prediction").innerHTML =
          "Prediction: ₹ " + prediction;
      }
    };
    xhr.onload = function () {};
    xhr.send(fd);
  }