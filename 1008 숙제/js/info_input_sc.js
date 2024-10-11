// 이메일 선택시 호출하는 함수
$(function () {
  $("#e_select").change(function () {
    $("#email2").val($("#e_select").val());
  });
});

// 생년월일 선택창을 호출하는 함수 
$(function () {
  let year = new Date().getFullYear();
  for (var i = year; i >= year - 80; i--) {
    $(y_select).append(`<option value="${i}">${i}</option>`)
  }
});
$(function () {
  for (var i = 1; i <= 12; i++) {
    $(m_select).append(`<option value="${i}">${i}</option>`)
  }
});
$(function () {
  for (var i = 1; i <= 31; i++) {
    $(d_select).append(`<option value="${i}">${i}</option>`)
  }
});

// 중복확인 버튼 함수
$(function () { 

})

// 우편번호 찾기 함수

// 취소하기 함수
$(function () {
  $("#clear").on("click", function () {
    if (confirm("작성하신 모든 내용을 지우시겠습니까?")) {
      $('form').each(function () {
        this.reset();
      });
    }
  });
});
// 가입하기 함수
let count = 0;
$(function () {
  $("#submit").on("click", function () {
