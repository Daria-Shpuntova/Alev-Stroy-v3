$(document).ready(function() {
    $(document).on('click', '.btn2', function () {
        $('.modalwindow').attr('aria-hidden', 'false');
        // Подставить нужные значения, если нужно
        // const title = $(this).data('title');
        // Обновите заголовок или другую информацию, если необходимо
        // $('#modalTitle').text(title);
        $('.modalwindow').addClass('opened'); // Открыть модальное окно
    });

//Закрытие модального окна
    $(document).on('click', '.closemodal', function (e) {
        e.preventDefault();
        $('.modalwindow').removeClass('opened');
        $('.modalwindow').attr('aria-hidden', 'true');
        clearForm(); // Очистить форму при закрытии

    });

    function clearForm() {
        document.getElementById('callForm').reset(); // Очистить форму
        console.log(44);
    }

    //Отправка формы с AJAX

    $('#callForm').submit(function (event) {
       event.preventDefault();
       console.log($(this).serialize());
       console.log($(this).attr('action'))
       console.log($(this).attr('method'))
       $.ajax({
           url: $(this).attr('action'),
           type: $(this).attr('method'),
           data: $(this).serialize(),
           success: function (){
                $('#serveses').load(window.location.href + " .serves");
                $('#callForm').trigger('reset');
                alert('Ваша заявка успешно отправлена!')
           },
           error: function (){
               alert('Что-то пошло не так');
           }
       });
    });
});
