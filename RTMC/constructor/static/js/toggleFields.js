// ____________________ load_participants _______________________________

// Функция загрузки файла
function uploadFile() {
    var fileInput = document.getElementById("file_input");
    var file = fileInput.files[0];
    var reader = new FileReader();
  
    reader.onload = function (e) {
      var contents = e.target.result;
    };
  
    reader.readAsText(file);
  }
  
  // Функция для ручного ввода участников
  document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("add_person_form");
    const tableBody = document.querySelector("#person_table tbody");
    let counter = 1;
  
    form.addEventListener("submit", function (event) {
      event.preventDefault();
  
      const firstName = document.getElementById("first_name").value;
      const lastName = document.getElementById("last_name").value;
      const middleName = document.getElementById("middle_name").value;
  
      const newRow = document.createElement("tr");
      newRow.innerHTML = `
                      <td>${counter}</td>
                      <td>${firstName}</td>
                      <td>${lastName}</td>
                      <td>${middleName}</td>
                  `;
      tableBody.appendChild(newRow);
  
      counter++;
      form.reset();
    });
  });
  
  // ____________________ load_participants _______________________________
  
  
  
  // _______________________ chose_template _______________________________
  
  const form = document.getElementById('template-form');
  const templatesList = document.getElementById('templates-list');
  const noResults = document.getElementById('no-results');
  
  form.addEventListener('submit', function (event) {
      event.preventDefault();
  
      const query = document.getElementById('template-name').value;
  
      // Здесь отправляем запрос на сервер для поиска шаблонов
      // В этом примере используем статические данные для демонстрации
  
      fetch(`https://example.com/search?query=${query}`)
          .then(response => response.json())
          .then(data => {
              templatesList.innerHTML = '';
              if (data.length > 0) {
                  data.forEach(template => {
                      const li = document.createElement('li');
                      const a = document.createElement('a');
                      a.href = `template-details.html?id=${template.id}`;
                      a.textContent = template.name;
                      li.appendChild(a);
                      templatesList.appendChild(li);
                  });
              } else {
                  noResults.style.display = 'block';
              }
          })
          .catch(error => {
              console.error('Error:', error);
              noResults.style.display = 'block';
          });
  });
  
  // _______________________ chose_template _______________________________
  
  
  
  // _______________________ make_template ________________________________
  
  // _______________________ make_template_________________________________
  
  
  
  // ________________________ password_reset_form _________________________
  
  function contactAdmin() {
    alert("Обратитесь к администратору для смены пароля.");
  }
  
  // ________________________ password_reset_form _________________________
  