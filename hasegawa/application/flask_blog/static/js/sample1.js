document.body.addEventListener("keyup", () => {
    
    document.getElementById("box").innerHTML = document.getElementById("InputText").value;
});
    
document.body.addEventListener("keyup", () => {
    document.getElementById("title").innerHTML = document.getElementById("InputTitle").value;
}); 

document.getElementById("h1").addEventListener("click", () => {
    document.getElementById("InputText").value += "<h1></h1>";
});
    
document.getElementById("h2").addEventListener("click", () => {
    document.getElementById("InputText").value += "<h2></h2>";
});

document.getElementById("h3").addEventListener("click", () => {
    document.getElementById("InputText").value += "<h3></h3>";
});

document.getElementById("p").addEventListener("click", () => {
    document.getElementById("InputText").value += "<p></p>";
});
 
document.getElementById("br").addEventListener("click", () => {
    document.getElementById("InputText").value += "<br>";
});

document.getElementById("list").addEventListener("click", () => {
    document.getElementById("InputText").value += "<ul><li></li></ul>";
});

document.getElementById("a").addEventListener("click", () => {
    document.getElementById("InputText").value += '<a href="url"></a>';
});

document.getElementById("imgsrc").addEventListener("click", () => {
    document.getElementById("InputText").value += "<img src='img/ここにimgの名前'>";
});