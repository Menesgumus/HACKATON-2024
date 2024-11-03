function send(number){
    var buttons = document.getElementsByClassName("buton");
    var input = document.getElementById("send-area");
    var sendButon = document.getElementById("buton");

    input.value = buttons[number-1].innerText;
    sendButon.click();
}