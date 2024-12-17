$(document).ready(function() {
  const csrfToken = $("meta[name='csrf-token']").attr("content"); // csrfToken을 가져옵니다.
  // const aId = "{{request.session.session_id}}"; // 세션 ID를 확인함
  

  // 이달의 이벤트
  $(".eventThisMonth").click(function(event){
    console.log(".eventThisMonth");
    event.preventDefault();
    $('html,body').animate({scrollTop:$(this.hash).offset().top},
    500);
    
  }) // 이달의 이벤트로 위치 이동 버튼


  // ####### 페이지 상,하단 이동
  const scrollBtn = document.querySelector('.scrollBtn');
  const documentHeight = document.documentElement.scrollHeight;

    // up,down opacity 설정
  document.addEventListener('scroll', () => {
    if (documentHeight*0.15 < window.scrollY) {
      scrollBtn.style.opacity = 1;
    } else {
      scrollBtn.style.opacity = 0;

    }
  }) 

  $(".scrollUp").click(function(){
    window.scrollTo({
      top: 0,
      behavior: "smooth"
    })
  }); // upBtn
  $(".scrollDown").click(function(){
    window.scrollTo({
      top: documentHeight,
      behavior: "smooth"
    })
  }); // downBtn




  // ########### 1. 출석 체크 이벤트
  $(".btn_today_attend_chk").click(function(){
    var id = $(this).data("id");
    // alert("aId: " + aId)
    console.log("id: " + id);

    // 세션이 비어있으면 로그인 페이지로 리다이렉트
    // if(aId == "" || aId == "{{request.session.session_id}}"){
    if(id == ""){
      alert("로그인이 필요합니다.")
      location.href="/member/login/"
      return;
    }

    // 출석체크 Ajax 요청
    $.ajax({ 
      headers:{"X-CSRFToken":csrfToken},
      url:"/event/calendar/",
      type:"post",
      data:{
        "id":id,
      },
      success:function(data){
        console.log("data.result: "+data.result);
        if(data.result == "success"){
          alert("출석체크 완료");
          $(".chk_count_num").text(data.count); // 출석 횟수를 화면에 업데이트
          $(".chk_event_ticket_num").text(data.aTicket); // 응모권 개수를 화면에 업데이트
        }else if(data.result == "already_checked"){
          alert("이미 출석체크를 하셨습니다.");
        }else{
          alert("에러");
        }
      },
      error:function(){
        alert("에러 발생.");
      }
    }); //ajax */
  }); // 출석btn()


  // ############# 2. 응모권 차감
  $(document).on("click",".btn_apply_event_coupon",function(){
    // alert("테스트")
    var couponName = $(this).closest('.attend_event_coupon_bundle').find('.event_cpn_name').text().trim();
    var ticketDeduction = 0; // 차감할 응모권 수 
    var id = $(this).data("id");
    // alert("aId: " + aId)
    console.log("id: " + id);

    // 세션이 비어있으면 로그인 페이지로 리다이렉트
    if(id == ""){
      alert("로그인이 필요합니다.")
      location.href="/member/login/"
      return;
    }

    // num1 과 num2에 따른 차감 값 설정
    if ($(this).hasClass('num1')){
      ticketDeduction = 5; // num1 클릭 시 차감할 응모권 수
    }else if($(this).hasClass('num2')){
      ticketDeduction = 10; // num2 클릭 시 차감할 응모권 수 
    }

    // 확인 창 
    if(confirm(couponName+"을(를) 응모하시겠습니까?")){
      // alert("응모완료"); 
      console.log("ticketDeduction",ticketDeduction);

      // 응모하기 Ajax 요청
    $.ajax({ 
      headers:{"X-CSRFToken":csrfToken},
      url:"/event/apply/",
      type:"post",
      data: {
        "id":id,
        "ticketDeduction":ticketDeduction, // 차감할 응모권 수 전송
      },
      success:function(data){
        console.log("data.result: "+data.result);
        if(data.result == "success"){
          alert("쿠폰이 지급되었습니다.");
          $(".chk_event_ticket_num").text(data.aTicket); // 잔여 응모권 개수 화면에 띄워야함
          $("#useConditionCnt").text(data.usedTicket); // 사용한 응모권 개수도 화면에 띄워야함
        }else if(data.result == "not_yet"){
          alert("응모권의 개수가 모자랍니다.");
        }else{
          alert("에러");
        }
      },
      error:function(){
        alert("에러 발생.");
      }
    }); //ajax */
    } // if
  }) //응모권 버튼




  // ############# 3. 행운권 추첨

   // 랜덤 숫자
   function randomInt(min,max){
    var randonNum = Math.floor(Math.random()*(max-min+1)) + min;
    return randonNum;
  }
  
  // 럭키드로우
  function luckBtn(){
    alert
    var result = randomInt(1,100);
    console.log(result)
    if (result === 7 || result === 77 || result === 33) {
      alert("당첨")
    } else {
      alert("다음기회에")
    }
  }

  $(document).on("click","#btnMyLucky",function(){
    var ticketDeduction = 10; // 차감할 응모권 수 
    var id = $(this).data("id");
    // alert("aId: " + aId)
    console.log("id: " + id);

    // 세션이 비어있으면 로그인 페이지로 리다이렉트
    if(id == ""){
      alert("로그인이 필요합니다.")
      location.href="/member/login/"
      return;
    }

    // 확인 창 
    if(confirm("행운뽑기에 도전하시겠습니까?")){
      // alert("응모완료"); 
      console.log("ticketDeduction",ticketDeduction);


      // 행운뽑기 Ajax 요청
      $.ajax({ 
        headers:{"X-CSRFToken":csrfToken},
        url:"/event/luckyDraw/",
        type:"post",
        data:{
          "id":id,
          "ticketDeduction":ticketDeduction, // 차감할 응모권 수 전송
        },
        success:function(data){
          console.log("data.result: "+data.result);
          if(data.result == "success"){
            luckBtn()
            // alert("쿠폰이 지급되었습니다.");
            $(".chk_event_ticket_num").text(data.aTicket); // 잔여 응모권 개수 화면에 띄워야함
            $("#useConditionCnt").text(data.usedTicket); // 사용한 응모권 개수도 화면에 띄워야함
          }else if(data.result == "not_yet"){
            alert("응모권의 개수가 모자랍니다.");
          }else{
            alert("에러");
          }
        },
        error:function(){
          alert("에러 발생.");
        }

      }); //ajax */
    } // if 
  }) // 행운권 추첨 버튼



  


}); // jquery








// ################### 4. 이벤트 페이지 url 복사 
// 현재 url 변수로 가져오기
let nowUrl = window.location.href;
function copyUrl(){
  // alert("테스트")
  // nowUrl 변수에 담긴 주소
  navigator.clipboard.writeText(nowUrl).then(res=>{
    alert("주소가 복사되었습니다.");
  })
}


