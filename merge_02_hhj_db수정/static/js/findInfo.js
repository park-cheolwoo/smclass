$(document).ready(function() {
  const csrfToken = $("meta[name='csrf-token']").attr("content");

  let signin = $(".links").find("li").find("#signin"); // 아이디 찾기
  let signup = $(".links").find("li").find("#signup"); // 비밀번호 찾기
  let loginPage = $(".links").find("li").find("#loginPage"); // 로그인페이지로 이동하는 그 부분

  let first_input = $("form").find(".first-input"); // 이름 텍스트박스
  let hidden_input = $("form").find(".input__block").find("#repeat__password"); // 인증번호 입력값
  let hidden_result = $("form").find(".hiddenResult");

  let sendEmailBtn = $("form").find(".sendEmailBtn"); // 인증번호 전송 버튼
  let resendEmail = $("form").find(".resendEmail"); // 인증번호 재전송 버튼
  let find_btn = $("form").find(".find_btn"); // 핑크버튼

  let verificationCode = ''; // 랜덤 인증번호 저장 변수

  // 초기설정 : 재전송 버튼 숨기기
  resendEmail.css("display", "none");

  //----------- 비밀번호 찾기 화면 ---------------------
  signup.on("click", function(e) {
    e.preventDefault();  // 페이지 새로고침 방지

    // 비밀번호 찾기 화면으로 변경
    $(this).parent().css("opacity", "1");
    $(this).parent().siblings().css("opacity", ".6");
    $("#id_find").css("display","none"); // 아이디 찾기 버튼 숨기기
    $("#pw_find").css("display","block"); // 비밀번호 찾기 버튼 나타내기

    // 이름 텍스트박스를 비밀번호 찾기 화면에 맞게 변환
    first_input.removeClass("first-input__block").addClass("signup-input__block");

    // 인증번호 입력 부분 보이기
    hidden_input.css({
        "opacity": "1",  // 인증번호 입력부분 나타내기
        "display": "block"
    });

    // 인증번호 전송 버튼 보이기
    sendEmailBtn.css("display", "inline-block");

    // 아이디/패스워드 알려주는 칸 숨기기
    hidden_result.css({
      "opacity": "0",  
      "display": "none"
    });

    // 버튼 텍스트를 "비밀번호 찾기"로 변경
    //find_btn.text("비밀번호 찾기");

    // ------- <인증번호 전송> 버튼 클릭 시 랜덤 숫자 전송 -------
    sendEmailBtn.on("click", function() {
      const name = $("#name").val(); // 입력된 이름 가져오기
      const email = $("#email").val(); // 입력된 이메일 주소 가져오기

      // 입력값 유효성 검사
      if ((!name) && (!email)) {
        alert("이름과 이메일을 입력하세요.");
        $("#name").focus();
        return;
      } else if (!name) {
        alert("이름을 입력하세요.");
        $("#name").focus();
        return;
      } else if (!email) {
        alert("이메일 주소를 입력하세요.");
        $("#email").focus();
        return;
      }

      // 랜덤 6자리 숫자 생성
      verificationCode = Math.floor(100000 + Math.random() * 900000);  // 6자리 랜덤 숫자

      // 이메일로 랜덤 숫자 전송 (여기선 AJAX로 서버에 요청한다고 가정)
      $.ajax({
        url: '/member/send_verification_code/', // 서버에서 처리할 URL
        type: 'POST',
        headers : {"X-CSRFToken" : csrfToken},
        data: {
          name: name,
          email: email,
          verification_code: verificationCode
        },
        success: function(response) {
          if (response.result == 'success') {
            alert("인증번호가 전송되었습니다.");
          } else {
            alert("전송 실패. " + response.message);
          }
        },
        error: function() {
          alert("서버 오류. 다시 시도해주세요.");
        }
      }); // ajax

      // 인증번호 전송 버튼 숨기기
      $("#sendEmail").css("display", "none");

      // 인증번호 재전송 버튼 나타내기



    }); // sendEmailBtn 인증번호 전송 버튼

    // ----- <인증번호 확인> 버튼 이부분수정!!!!!!!!!!!!!! 이거 바꿀 거임 새 버튼 만들어서
    $("#pw_find").on("click", function() {
      const enteredCode = $("#repeat__password").val(); // 사용자가 입력한 인증번호
      
      $.ajax({
        url: '/member/verify_code/',  // 인증번호 확인을 위한 URL
        type: 'POST',
        headers : {"X-CSRFToken" : csrfToken},
        data: {
          verification_code: enteredCode
        },
        success: function(response) {
          if (response.result === 'success') {
            alert("인증번호가 일치합니다.");

          } else {
            alert("인증번호가 일치하지 않습니다. 다시 시도해주세요.");
          }
        },
        error: function() {
          alert("서버 오류. 다시 시도해주세요.");
        }
      }); //ajax
    });  // <인증번호 확인> 버튼

    // 비밀번호 찾기 클릭 시
    $("#pw_find").click(function(){
      alert("비밀번호 찾기 클릭");  
      name = $("#name").val(); // 사용자가 입력한 인증번호
      email = $("#email").val(); // 사용자가 입력한 이메일

      if((!name) && (!email)){
        alert("이름과 이메일 주소를 입력하세요.");
        $("#name").focus();
        return;
      }else if(!name){
        alert("이름을 입력하세요.");
        $("#name").focus();
        return;
      }else if(!email){
        alert("이메일 주소를 입력하세요.");
        $("#email").focus();
        return;
      }

      $.ajax({
        url: '/member/findId/',  // 아이디 패스워드 확인해야 함 url추가하고
        type: 'POST',
        headers : {"X-CSRFToken" : csrfToken},
        data: {
          "name" : name,
          "email" : email 
        },
        success: function(data) { // 입력한 이메일과 이름이 맞을때
          if(data.result == 'success') {
            alert("회원정보가 확인되었습니다.");
          } else {
            alert("존재하지 않는 회원입니다.");
          }
        },
        error: function() {
          alert("에러");
        }
      }); // ajax
    }); // 비밀번호 찾기 클릭
  }); //  비밀번호 찾기 화면

  //----------- 아이디 찾기 화면 ---------------------
  signin.on("click", function(e) {
    e.preventDefault();  // 페이지 새로고침 방지
    
    $("#id_find").css("display","block"); // 아이디 찾기 버튼 나타내기
    $("#pw_find").css("display","none"); // 비밀번호 찾기 버튼 숨기기

    // 아이디 찾기 화면으로 변경
    $(this).parent().parent().siblings("h1").text("아이디 찾기");
    $(this).parent().css("opacity", "1");
    $(this).parent().siblings().css("opacity", ".6");

    // 이름 텍스트박스를 아이디 찾기 화면에 맞게 변환
    first_input.addClass("first-input__block").removeClass("signup-input__block");

    // 아이디 결과 부분 숨기기
    hidden_result.css({
      "opacity": "0",  
      "display": "none"
    });
    // 인증번호 입력 부분 숨기기
    hidden_input.css({
      "opacity": "0",  
      "display": "none"
    });

    // 인증번호 전송 버튼 숨기기
    sendEmailBtn.css("display", "none");
    resendEmail.css("display", "none");

    // 버튼 텍스트를 "아이디 찾기"로 변경
    //find_btn.text("아이디 찾기");
  
  }); // 아이디 찾기 화면

  // 로그인 누르면 로그인화면으로 이동
  loginPage.on("click", function() {
    location.href = "/member/login/";
  });      
}); // ready

// -------------------------- 여기서부터 뭐이것저것처리 --------------------------
let idBtnHidden = false; // 버튼 숨김 상태 관리
$(function(){
  const csrfToken = $("meta[name='csrf-token']").attr("content");

  // 아이디 찾기 버튼 클릭 시
  $("#id_find").on("click", function(e){
    e.preventDefault(); // 기본 동작 방지
    alert("아이디 찾기 클릭");

    const name = $("#name").val(); // 사용자가 입력한 인증번호
    const email = $("#email").val(); // 사용자가 입력한 이메일

    if((!name) && (!email)){
      alert("이름과 이메일 주소를 입력하세요.");
      $("#name").focus();
      return;
    } else if(!name){
      alert("이름을 입력하세요.");
      $("#name").focus();
      return;
    } else if(!email){
      alert("이메일 주소를 입력하세요.");
      $("#email").focus();
      return;
    }

    $.ajax({
      url: '/member/findId/',  // 아이디 패스워드 확인해야 함 url추가하고
      type: 'POST',
      headers : {"X-CSRFToken" : csrfToken},
      data: {
        "name" : name,
        "email" : email 
      },
      success: function(response) {
        // 서버 응답 처리
        if (response.result == "success") {
          alert("회원정보가 확인되었습니다.");
          
          // 텍스트박스, 버튼 숨기기
          $("#name").parent().hide();
          $("#email").parent().hide();
          $("#id_find").css("display", "none");
          /*$("#name").css("display","none"); 
          $("#email").css("display","none"); 
          $("#id_find").css("display","none"); */
          
          // 화면에 메시지 표시
          const message = `<div style="width: 90%; max-width: 680px; height: 150px; margin: 0 auto; border-radius: 8px; border: none; background: rgba(15, 19, 42, 0.1); color: #333; padding: 0 0 0 15px; font-size: 1.2em; text-align: center; margin-top: 20px;">
          <h2 style="padding-top: 55px;">${response.name}님의 아이디는 <strong>${response.user_id}</strong>입니다.</h2>
          </div>`;
          

          $("#result_message").html(message);
          $("#result_message").css("display", "block");

        } else if (response.result == "fail") {
          alert(response.message); // 서버에서 보낸 오류 메시지
          $("#name").val("");
          $("#email").val("");
          $("#name").focus();
        }
      },
      error: function(xhr, status, error) {
        alert("서버 오류");
      }
    }); // ajax
  }); // 아이디 찾기 버튼 클릭 시
  
  // '아이디 찾기 화면'으로 전환
  $("#signin").on("click", function (e) {
    e.preventDefault();
    $("#id_find").css("display", idBtnHidden ? "none" : "block"); // 버튼 상태 유지
    $("#pw_find").css("display", "none");
    $("#result_message").css("display", idBtnHidden ? "block" : "none"); // 메시지 상태 유지
    $("#name").parent().show();
    $("#email").parent().show();
    $("#name").val("");
    $("#email").val("");
  });

  // '비밀번호 찾기 화면'으로 전환
  $("#signup").on("click", function (e) {
    e.preventDefault();
    $("#id_find").css("display", "none");
    $("#pw_find").css("display", "block");
    $("#result_message").css("display", "none"); // 메시지 숨기기
    $("#name").parent().show();
    $("#email").parent().show();
    $("#name").val("");
    $("#email").val("");
  });

}); // jquery
