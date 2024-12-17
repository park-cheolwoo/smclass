$(document).ready(function(){
  const csrfToken = $("meta[name='csrf-token']").attr("content"); // csrfToken을 가져옵니다.


  // 인기글 포인트 지급 임시 버튼 클릭 시 
  $('#reward_points_button').on('click',function(event){


     // 출석체크 Ajax 요청
    $.ajax({ 
      headers:{"X-CSRFToken":csrfToken},
      url:"/board/execute_reward_points/",
      type:"post",
      data:{
        
      },
      success:function(response){
        console.log("response: "+response);
        if(response.success){
          alert("포인트 지급 완료");
        }else{
          alert("오류 발생");
        }
      },
      error:function(){
        alert("에러 발생.");
      }
    }); //ajax */
  }) // 버튼 클릭
}) // jquery