 // 1. 사이트 GPS 출력
 $(function() {
  const radius = 6371; // 지구 반지름 (단위: km)

  // 두 지점 간의 거리 계산 함수 (Haversine 공식)
  function getDistance(lat1, lon1, lat2, lon2) {
      const toRad = (value) => (value * Math.PI) / 180;
      const dLat = toRad(lat2 - lat1);
      const dLon = toRad(lon2 - lon1);
      const a = Math.sin(dLat / 2) ** 2 +
                Math.cos(toRad(lat1)) * Math.cos(toRad(lat2)) * 
                Math.sin(dLon / 2) ** 2;
      const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
      return radius * c; // 단위: km
  }

  // Geolocation API로 현재 위치를 가져옴
  if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(function(pos) {
          const userLat = pos.coords.latitude;
          const userLon = pos.coords.longitude;

          $('#latitude').html(userLat); // 위도
          $('#longitude').html(userLon); // 경도

          // CSV 파일 읽기
          $.ajax({
              url: '/static/좌표데이터.csv', // static 폴더에 있는 파일
              dataType: 'text',
              success: function(data) {
                  processCSVData(data, userLat, userLon);
              },
              error: function() {
                  alert('CSV 파일을 읽는 데 실패했습니다.');
              }
          });
      });
  } else {
      alert("이 브라우저에서는 Geolocation이 지원되지 않습니다.");
  }

  // CSV 데이터를 처리하는 함수
  function processCSVData(data, userLat, userLon) {
      const lines = data.split("\n"); // 줄 단위로 나눔
      let nearestLocation = null; // 가장 가까운 위치
      let minDistance = Infinity; // 최소 거리

      for (let i = 1; i < lines.length; i++) { // 첫 번째 줄은 헤더
          const line = lines[i].trim();
          if (line) {
              const columns = line.split(",");
              const 시도 = columns[0];
              const 시군구 = columns[1];
              const 위도 = parseFloat(columns[4]);
              const 경도 = parseFloat(columns[5]);

              // 사용자 위치와의 거리 계산
              const distance = getDistance(userLat, userLon, 위도, 경도);
              if (distance < minDistance) {
                  minDistance = distance;
                  nearestLocation = `${시도} ${시군구}`;
              }
          }
      }
  }
});// 1번 끝

// 2. 글쓰기 유효성 검사
if ("{{umsg}}" != ""){
alert("게시글이 수정되었습니다.")
location.href="/board/bbview/{{umsg}}";
}

$(function(){
$('.write').click(function(){
    if($('#btitle').val().length<2){
        alert('게시글 제목은 두 자리 이상 입력해야 합니다.');
        $('#btitle').focus()
        return false();
    }
    if($('#summernote').val().length<2){
        alert('게시글 내용은 두 자리 이상 입력해야 합니다.');
        $('#summernote').focus()
        return false();
    }
    if($('#bgps').val().length<2){
        alert('위치를 입력해야 게시글 작성이 가능합니다.');
        $('#bgps').focus()
        return false();
    }
    modifyFrm.submit();
});
});// 2번 끝


// 3. 썸머노트 삽입
$(function(){

$('#summernote').summernote({
  focus:true,  width:"100%",
  minHeight: 400,           // 에디터 최소 높이
  maxHeight: 500,          // 에디터 최대 높이
  lang : 'ko-KR',
  placeholder: '글자를 입력하시면 됩니다.' ,
  disableResizeEditor: true,
  //  추가 부분
  toolbar: [
  // [groupName, [list of button]]
  ['fontname', ['fontname']],
  ['fontsize', ['fontsize']],
  ['style', ['bold', 'italic', 'underline','strikethrough', 'clear']],
  ['color', ['forecolor','color']],
  ['table', ['table']],
  ['para', ['ul', 'ol', 'paragraph']],
  ['height', ['height']],
  ['insert',['picture','link','video']],
  ['view', ['fullscreen', 'help']]
  ],
fontNames: ['Arial', 'Arial Black', 'Comic Sans MS', 'Courier New','맑은 고딕','궁서','굴림체','굴림','돋움체','바탕체'],
fontSizes: ['8','9','10','11','12','14','16','18','20','22','24','28','30','36','50','72'],
//이미지 업로드 시 width 적용
callbacks: {
  onImageUpload: function(image) {
    console.log('in');
    const file = image[0];
    const reader = new FileReader();
    reader.onloadend = function() {
      const image = $('<img>').attr('src',  reader.result);
      image.attr('width','100 %');
      $('#summernote').summernote("insertNode", image[0]);
    }
        reader.readAsDataURL(file);
    }
  }
});
}); // 3번 끝