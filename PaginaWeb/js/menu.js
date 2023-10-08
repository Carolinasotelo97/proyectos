const hamburguesa = document.querySelector('.hamburguesa')
const menu = document.querySelector('.menu-navegacion')

hamburguesa.addEventListener('click', () =>{
     menu.classList.toggle("spread") //esto es para que cada vez que toco el icono de menu me muestro el contenido
})

window.addEventListener('click', e=>{ //e es el evento de hacer click en un lugar
    if(menu.classList.contains('spread') && e.target !=menu && e.target != hamburguesa){ //aca le digo que mientras tenga el spread y haga click  en el menu, este no se va a cerrar, pero si hago click en otro lado, si
        menu.classList.toggle("spread")
    }
})