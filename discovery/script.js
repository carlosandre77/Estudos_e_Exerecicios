function toggleMode() {
    const html = document.documentElement

    // if(html.classList.contains('light')) {
    //     html.classList.remove('light')

    // } else {
    //     html.classList.add("light")
    // }
    html.classList.toggle('light')

    //pegar a imagem
    const img = document.querySelector("#profile img")

    //substituir imagem
    if(html.classList.contains('light')) {
        //se tiver light mode, adicionar a imagem light
        img.setAttribute('src',"./imagens/avatar-light.png")
    }else {
        // se tiver sem ligth mode, manter a imagem normal
        img.setAttribute('src',"./imagens/avatar.png")
    }
}