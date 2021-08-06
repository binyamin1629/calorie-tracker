var male = document.getElementById('male')
var female = document.getElementById('female')
if (male.checked == false) {
  female.checked = true;
}

window.onscroll = function () { scorlpro }
function scorlpro() {
    var winscrol = document.body.scrollTop || document.documentElement.scrollTop;
    var hight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    var scroll = (winscrol / hight) * 100;
    document.getElementById("scorllbar").style.width = scroll + "%";
}