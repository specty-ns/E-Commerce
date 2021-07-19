window.onload = initAll; 


var addtoCart;
 
function initAll(){
    addtoCart = document.getElementById('add_cart');
    addtoCart.onclick = addCart;
}

function addCart(){
    var pid = document.getElementById('pid').value;
    var url = 'addtocart?pid='+pid;
   
    var req = new XMLHttpRequest();
    req.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        alert(req.responseText);
      }
    };
    req.open("GET",url, true);
    req.send(); 
}

