//let repair_list = {
//    '.q1': '.o1',
//    '.q2': '.o2',
//    '.q3': '.o3',
//    '.q4': '.o4',
//    '.q5': '.o5',
//    '.q6': '.o6',
//    '.q7': '.o7'
    //}
//
//
//for (const key in repair_list) {
//    $(function(){
//    $(key).click(function(){
//        if ($(repair_list[key]).hasClass("text-show")){
//            $(repair_list[key]).removeClass("text-show");
//        } else {
//            $(repair_list[key]).addClass("text-show");
//        };
//    });
//    });
//};

document.querySelectorAll('.quest .quiet1').forEach(question => {
    question.addEventListener('click', function () {
        // Скрываем все ответы
        document.querySelectorAll('.answer').forEach(answer => {
            answer.style.display = 'none';
        });

        // Получаем родительский элемент .quest
        const quest = this.closest('.quest');

        // Получаем ответ, который связан с текущим вопросом
        const answer = quest.querySelector('.answer');

        // Проверяем, видим ли мы текущий ответ
        if (answer.style.display === 'none' || answer.style.display === '') {
            // Показать текущий ответ
            answer.style.display = 'block';
        }
    });
});
