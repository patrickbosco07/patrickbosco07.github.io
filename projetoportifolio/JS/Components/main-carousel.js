// 1 Acessar o browser
// 2 Pegar html todo
// 3 Pegar o botão
// 4 Checar se o botão está sendo clicado
// 5 Pegar o browser
// 6 Pegar o html todo
// 6 Pegar o elements
// 7 Mover o Elements para a direita

const buttonright = window.document.querySelector(".main-button-secaosobre.-right");
const buttonleft = window.document.querySelector(".main-button-secaosobre.-left");
const elements = window.document.querySelector(".elements");
let pixels = 100;


buttonright.addEventListener("click", function() {
    pixels = pixels + 100;
    elements.style = `transform: translateX(${pixels}px)`;
});

buttonleft.addEventListener("click", function() {
    pixels = pixels - 100;
    elements.style = `transform: translateX(${pixels}px)`;
});