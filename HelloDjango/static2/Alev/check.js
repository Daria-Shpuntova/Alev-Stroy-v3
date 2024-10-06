//var input_name=document.querySelector('.name_text');
//
//input_name.onblur = () => {
//    let username = input_name.value;
//    if (username.length == 0){
//        document.querySelector('.error_name').innerHTML ='Name cannot blank';
//    } else if (username.length < 3 || 25 < username.length){
//        document.querySelector('.error_name').innerHTML='Name must be between 3 and 25';
//    } else {
//         document.querySelector('.error_name').innerHTML=" ";
//    }
//}
//
//
//$(document).ready(function(){
//$( ".email_text" ).focusout(function() {
//    var inputvalue = $(this).val();
//    var regemail = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
//    if((!regemail.test(inputvalue)) && (inputvalue!='')){
//        document.querySelector('.error_email').innerHTML="Email is not valid. It should be in the format 'email@domain.com'";
//    }else if(inputvalue == ''){
//        document.querySelector('.error_email').innerHTML="Email cannot blank";
//    }else{
//        document.querySelector('.error_email').innerHTML=" ";
//}
//});
//console.log(34567)
//console.log($('.phone_text'))
//console.log($('.form2.phone_text'))
//$('.form2.phone_text').focusout(function() {
//    var phone = $(this).val();
//    console.log(phone)
//    var regtel = /^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$/;
//    if(!regtel.test(phone)){
//        document.querySelector('.error_phone').innerHTML="Phone is not valid";
//    }else if (phone==" "){
//        document.querySelector('.error_phone').innerHTML="Phone cannot blank";
//    }else{
//        document.querySelector('.error_phone').innerHTML=" ";
//    }
//});
//});
//

//window.addEventListener('DOMContentLoaded', function() {
//    function validateName(name) {
//        return name.trim() !== '';
//    }
//
//    function validatePhone(phone) {
//        const phonePattern = /^\+7\(\d{3}\) \d{3}-\d{4}$/; // Пример паттерна для проверки телефона
//        return phonePattern.test(phone);
//    }
//
//    function addValidationListeners(formId) {
//        const form = document.getElementById(formId);
////        console.log(form)
//        const nameInput = form.querySelector('input[type="text"][id="id_name"]');
// //       console.log(nameInput)
//        const phoneInput = form.querySelector('input[type="text"][id="id_phone"]');
// //       console.log(phoneInput)
//        const btn = form.querySelector('button')
//
//        nameInput.addEventListener('input', function () {
//            if (!validateName(this.value)) {
//                this.classList.add("input-error");
//                console.log('name-error');
//                btn.disabled = true;
//            } else {
//                console.log('name-not-error');
//                this.classList.remove("input-error");
//                btn.disabled = false;
//            }
//        });
//
//        phoneInput.addEventListener('input', function () {
//            if (!validatePhone(this.value)) {
//                this.classList.add("input-error");
//                console.log('tel-error');
//                btn.disabled = true;
//            } else {
//                console.log('tel-not-error');
//                this.classList.remove("input-error");
//                btn.disabled = false;
//            }
//        });
//    }
//
//    addValidationListeners('calc_form');
//    addValidationListeners('request_form');
//
//    $(document).ready(function() {
//        $("#id_area").focusout(function () {
//            let inputValue = $(this).val();
//            let btn1 =  $("#btn1");
//            console.log(inputValue, 'inputValue')
//            console.log(inputValue.trim, 'inputValue.trim')
//            if (inputValue.trim() === ''){
//                this.classList.add("input-error");
//                console.log('area-error');
//                btn1.disabled = true;
//            } else {
//                console.log('area-not-error');
//                this.classList.remove('input-error');
//                btn1.disabled = false;
//            }
//
//
//
//        });
//    });
//});
//
//
//
//
////function Area() {
////    const area = document.getElementById('id_area')
////    if (area.trim() === '') {
////        area.classList.add("input-error");
////    } else {
////        area.classList.remove("input-error");
////    }
////}
//

//window.addEventListener('DOMContentLoaded', function() {
//    // ...

//    function validateForm(formId) {
//        const form = document.getElementById(formId);
//        const requiredInputs = form.querySelectorAll('input[required]');
//        let isValid = true;

//        requiredInputs.forEach(input => {
//            if (!validateInput(input)) {
//                isValid = false;
//            }
//        });
//
//        return isValid;
//    }
//
//    function validateInput(input) {
//        if (input.type === 'text') {
//            return input.value.trim() !== '';
//        } else if (input.type === 'tel') {
//            return validatePhone(input.value);
//        } else {
//            // добавить валидацию для других типов полей
//            return true;
//        }
//    }
//
//    function addValidationListener(formId) {
//        const form = document.getElementById(formId);
//        const requiredInputs = form.querySelectorAll('input[required]');
//
//        requiredInputs.forEach(input => {
//            input.addEventListener('input', function() {
//                if (!validateInput(this)) {
//                    this.classList.add("input-error");
//                    form.querySelector('button').disabled = true;
//                } else {
//                    this.classList.remove("input-error");
//                    form.querySelector('button').disabled = false;
//                }
//            });
//        });
//
//        form.addEventListener('submit', function(event) {
//            if (!validateForm(formId)) {
//                event.preventDefault();
//            }
//        });
//    }
//
//    addValidationListener('calc_form');
//    addValidationListener('request_form');
//});
//

//window.addEventListener('DOMContentLoaded', function() {
//    function validateName(name) {
//        return name.trim() !== '';
//    }

//    function validatePhone(phone) {
//        const phonePattern = /^\+7\(\d{3}\) \d{3}-\d{4}$/; // Пример паттерна для проверки телефона
//        return phonePattern.test(phone);
//    }
//
//    function validateArea(area) {
//        return area.trim() !== '';
//    }
//
//    function validateForm(form) {
//        const nameInput = form.querySelector('input[type="text"][id="id_name"]');
//        const phoneInput = form.querySelector('input[type="text"][id="id_phone"]');
//        const areaInput = form.querySelector('input[type="text"][id="id_area"]');
//
//        const isNameValid = validateName(nameInput.value);
//        const isPhoneValid = validatePhone(phoneInput.value);
//        const isAreaValid = areaInput ? validateArea(areaInput.value) : true; // полe area только в первой форме
//
//        return isNameValid && isPhoneValid && isAreaValid;
//    }
//
//    function addValidationListeners(formId) {
//        const form = document.getElementById(formId);
//        const btn = form.querySelector('button');
//
//        // Проверка валидации при вводе
//        form.addEventListener('input', function() {
//            if (validateForm(form)) {
//                btn.disabled = false;
//            } else {
//                btn.disabled = true;
//            }
//        });
//
//        // Проверка валидации перед отправкой формы
//        form.addEventListener('submit', function(event) {
//            if (!validateForm(form)) {
//                event.preventDefault(); // Отменяем отправку формы
//                alert("Пожалуйста, заполните все обязательные поля корректно."); // Сообщение об ошибке
//            }
//        });
//    }
//
//    addValidationListeners('calc_form');
//    addValidationListeners('request_form');
//});


//window.addEventListener('DOMContentLoaded', function() {
//    function validateName(name) {
//        return name.trim() !== '';
//    }
//
//    function validatePhone(phone) {
//        const phonePattern = /^\+7\(\d{3}\) \d{3}-\d{4}$/; // Пример паттерна для проверки телефона
//        return phonePattern.test(phone);
//    }
//
//    function addValidationListeners(formId) {
//        const form = document.getElementById(formId);
//        const nameInput = form.querySelector('input[type="text"][id="id_name"]');
//        const phoneInput = form.querySelector('input[type="text"][id="id_phone"]');
//        const areaInput = form.querySelector('input[type="text"][id="id_area"]'); // поле area
//        const btn = form.querySelector('button');
//
//        function updateSubmitButtonState() {
//            const isNameValid = validateName(nameInput.value);
//            const isPhoneValid = validatePhone(phoneInput.value);
//            const isAreaValid = formId === 'calc_form' ? (areaInput ? validateName(areaInput.value) : true) : true;
//
//            btn.disabled = !(isNameValid && isPhoneValid && isAreaValid);
//        }
//
//        nameInput.addEventListener('input', function () {
//            if (!validateName(this.value)) {
//                this.classList.add("input-error");
//                console.log('name-error');
//            } else {
//                this.classList.remove("input-error");
//                console.log('name-not-error');
//            }
//            updateSubmitButtonState();
//        });
//
//        phoneInput.addEventListener('input', function () {
//            if (!validatePhone(this.value)) {
//                this.classList.add("input-error");
//                console.log('tel-error');
//            } else {
//                this.classList.remove("input-error");
//                console.log('tel-not-error');
//            }
//            updateSubmitButtonState();
//        });
//
//        if (areaInput) {
//            areaInput.addEventListener('input', function () {
//                if (!validateName(this.value)) {
//                    this.classList.add("input-error");
//                    console.log('area-error');
//                } else {
//                    this.classList.remove("input-error");
//                    console.log('area-not-error');
//                }
//                updateSubmitButtonState();
//            });
//        }
//    }
//
//    addValidationListeners('calc_form');
//    addValidationListeners('request_form');
//});


//window.addEventListener('DOMContentLoaded', function() {
//    function validateName(name) {
//        return name.trim() !== '';
//    }
//
//    function validatePhone(phone) {
//        const phonePattern = /^\+7\(\d{3}\) \d{3}-\d{4}$/;
//        return phonePattern.test(phone);
//    }
//
//    function addValidationListeners(formId) {
//        const form = document.getElementById(formId);
//        const nameInput = form.querySelector('input[type="text"][id="id_name"]');
//        const phoneInput = form.querySelector('input[type="text"][id="id_phone"]');
//        const btn = form.querySelector('button[type="submit"]');
//
//        function validateForm() {
//            const isNameValid = validateName(nameInput.value);
//            const isPhoneValid = validatePhone(phoneInput.value);
//
//            btn.disabled = !(isNameValid && isPhoneValid);
//        }
//
//        nameInput.addEventListener('input', function () {
//            if (!validateName(this.value)) {
//                this.classList.add("input-error");
//            } else {
//                this.classList.remove("input-error");
//            }
//            validateForm();
//        });
//
//        phoneInput.addEventListener('input', function () {
//            if (!validatePhone(this.value)) {
//                this.classList.add("input-error");
//            } else {
//                this.classList.remove("input-error");
//            }
//            validateForm();
//        });
//
//    }
//
//    addValidationListeners('calc_form');
//    addValidationListeners('request_form');
//});
//

//window.addEventListener('DOMContentLoaded', function() {
//    function validateName(name) {
//        return name.trim() !== '';
//    }
//
//    function validatePhone(phone) {
//        const phonePattern = /^\+7\(\d{3}\) \d{3}-\d{4}$/;
//        return phonePattern.test(phone);
//    }
//
//    function addValidationListeners(formId) {
//        const form = document.getElementById(formId);
//        const nameInput = form.querySelector('input[type="text"][id="id_name"]');
//        const phoneInput = form.querySelector('input[type="text"][id="id_phone"]');
//        const btn = form.querySelector('button[type="submit"]');
//
//        function validateForm() {
//            const isNameValid = validateName(nameInput.value);
//            const isPhoneValid = validatePhone(phoneInput.value);
//
//   //         btn.disabled = !(isNameValid && isPhoneValid);
//
//            if (isNameValid && isPhoneValid) {
//                // Отправка формы через Ajax
//                const formData = new FormData(form);
//                const xhr = new XMLHttpRequest();
//                xhr.open('POST', form.action, true);
//                xhr.send(formData);
//                xhr.onload = function() {
//                    if (xhr.status === 200) {
//                        console.log('Форма отправлена успешно!');
//                        alert("Ваша заявка успешно отправлена!")
//                        form.reset();
//                    } else {
//                        console.log('Ошибка отправки формы!');
//                        alert("Ошибка при отправке!")
//                    }
//                };
//            }
//        }
//
//        nameInput.addEventListener('input', function () {
//            if (!validateName(this.value)) {
//                this.classList.add("input-error");
//            } else {
//                this.classList.remove("input-error");
//            }
//            validateForm();
//        });
//
//        phoneInput.addEventListener('input', function () {
//            if (!validatePhone(this.value)) {
//                this.classList.add("input-error");
//            } else {
//                this.classList.remove("input-error");
//            }
//            validateForm();
//        });
//
//        // Добавляем слушатель события submit для формы
//        form.addEventListener('submit', function(event) {
//            event.preventDefault();
//            validateForm();
//        });
//
////        // Добавляем слушатель события submit для формы
////        form.addEventListener('submit', function(event) {
////            event.preventDefault();
////            validateForm();
////        });
//    }
//
//    addValidationListeners('calc_form');
//    addValidationListeners('request_form');
//});
//
//
window.addEventListener('DOMContentLoaded', function() {
    function validateName(name) {
        return name.trim() !== '';
    }

    function validatePhone(phone) {
        const phonePattern = /^\+7\(\d{3}\) \d{3}-\d{4}$/;
        return phonePattern.test(phone);
    }

    function addValidationListeners(formId) {
        const form = document.getElementById(formId);
        const nameInput = form.querySelector('input[type="text"][id="id_name"]');
        const phoneInput = form.querySelector('input[type="text"][id="id_phone"]');
        const btn = form.querySelector('button[type="submit"]');
 //       const messageContainer = document.getElementById('message-container');

        function validateForm() {
            const isNameValid = validateName(nameInput.value);
            const isPhoneValid = validatePhone(phoneInput.value);

            if (isNameValid && isPhoneValid) {
                // Отправка формы через Ajax
                const formData = new FormData(form);
                const xhr = new XMLHttpRequest();
                xhr.open('POST', form.action, true);
                xhr.send(formData);
                xhr.onload = function() {
                    if (xhr.status === 200) {
                        console.log('Форма отправлена успешно!');
//                        messageContainer.innerHTML = 'Форма отправлена успешно!';
                        form.reset();
                    } else {
                        console.log('Ошибка отправки формы!');
//                        messageContainer.innerHTML = 'Ошибка отправки формы!';
                    }
                };
//            } else {
//                messageContainer.innerHTML = 'Пожалуйста, заполните все поля корректно!';
            }
        }

        nameInput.addEventListener('input', function () {
            if (!validateName(this.value)) {
                this.classList.add("input-error");
            } else {
                this.classList.remove("input-error");
            }
        });

        phoneInput.addEventListener('input', function () {
            if (!validatePhone(this.value)) {
                this.classList.add("input-error");
            } else {
                this.classList.remove("input-error");
            }
        });

        // Добавляем слушатель события submit для формы
        form.addEventListener('submit', function(event) {
            event.preventDefault();
            validateForm();
        });
    }

    addValidationListeners('calc_form');
    addValidationListeners('request_form');
});

