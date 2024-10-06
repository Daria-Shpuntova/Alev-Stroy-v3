//$(function(){
//    $(".serves_menu").click(function(){
//        if ($(".menu_link1").hasClass("menu_link1_show")){
//            $(".menu_link1").removeClass("menu_link1_show");
//        } else {
//            $(".menu_link1").addClass("menu_link1_show");
//        }
//    });
//});

const openMenu = document.getElementById('serves_menu');
const menu = document.getElementById('menu_link1');
const body = document.body;

openMenu.addEventListener('click', (event) => {
    event.stopPropagation();
    menu.classList.toggle('hidden');
});

body.addEventListener('click', (event) => {
    if (event.target !== menu && !menu.contains(event.target)) {
        menu.classList.add('hidden');
    }
});



let submenuLiAll = document.querySelectorAll('.submenuLi')
console.log(submenuLiAll)

submenuLiAll.forEach(item => {
  item.addEventListener('mouseover', () => {
    // Удаляем класс у всех элементов
    submenuLiAll.forEach(i => i.classList.remove('active'));
    // Добавляем класс активному элементу
    item.classList.add('active');
  });
});

let typeKvAll = document.querySelectorAll('.type_repairLi')
console.log(typeKvAll)

typeKvAll.forEach(item => {
  item.addEventListener('mouseover', () => {
    // Удаляем класс у всех элементов
    typeKvAll.forEach(i => i.classList.remove('active'));
    // Добавляем класс активному элементу
    item.classList.add('active');
  });
});
