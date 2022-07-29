function light(sw) {
    var pic;
    if (sw == 0) {
      pic = "pic_bulboff.gif"
    } else {
      pic = "pic_bulbon.gif"
    }
    document.getElementById('myImage').src = pic;
  }

  function change_demo(){
    // document.getElementById("demo").innerHTML="i'm writing this from javascript"
    document.getElementById("demo").style.background="red"

  }

  function sum (){
    let x,y;
    x = 5;
    y = 6;
    document.getElementById("demo").innerHTML = x + y;
  }
    



