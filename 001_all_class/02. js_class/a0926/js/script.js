$(function () {
  var d_num = $(this).closest("tr").attr("id");
  var count = 1;
  var avg = 0;
  var total = 0;
  var d_data = "" //(!)

  //1. ajax 활용 데이터 가져오기 버튼
  $(document).on("click", "#dataBtn", function () { //(!)
    alert("데이터를 가져옵니다.");
    $.ajax({
      url: "js/stuData.json", //(!)
      type: "get",
      data: "",
      datatype: "json",
      success: function (data) {
        for (var i = 0; i < data.length; i++) { //(!)
          var name = data[i].name;
          var kor = data[i].kor;
          var eng = data[i].eng;
          var math = data[i].math;
          var total = Number(kor) + Number(eng) + Number(math);
          var avg = (total / 3).toFixed(2);
          d_data += `<tr id = ${count}>`
          d_data += `<td>${count}</td>`
          d_data += `<td>${name}</td>`
          d_data += `<td>${kor}</td>`
          d_data += `<td>${eng}</td>`
          d_data += `<td>${math}</td>`
          d_data += `<td>${total}</td>`
          d_data += `<td>${avg}</td>`
          d_data += `<td><button class="updateBtn">수정</button> <button class="delBtn">삭제</button></td>`
          d_data += `</tr>`
          count++;
        }//for
        $("tbody").html(d_data); //(!)
        d_data = ""
      },//success
      error: function () {
        alert("실패");
        return false;
      }//error
    });//ajax
  });//데이터 가져오기 버튼


  //삭제버튼
  $(document).on("click", ".delBtn", function () {
    var d_num = $(this).closest("tr").attr("id");
    if (confirm(d_num + "번 학생을 삭제하시겠습니까?")) {
      $("#" + d_num).remove();
      alert(d_num + "번 학생을 삭제하셨습니다.");
    } else { alert("삭제를 취소하셨습니다."); }
  });//삭제버튼

  //입력 버튼
  $(document).on("click", "#create", function () {
    alert("버튼 클릭");
    var name = $("#name").val();
    var kor = $("#kor").val();
    var eng = $("#eng").val();
    var math = $("#math").val();
    var total = Number(kor) + Number(eng) + Number(math);
    var avg = (total / 3).toFixed(2);
    if (name.length < 1 || name.kor < 1 || name.eng < 1 || name.math < 1) {
      alert("데이터를 입력하셔야합니다.")
    } else {
      d_data += `<tr id = ${count}>`
      d_data += `<td>${count}</td>`
      d_data += `<td>${name}</td>`
      d_data += `<td>${kor}</td>`
      d_data += `<td>${eng}</td>`
      d_data += `<td>${math}</td>`
      d_data += `<td>${total}</td>`
      d_data += `<td>${avg}</td>`
      d_data += `<td><button class="updateBtn">수정</button> <button class="delBtn">삭제</button></td>`
      d_data += `</tr>`
      count++;
      $("tbody").prepend(d_data);


      alert("학생이 추가되었습니다.");
      d_data = "";
      name = "";
      kor = "";
      eng = "";
      math = "";
    }//if문
  })//입력버튼

  //수정버튼
  $(document).on("click", ".updateBtn", function () {
    $("#create, #update, #updateCancel").toggle();
    $("#name").val($(this).closest("tr").children(`td:eq(${1})`).text());//(!)
    $("#kor").val($(this).closest("tr").children(`td:eq(${2})`).text());
    $("#eng").val($(this).closest("tr").children(`td:eq(${3})`).text());
    $("#math").val($(this).closest("tr").children(`td:eq(${4})`).text());
  });//수정버튼
  //수정취소버튼
  $(document).on("click", "#updateCancel", function () {
    alert("수정이 취소되었습니다.");
    $("#create, #update, #updateCancel").toggle();
    
  });//수정취소버튼
  //수정완료버튼
  $(document).on("click", "#update", function () {
    alert("수정하였습니다.")
    var name_up = $("#name").val();
    var kor_up = Number($("#kor").val());
    var eng_up = Number($("#eng").val());
    var math_up = Number($("#math").val());
   
    if (name_up.length < 1 || kor_up.length < 1 || eng_up.length < 1 || math_up.legnth < 1) {
      alert("데이터를 입력하셔야합니다.")
    }
    else {
      alert("성공");
    };
    //   d_data += `<tr id = ${count}>`
    //   d_data += `<td>${count}</td>`
    //   d_data += `<td>${name}</td>`
    //   d_data += `<td>${kor}</td>`
    //   d_data += `<td>${eng}</td>`
    //   d_data += `<td>${math}</td>`
    //   d_data += `<td>${total}</td>`
    //   d_data += `<td>${avg}</td>`
    //   d_data += `<td><button class="updateBtn">수정</button> <button class="delBtn">삭제</button></td>`
    //   d_data += `</tr>`
    //   count++;
    //   $("tbody").prepend(d_data);


    //   alert("학생이 추가되었습니다.");
    //   d_data = "";
    //   name = "";
    //   kor = "";
    //   eng = "";
    //   math = "";

    
  });//수정완료버튼


});//제이쿼리