

var sleep = function(time) {
    var startTime = new Date().getTime() + parseInt(time, 10);
    while(new Date().getTime() < startTime) {}
};

function doit(){
document.getElementsByClassName("contact-btn")[0].click();
sleep(1000);
document.getElementsByClassName("add-product-operate")[0].getElementsByTagName("button")[0].click();
sleep(1000);
document.getElementsByClassName("ant-checkbox")[0].getElementsByTagName("input")[0].click();
sleep(1000);
document.getElementsByClassName("add-product__footer-wrapper")[0].getElementsByTagName("button")[0].click();
sleep(1000);
document.getElementsByClassName("drawer-footer-default")[0].getElementsByTagName("button")[0].click();
sleep(1000)
}
doit()




