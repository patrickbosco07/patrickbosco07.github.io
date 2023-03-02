const botaovoltar = window.document.querySelector(".botao-carrossel-left");
const botaoright = window.document.querySelector(".botao-carrossel-left.-right");
const elements = window.document.querySelector(".gallery");
var $pixel = 1247;

botaovoltar.addEventListener("click", function() {
    $pixel = $pixel - 1247;
    elements.style = `transform: translatex(${$pixel}px)`;
});

botaoright.addEventListener("click", function() {
    $pixel = $pixel + 1247;
    elements.style = `transform: translatex(${$pixel}px)`;
});
