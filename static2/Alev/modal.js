//$(document).ready(function() {
//    // Открытие модального окна
//    $('.btn2').click(function (e) {
//        e.preventDefault();
//        $('.modalwindow').addClass('opened');
//        $('.modalwindow').attr('aria-hidden', 'false');
//    });
//
//    // Закрытие модального окна
//    $(document).on('click', '.closemodal', function (e) {
//        e.preventDefault();
//        $('.modalwindow').removeClass('opened');
//        $('.modalwindow').attr('aria-hidden', 'true');
//    });
//
//       $('#callForm').submit(function(e) {
//        console.log(454)
//        e.preventDefault(); // предотвращаем отправку формы по умолчанию
//
//        // Здесь можно выполнить валидацию, если нужно
//        console.log('Форма отправляется');
//
//        // Отправка данных на сервер
//        $.ajax({
//            type: 'POST',
//            url: $(this).attr('action'), // Если у вас указан URL в атрибуте action формы
//            data: $(this).serialize(), // Список данных формы
//            success: function() {
//                console.log('Форма успешно отправлена');
//                $('#callForm').load(window.location.href + " #callForm" );
//                $(".modalwindow").trigger('reset');
//                // Здесь вы можете закрыть модальное окно и обработать ответ сервера
//                $('.modalwindow').removeClass('opened');
//                // дополнительная логика для работы с ответом
//            },
//            error: function() {
//                alert('Что-то пошло не так');
//            },
//        });
//    });
//});
//
//
//$(document).ready(function() {
//    // Открытие модального окна
//    $('.btn2').click(function (e) {
//        e.preventDefault();
//        $('.modalwindow').addClass('opened');
//        $('.modalwindow').attr('aria-hidden', 'false');
//    });
//
//    // Закрытие модального окна
//    $(document).on('click', '.closemodal', function (e) {
//        e.preventDefault();
//        $('.modalwindow').removeClass('opened');
//        $('.modalwindow').attr('aria-hidden', 'true');
//        clearForm(); // Очистить форму при закрытии
//    });
//
//    function clearForm() {
//        document.getElementById('callForm').reset(); // Очистить форму
//        console.log(44);
//    }
//
//    // Отправка формы
//    $('#callForm').on('submit', function(e) {
//        e.preventDefault(); // предотвращаем стандартное поведение
//        $.ajax({
//            type: 'POST',
//            url: $(this).attr('action'),
//            data: $(this).serialize(),
//            success: function(response) {
//                console.log('Форма успешно отправлена');
//                // Обновляем только блок формы
//                $('#callForm').load(window.location.href + " #callForm > *"); // обновляем только содержимое формы
//                $('.modalwindow').removeClass('opened'); // Закрываем модальное окно
//            },
//            error: function() {
//                alert('Что-то пошло не так');
//            },
//        });
//    });
//});

$(document).ready(function() {
    // Открытие модального окна
    $('.btn2').click(function (e) {
        e.preventDefault();
        const modal = $(this).siblings('.modalwindow'); // Находим модальное окно, соответствующее кнопке
        modal.addClass('opened');
        modal.attr('aria-hidden', 'false');
    });

    // Закрытие модального окна
    $(document).on('click', '.closemodal', function (e) {
        e.preventDefault();
        const modal = $(this).closest('.modalwindow'); // Находим текущее модальное окно
        modal.removeClass('opened');
        modal.attr('aria-hidden', 'true');
        clearForm(modal.find('form')); // Передаем форму в функцию очистки
    });

    function clearForm(form) {
        form[0].reset(); // Очистить форму
        console.log(44);
    }
    // Отправка формы с AJAX
   // $(document).on('submit', '#callForm', function(e) {
   //     e.preventDefault(); // Предотвращаем стандартное поведение формы
   //     $.ajax({
   //         type: 'POST',
   //         url: $(this).attr('action'), // URL из атрибута action формы
   //         data: $(this).serialize(), // Данные формы
   //         success: function() {
   //             console.log('Форма успешно отправлена');
 ////               clearForm($('#callForm')); // Очистить форму после успешной отправки
   //             $('#callForm').trigger('reset');
   //             $('.modalwindow').removeClass('opened'); // Закрыть модальное окно
   //         },
   //         error: function() {
   //             alert('Что-то пошло не так');
   //         },
   //     });
   // });
//  $('.callForm').on('submit', function(e) {
//  e.preventDefault(); // Предотвращение стандартного поведения формы

//  $.ajax({
//      type: 'POST',
//      url: $(this).attr('action'),
//      data: $(this).serialize(),
//      success: function(response) {
//          console.log('Форма успешно отправлена');
//          $('.callForm').trigger('reset'); // Очищаем форму
//          $('.modalwindow').removeClass('opened'); // Закрываем модальное окно
//          alert('Отправлено');
//          // Дополнительная логика обработки ответа
//      },
//      error: function() {
//          console.log('Что-то пошло не так');
//      },
//  });
//});

//   $(document).on('submit', '.callForm', function(e) {
//       e.preventDefault(); // Предотвращаем стандартное поведение формы
//       $.ajax({
//           type: 'POST',
//           url: $(this).attr('action'), // URL из атрибута action формы
//           data: $(this).serialize(), // Данные формы
//           success: function(response) {
//               console.log(response)
//         //               console.log('Форма успешно отправлена');
//               $('.callForm').trigger('reset'); // Очистить форму после успешной отправки
//               $('.modalwindow').removeClass('opened'); // Закрыть модальное окно
//               alert('Отправлено');
//           },
//           error: function() {
//               alert('Что-то пошло не так');
//           },
//       });
//   });
//});

$(document).on('submit', '.callForm', function(e) {
    e.preventDefault(); // предотвращаем стандартное поведение формы
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val(); // получаем CSRF токен
    $.ajax({
        type: 'POST',
        url: $(this).attr('action'),
        data: $(this).serialize(),
        beforeSend: function(xhr) {
            xhr.setRequestHeader("X-CSRFToken", csrfToken); // установка CSRF токена
        },
        success: function(response) {
            console.log('Форма успешно отправлена');
            $('.callForm').trigger('reset'); // Очистка формы
            $('.modalwindow').removeClass('opened'); // Закрытие модального окна
        },
        error: function() {
            alert('Что-то пошло не так');
        },
    });
});
    });