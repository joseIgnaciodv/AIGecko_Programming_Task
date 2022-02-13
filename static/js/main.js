function prueba(){
    p = document.getElementsByName('image_upload').values
    console.dir(p)
    document.getElementById('prueba').innerHTML = p[0]
}