burger = document.querySelector('.burger')
navbar = document.querySelector('#navbar');
nav_list = document.querySelector('#nav-list');

burger.addEventListener('click', ()=>{
    navbar.classList.toggle('h-nav');
    nav_list.classList.toggle('v-nav');
})