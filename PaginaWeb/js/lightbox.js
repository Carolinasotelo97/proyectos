const imagenes = document.querySelectorAll('.img-galeria')
const imagenesLight = document.querySelector('.agregar-imagen')
const contenedorLight = document.querySelector('.imagen-light')
const hamburguesa1 = document.querySelector('.hamburguesa')

imagenes.forEach(imagen =>{
    imagen.addEventListener('click', () =>{
        aparecerImagen(imagen.getAttribute('src')) //me va a devover la direccion de la imagen cada vez que le doy click
    })
})

contenedorLight.addEventListener('click', (e) =>{ //esto me indica que si le doy click a cualquier parte que no sea la imagen, esta se cierra
    if(e.target !== imagenesLight){
        contenedorLight.classList.toggle('show')
        imagenesLight.classList.toggle('show-image')
        hamburguesa1.style.opacity = '1' //esto es para que no se vea el icono de menu cuando abro la imagen tipo popup

    }
})
const aparecerImagen = (imagen) =>{
    imagenesLight.src = imagen
    contenedorLight.classList.toggle('show')
    imagenesLight.classList.toggle('show-image')
    hamburguesa1.style.opacity = '0'//esto es para que no se vea el icono de menu cuando abro la imagen tipo popup
}