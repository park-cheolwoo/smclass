$(function(){
	
	$(window).resize(function(){ 

		var winWidth = $(window).width();

		gnbcheck();
		if (winWidth > 767){$("#mnaviOpen").css("display","none")}else{$("#mnaviOpen").css("display","block")}
		$("#mnaviClose").css("display","none");

	});
	
	
	$("#mnaviOpen").click(function(){
		$("#gnb").show("fast");
		$("#mnaviClose").css("display","block");
		$(this).css("display","block");
	});

	$("#mnaviClose").click(function(){
		$("#gnb").hide("fast");
		$("#mnaviOpen").css("display","block");
		$(this).css("display","none");
	});

	function gnbcheck(){
		var winWidth = $(window).width();
		if(winWidth < 767){
			$("#gnb").css("display","none");
		}else{
			$("#gnb").css("display","block");
		}
	}

	gnbcheck();
	
});

$(function(){	
	$('#search-form').submit(function(e){
					if($('.search-txt').val().length < 1){
									e.preventDefault(); // 폼 제출을 막습니다
									alert('검색창에 검색어를 입력하세요.');
									$('.search-txt').focus();
					}
	});
});
document.addEventListener("DOMContentLoaded", () => {
	const hashtags = document.querySelectorAll(".hashtag");

	hashtags.forEach((tag) => {
					tag.addEventListener("click", function (e) {
									e.preventDefault(); // 기본 링크 동작 방지

									const keyword = this.getAttribute("data-keyword"); // data-keyword 가져오기
									document.getElementById("hidden-search-keyword").value = keyword; // 숨겨진 input에 값 설정

									document.getElementById("redirect-form").submit(); // 폼 제출
					});
	});
});