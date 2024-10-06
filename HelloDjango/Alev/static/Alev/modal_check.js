$(document).ready(function() {
    console.log(5555)
    // Инициализация маски для телефона
    $('[name="phone"]').mask("+7(999) 999-9999");

    function validatePhone(phone) {
        // Регулярное выражение для проверки в соответствии с маской
        const phonePattern = /^\+7\(\d{3}\) \d{3}-\d{4}$/;
        return phonePattern.test(phone);
    }

    function validateName(name) {
    return name.trim() !== '';
}
    // Обработчик события focusout для проверки номера телефона
    $('[name="phone"]').on('focusout', function() {
        if (!validatePhone($(this).val())) {
            alert('Неверный формат телефона! Ожидается: +7(999) 999-9999');
            $(this).focus(); // Возвращаем фокус на поле
            $(this).addClass('input-error'); // Добавляем класс ошибки
        } else {
            $(this).removeClass('input-error'); // Убираем класс ошибки
        }
    });


    // Обработчик события focusout для проверки имени
    $('[name="name"]').on('focusout', function () {
        if (!validateName($(this).val())) {
            alert('Неверный ');
            $(this).focus(); // Возвращаем фокус на поле
            $(this).addClass('input-error'); // Добавляем класс ошибки
        } else {
            $(this).removeClass('input-error'); // Убираем класс ошибки
        }

    })

    // Открытие модального окна
    $('.openModal').on('click', function() {
        console.log(5655)
        $('.modalwindow').fadeIn();
    });

    // Закрытие модального окна
    $('.closemodal').on('click', function() {
        $('.modalwindow').fadeOut();
    });

    // Обработчик отправки формы в модальном окне
    $('#submitModal').on('click', function(e) {
        if ($('.input-error').length > 0) {
            e.preventDefault(); // Отменяем действие по умолчанию (отправку формы)
            alert('Пожалуйста, исправьте ошибки перед отправкой формы.'); // Сообщение об ошибках
        } else {
            alert('Форма успешно отправлена!'); // Здесь можете добавить логику отправки формы
            $('.modalwindow').fadeOut(); // Закрываем модальное окно
        }
    });
});
