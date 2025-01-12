$(document).ready(function(){


	$(".nav_mypage").click(function(){

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

	}) // 미로그인 마이페이지 클릭
}) // jquery

