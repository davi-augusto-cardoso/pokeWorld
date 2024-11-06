botao = document.getElementById("burger-bar");
menu = document.getElementById("menu");
botao.addEventListener("click", () => {
    if (menu.style.display === "none") {
        document.getElementById("burger-bar").innerHTML = "<img src='src/burger-menu-right-svgrepo-com.svg' alt='Botão de menu'></img>";
        menu.style.display = "flex";
    } else {
        document.getElementById("burger-bar").innerHTML = "<img src='src/burger-menu-svgrepo-com.svg' alt='Botão de menu'></img>";
        menu.style.display = "none";
    }
});