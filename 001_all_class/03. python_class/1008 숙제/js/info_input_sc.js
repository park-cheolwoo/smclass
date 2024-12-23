// 이메일 선택시 호출하는 함수
$(function () {
  $("#e_select").change(function () {
    $("#email2").val($("#e_select").val());
    a
  });

  // 생년월일 선택창을 호출하는 함수 
  let year = new Date().getFullYear();
  for (var i = year; i >= year - 80; i--) {
    $(y_select).append(`<option value="${i}">${i}</option>`)
  
    for (var i = 1; i <= 12; i++) {
      $(m_select).append(`<option value="${i}">${i}</option>`)
    }

    for (var i = 1; i <= 31; i++) {
      $(d_select).append(`<option value="${i}">${i}</option>`)
    }

    // 중복확인 버튼 함수

    // 우편번호 찾기 함수

    // 취소하기 함수
    $(document).on("click", "#clear", function () {
      if (confirm("작성하신 모든 내용을 지우시겠습니까?")) {
        $('form').each(function () {
          this.reset();
        });
      }
    });
  };

  // 가입하기 버튼
  $(document).on("click", "#submit", function () {

  // 공백을 확인하는 함수
      if ($("#user").val() == "") {
        alert("이름을 입력해주세요.")
        $("#user").focus()
        $("#user").css("background", "yellow")
        return false
      }
      else if ($("#id").val() == "") {
        alert("아이디를 입력해주세요.")
        $("#id").focus()
        $("#id").css("background", "yellow")
        return false
      }
      else if ($("#pw").val() == "") {
        alert("비밀번호를 입력해주세요.")
        $("#pw").focus()
        $("#pw").css("background", "yellow")
        return false
      }
      else if ($("#pw_check").val() == "") {
        alert("비밀번호 확인을 입력해주세요.")
        $("#pw_check").focus()
        $("#pw_check").css("background", "yellow")
        return false
      }
      else if ($("#email1").val() == "") {
        alert("이메일을 입력해주세요.")
        $("#email1").focus()
        $("#email1").css("background", "yellow")
        return false
      }
      else if ($("#email2").val() == "") {
        alert("이메일을 입력해주세요.")
        $("#email2").focus()
        $("#email2").css("background", "yellow")
        return false
      }
      else if ($("#f_postal").val() == "") {
        alert("주소를 입력해주세요.")
        $("#f_postal").focus()
        $("#f_postal").css("background", "yellow")
        return false
      }
      else if ($("#l_postal").val() == "") {
        alert("주소를 입력해주세요.")
        $("#f_postal").focus()
        $("#f_postal").css("background", "yellow")
        return false
      }
      else if ($("#address1").val() == "") {
        alert("주소를 입력해주세요.")
        $("#address1").focus()
        $("#address1").css("background", "yellow")
        return false
      }
      else if ($("#phone1").val() == "") {
        alert("휴대전화를 입력해주세요.")
        $("phone1").focus()
        $("#phone1").css("background", "yellow")
        return false
      }
      else if ($("#phone2").val() == "") {
        alert("휴대전화를 입력해주세요.")
        $("#phone2").focus()
        $("#phone2").css("background", "yellow")
        return false
      }
      else if ($("#phone3").val() == "") {
        alert("휴대전화를 입력해주세요.")
        $("#phone3").focus()
        $("#phone3").css("background", "yellow")
        return false
      }
      else { 
          alert("공백 유효성검사 통과")
    return true
  }
    });

  // 선택했는지 확인하는 함수(필수항목 라디오박스)
  $(document).on("click", "#submit", function () {
    if ($("#solar").is(":checked") == false || $("#lunar").is(":checked") == false) {
      alert("양력 또는 음력을 선택해야합니니다.")
      return false;
    } else if ($("#male").is(":checked") == false || $("#female").is(":checked") == false) {
      alert("남성 또는 여성을 선택해야합니니다.")
      return false;
    } else if ($("#n_yes").is(":checked") == false || $("#n_no").is(":checked") == false) {
      alert("뉴스레터 수신여부를 선택해야합니니다.")
      return false;
    } else if ($("#s_yes").is(":checked") == false || $("#s_no").is(":checked") == false) {
      alert("SMS 수신여부를 선택해야합니니다.")
      return false;
    } else {
      alert("선택 유효성검사 통과")
      return true;
    }
  });

  // 전화번호 패턴 확인하는 함수
  $(document).on("click", "#submit", function () {
    let phone_pattern = /^[0-9]{3,4}$/;
    if (!(phone_pattern.test($("#phone1").val())) || !(phone_pattern.test($("#phone2").val())) || !(phone_pattern.test($("#phone3").val()))) {
      alert("휴대전화는 숫자 3~4자리만 입력 가능합니다. 다시 시도해주세요.")
      return false;
    } else {
      alert("휴대전화 유효성 통과")
      return true
    }
  });

  // 가입 조건(아이디/비밀번호) 확인하는 함수
  $(document).on("click", "#submit", function () {
    let name_pattern = /^[가-힣]{3-8}$/;
    let pw_pattern = /^(?=.*[0-9])(?=.*[a-zA-Z])(?=.*[!@#$%^&*]){,8}$/
    if (!(name_pattern.test($("#user").val()))) {
      alert("아이디 조건을 확인하고 다시 입력하세요.");
      return false;
    } else if (!(pw_pattern.test($("#pw1").val()))) {
      alert("비밀번호 조건을 확인하고 다시 입력하세요.");
      return false;
    } else if (!($("#pw1").val() == $("pw2").val())) {
      alert("비밀번호 확인이 비밀번호와 일치하지 않습니다.");
      return false;
    } else {
      alert("아이디 비밀번호 조건 일치")
      alert("가입을 환영합니다.")
      console.log("가입 성공")
      // $("#submit").submit();
    }
  });
}); // 제이쿼리 선언