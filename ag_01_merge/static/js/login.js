// $('#signup').click(function() {
//   $('.pinkbox').css('transform', 'translateX(80%)');
//   $('.signin').addClass('nodisplay');
//   $('.signup').removeClass('nodisplay');
// });

// $('#signin').click(function() {
//   $('.pinkbox').css('transform', 'translateX(0%)');
//   $('.signup').addClass('nodisplay');
//   $('.signin').removeClass('nodisplay');
// });

// // 로그인버튼
// $(function(){
//   const csrfToken = $("meta[name='csrf-token']").attr("content");
//   $("#sBtn").click(function(){
//     alert("클릭됨");
//     id = $("#id").val();
//     pw = $("#pw").val();

//     $.ajax({
//       headers : {"X-CSRFToken":csrfToken},
//       url : "/member/loginChk/",
//       type : "post",
//       data : {"id":id, "pw":pw},

//       success : function(data){
//         if(data.result == "success"){
//           console.log("아이디 : " + id + " / 패스워드 : " + pw);
//           alert("로그인되었습니다.");
//           location.href = "/";
//         }else{
//           alert("아이디 또는 패스워드가 일치하지 않습니다.");
//         }
//       },
//       error : function(){
//         alert("실패");
//       }
//     }); // ajax
//   }); // .button(로그인버튼)
// }); // jquery