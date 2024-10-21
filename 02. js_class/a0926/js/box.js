let num = 0;
let num2 = 0;
let num3 = 0;
$(function () {

  $("#right").click(function () {
    if (num >= 900) {
      alert("오른쪽 끝에 도달했습니다. 우측 이동은 불가합니다.")
    } else {
      $("#box").stop();
      num += 100;
      num2 += 360;
      $("#box").animate({ //funtion과 괄호 위치가 다름에 유의
        left: num, "rotate": num2 + "deg"
      }, 1000);
    }//else
  });//right

  $("#left").click(function () {
    if (num <= 0) {
      alert("왼쪽 끝에 도달했습니다. 좌측 이동은 불가합니다.");
      return false;
    } else {
      $("#box").stop();
      num -= 100;
      num2 -= 360;
      $("#box").animate({
        left: num, "rotate": num2 + "deg"
      }, 1000);
    };//else
  });//left

});//제이쿼리 선언