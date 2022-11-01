let resultado = document.getElementById("resultado").innerText;
console.log(resultado);

if(resultado != "") {
    var heightPage = document.body.scrollHeight;
    window.scrollTo(0 , heightPage);
}