window.onload = initAll; 


var addtoCart;
 
function initAll(){
    addtoCart = document.getElementById('sin_cart');
    addtoCart.onclick = addCart;
}

function addCart(){
    var sin = document.getElementById('pid').value;
    // var ul = 
   
    var rq = new XMLHttpRequest();
    rq.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        alert(rq.responseText);
      }
    };
    rq.open("GET",'/addtocart?pid='+sin, true);
    rq.send(); 
}

