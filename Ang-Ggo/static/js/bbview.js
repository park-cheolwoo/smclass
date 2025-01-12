 // 1. 모달창 위치정보 수집 동의
 let userLat = null;
 let userLon = null;
 let nearestLocation = null;
 let nearestLocation_s = null;

 // 위치 정보를 업데이트하는 함수
 function updateLocation(lat, lon) {
   userLat = lat;
   userLon = lon;

   // 위치 데이터를 sessionStorage에 저장
   sessionStorage.setItem("userLat", lat);
   sessionStorage.setItem("userLon", lon);

   // CSV 데이터와 비교하여 가장 가까운 위치 업데이트
   $.ajax({
     url: '/static/좌표데이터.csv',
     dataType: 'text',
     success: function (data) {
       processCSVData(data, lat, lon);
     },
     error: function () {
       alert('CSV 파일을 읽는 데 실패했습니다.');
     },
   });
 }

 // 가장 가까운 위치를 찾고 DOM 업데이트
 function processCSVData(data, lat, lon) {
   const lines = data.split("\n");
   let minDistance = Infinity;

   for (let i = 1; i < lines.length; i++) {
     const line = lines[i].trim();
     if (line) {
       const columns = line.split(",");
       const 시도 = columns[0];
       const 시군구 = columns[1];
       const 위도 = parseFloat(columns[4]);
       const 경도 = parseFloat(columns[5]);

       const distance = getDistance(lat, lon, 위도, 경도);
       if (distance < minDistance) {
         minDistance = distance;
         nearestLocation = `${시도} ${시군구}`;
         nearestLocation_s = `${시군구}`;
       }
     }
   }

   // DOM 업데이트
   if (nearestLocation) $("#gps").html(`<h2>${nearestLocation}</h2>`);
   if (nearestLocation_s) $("#gps_s").html(`<h2>${nearestLocation_s} <i class="fa-solid fa-location-dot"></i></h2>`);

   // 위치 데이터를 sessionStorage에 저장
   sessionStorage.setItem("nearestLocation", nearestLocation);
   sessionStorage.setItem("nearestLocation_s", nearestLocation_s);
 }

 // Haversine 공식으로 거리 계산
 function getDistance(lat1, lon1, lat2, lon2) {
   const radius = 6371; // 지구 반지름 (km)
   const toRad = (value) => (value * Math.PI) / 180;
   const dLat = toRad(lat2 - lat1);
   const dLon = toRad(lon2 - lon1);
   const a =
     Math.sin(dLat / 2) ** 2 +
     Math.cos(toRad(lat1)) * Math.cos(toRad(lat2)) * Math.sin(dLon / 2) ** 2;
   const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
   return radius * c;
 }

 // 위치 권한 요청 및 업데이트
 function requestLocationPermission() {
   if (navigator.geolocation) {
     navigator.geolocation.getCurrentPosition(
       (position) => {
         const lat = position.coords.latitude;
         const lon = position.coords.longitude;
         updateLocation(lat, lon);
         alert("위치 권한이 허용되었습니다.");
       },
       (error) => {
         switch (error.code) {
           case error.PERMISSION_DENIED:
             alert("위치 권한이 거부되었습니다.");
             break;
           case error.POSITION_UNAVAILABLE:
             alert("위치 정보를 사용할 수 없습니다.");
             break;
           case error.TIMEOUT:
             alert("위치 요청이 시간 초과되었습니다.");
             break;
           default:
             alert("알 수 없는 오류가 발생했습니다.");
         }
       }
     );
   } else {
     alert("이 브라우저는 위치 서비스를 지원하지 않습니다.");
   }
 }

 // 페이지 로드 시 sessionStorage에서 데이터 복원
 $(document).ready(() => {
   const storedLat = sessionStorage.getItem("userLat");
   const storedLon = sessionStorage.getItem("userLon");
   const storedNearestLocation = sessionStorage.getItem("nearestLocation");
   const storedNearestLocation_s = sessionStorage.getItem("nearestLocation_s");

   if (storedLat && storedLon) {
     userLat = parseFloat(storedLat);
     userLon = parseFloat(storedLon);
     nearestLocation = storedNearestLocation;
     nearestLocation_s = storedNearestLocation_s;

     // DOM 복원
     if (nearestLocation) $("#gps").html(`<h2>${nearestLocation}</h2>`);
     if (nearestLocation_s) $("#gps_s").html(`<h2>${nearestLocation_s} <i class="fa-solid fa-location-dot"></i></h2>`);
   }
 });// 1번 끝


// 2. 좋아요 기능
$(function(){
 $("#likeBtn").click(function(){
   const csrfToken = $("meta[name='csrf_token']").attr("content");
   let bno = "{{board.bno}}"
   $.ajax({
     headers:{"X-CSRFToken":csrfToken},
     url:"/board/likes/",
     type:"post",
     data:{"bno":bno},
     success:function(data){
       console.log("결과 data.result : "+data.result)
       if(data.result == "remove"){
         $("#likecount").text(data.count)
         $("#liketxt").html('<i class="fa-regular fa-thumbs-up"></i>')
         console.log(data.count)
       }else{
         $("#likecount").text(data.count)
         $("#liketxt").html('<i class="fa-solid fa-thumbs-up"></i>')
         console.log(data.count)
       }
     },
     error:function(){
       alert("실패")
     }
   })//ajax
 });
});// 2번 끝

// 3. 댓글등록(입력)
$(document).on("click", ".replyBtn", function () {
 if($('.replyType').val().length<2){
   alert('댓글은 두 자리 이상 입력해야 합니다.');
   $('.replyType').focus()
   return false();
 }
 const ccontent = $(".replyType").val();
 const bno = "{{ board.bno }}";
 const csrfToken = $("meta[name='csrf_token']").attr("content");

 $.ajax({
   headers: { "X-CSRFToken": csrfToken },
   url: "/comment/cwrite/",
   type: "post",
   data: { ccontent: ccontent, bno: bno },
   success: function (data) {
     if (data.result === "success") {
       alert("하단댓글이 등록되었습니다.");
       
       var datahtml = ""
         datahtml += `<ul id="${data.comment[0].cno}">`
         datahtml += `<li class="name">{{request.session.session_nickname}}<span>[ ${data.comment[0].cdate} ]</span></li>`
         datahtml += `<li class="txt">${data.comment[0].ccontent}</li>`
         datahtml += `<li class="btn">`
         datahtml += `<a class="uBtn rebtn">수정</a>&nbsp`
         datahtml += `<a class="dBtn rebtn">삭제</a>`
         datahtml += `</li>`
         datahtml += `</ul>`
         console.log(datahtml)
         $(".comments-list").prepend(datahtml)
         let cnt = $("#cnt").text()
         console.log("개수 : "+(Number(cnt)+1))
         $("#cnt").text(Number(cnt)+1)
         location.reload();
     } else {
       alert("등록이 되지 않았습니다. 다시 입력하세요.");
     }
   },
   error: function () {
     alert("실패");
   },
 });

 $(".replyType").val("");
});// 3번 끝

// 4. 댓글삭제 - 동적클릭진행
$(document).on("click",".dBtn",function(){
const csrfToken = $("meta[name='csrf_token']").attr("content");
let cno = $(this).closest("ul").attr("id");
if (confirm(cno + "번 댓글을 삭제하시겠습니까?")){
 //ajax
 $.ajax({
   headers:{"X-CSRFToken":csrfToken},
   url:"/comment/cdelete/",
   type:"post",
   data:{"cno":cno},
   success:function(data){
     console.log("결과 data.result : "+data.result)

     if (data.result == "success"){
       alert(cno + "번 댓글이 삭제되었습니다.")
       $("#"+cno).remove()
       //전체개수 -1감소
       let cnt = $("#cnt").text()
       console.log("개수 : "+(Number(cnt)-1))
       $("#cnt").text(Number(cnt)-1)
     }
   },
   error:function(){
     alert("실패")
   }
 })//ajax
}//confirm
});// 4번 끝

// 5. 댓글수정
$(document).on("click",'.uBtn',function(){
let cno = $(this).closest("ul").attr("id");
let id = "{{request.session.session_nickname}}";
let cdate = $(this).closest("ul").find(".name span").text();
let ccontent = $(this).closest("ul").find(".txt").text();

var datahtml = ""
 datahtml += `<li class="name">${id}<span>&nbsp;${cdate}&nbsp;</span></li>`
 datahtml += `<li class="btn">`
 datahtml += `<a class="sBtn rebtn">완료</a>&nbsp`
 datahtml += `<a class="cBtn rebtn">취소</a>`
 datahtml += `</li>`
 datahtml += `<li class="txt"><textarea class="replyType" style="width: 1000px; height: 200px; font-size: 20px; margin-top: 10px;">${ccontent}</textarea></li>`
$("#"+cno).html(datahtml);
});// 5번 끝

// 6. 댓글수정(취소)
$(document).on("click",'.cBtn',function(){
location.reload();
});// 6번 끝

// 7. 댓글수정(저장)
$(document).on("click",'.sBtn',function(){
let cno = $(this).closest("ul").attr("id");
let ccontent = $(this).closest("ul").find(".txt textarea").val();
const csrfToken = $("meta[name='csrf_token']").attr("content");
//ajax
$.ajax({
 headers:{"X-CSRFToken":csrfToken},
 url:"/comment/cupdate/",
 type:"post",
 data:{"cno":cno,"ccontent":ccontent},
 success:function(data){
   console.log("결과 data.result : "+data.result)
   console.log("결과 data.comment[0].cno : "+data.comment[0].cno)
   console.log("결과 data.comment[0].ccontent : "+data.comment[0].ccontent)

   if (data.result == "success"){
     alert("하단댓글이 수정되었습니다.")
     var datahtml = ""

     datahtml += `<li class="name">{{request.session.session_nickname}}<span>[ ${data.comment[0].cdate} ]</span></li>`
     datahtml += `<li class="btn">`
     datahtml += `<a class="uBtn rebtn">수정</a>&nbsp`
     datahtml += `<a class="dBtn rebtn">삭제</a>`
     datahtml += `</li>`
     datahtml += `<li class="txt">${data.comment[0].ccontent}</li>`
     $("#"+cno).html(datahtml);
     location.reload();
   }else{
     alert("등록이 되지 않았습니다. 다시 입력하세요.")
   }
 },
 error:function(){
   alert("실패")
 }
})//ajax
});//7번 끝

// 8. 대댓글 기능
$(document).on("click", ".rBtn", function () {
const parentCno = $(this).closest("ul").attr("id"); // 부모 댓글 ID
const bno = "{{ board.bno }}"; // 게시글 ID
const csrfToken = $("meta[name='csrf_token']").attr("content");

const replyBox = `
   <li class="txt">
     <textarea class="replyType" style="width: 100%; height: 100px;"></textarea>
     <button class="r_Btn rebtn">답글 등록</button>
     <button class="c_Btn rebtn">취소</button>
   </li>`;
$(this).closest("ul").append(replyBox);

$(document).on("click", ".r_Btn", function () {
   const ccontent = $(this).siblings(".replyType").val();
   if (ccontent.length < 2) {
       alert('답글은 두 글자 이상이어야 합니다.');
       return;
   }

   $.ajax({
       headers: { "X-CSRFToken": csrfToken },
       url: "/comment/reply/",
       type: "post",
       data: { cno: parentCno, bno: bno, ccontent: ccontent },
       success: function (data) {
           if (data.result === "success") {
               alert("답글이 등록되었습니다.");
               location.reload();
           } else {
               alert("답글 등록 실패. 다시 시도해주세요.");
           }
       },
       error: function () {
           alert("서버 요청 실패. 다시 시도해주세요.");
       }
   });
});

$(document).on("click", ".c_Btn", function () {
   $(this).closest(".txt").remove();
});
});
// 8번 끝