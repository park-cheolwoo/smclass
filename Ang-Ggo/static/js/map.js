var map;
    var InfoWindow,marker;
    var content,content1,content2,content3,rect;
    var url,lat,lon,name;
	var Clicklat,Clicklon;
	var result,resultDiv; 
    var centerlat,centerlon;
	var poiId,color;
	var poiId2,color2;
	var tData = new Tmapv2.extension.TData();
	let isSquareMapActive = false;
	let isAutoTrafficActive = false;
	let isMeasureDistanceActive = false; // 플래그 변수 추가
    let lastclicktime = 0;
    let lastclickx,lastclicky = 0;
    let currentDate = 0;
    var bFile1, bFile2, bFile3;
    var TimeAvg, rate_list, rate_count;
	 
     // 마커와 라벨을 저장할 배열 초기화
     var markerArr = [];
     var labelArr = [];

     var positions = [
    {
        title: '티맵모빌리티', 
        lonlat: new Tmapv2.LatLng(37.56520450, 126.98702028),
        keyword: '크리스마스'
    },
    {
        title: 'SKT타워', 
        lonlat: new Tmapv2.LatLng(37.566369,126.984895),
        keyword: '와인/바'
    },
    {
        title: '경찰서', 
        lonlat: new Tmapv2.LatLng(37.563709,126.989577),
        keyword: '비건식당'
    },
    {
        title: '호텔',
        lonlat: new Tmapv2.LatLng(37.565138,126.983655),
        keyword: '연말파티'
    },
    {
        title: '병원',
        lonlat: new Tmapv2.LatLng(37.565128,126.988830),
        keyword: '브런치'
    }
];
     function initTmap(){
        // map 생성
        // Tmap.map을 이용하여, 지도가 들어갈 div, 넓이, 높이를 설정합니다.
        map = new Tmapv2.Map("map_div", {
            center : new Tmapv2.LatLng(37.56520450, 126.98702028), // 지도 초기 좌표
            zoom : 16,
            width : "70%", // map의 width 설정
            height : "700px" // map의 height 설정   
        });
    
        map.addListener("click", onClick);


        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function (position) {
                var lat = position.coords.latitude;
                var lon = position.coords.longitude;
                centerlat = lat;
                centerlon = lon;
                console.log(lat, lon);
    
                // 마커 생성 시, icon 속성에 새로운 이미지 경로 설정
                marker = new Tmapv2.Marker({
                    position: new Tmapv2.LatLng(lat, lon),
                    map: map,
                    icon: "/static/images/markerStar.png",  // 마커 이미지 변경
                    iconSize: new Tmapv2.Size(24, 35) // 마커 이미지 크기 설정 (필요시 조정)
                });
    
                map.setCenter(new Tmapv2.LatLng(lat, lon));
                map.setZoom(16);

                updateMapCenter();
            });
        }

        // 지도 이동 이벤트 리스너 추가
        map.addListener("dragend", function() {
        updateMapCenter();
        });
    
        // 기본 상태로 measureDistance 실행
        measureDistance();
    }

    // 기본 정보
    function measureDistance() {
    resetActiveStates(); // 다른 기능 초기화
    isMeasureDistanceActive = true; // measureDistance 활성화

    $(".api_etc_btns > div#measureDistance").addClass("__color_blue_fill");
    $("#map_wrap").html('');
    }


    // 날씨 코드와 설명 매핑
const weatherDescriptions = {
    0: "맑음",
    1: "비",
    2: "비/눈",
    3: "눈",
    4: "소나기",
    5: "이슬비",
    6: "비와 눈 날림",
    7: "눈날림"
};

// 풍향 코드와 설명 매핑
function getWindDirection(degrees) {
    if (degrees >= 337.5 || degrees < 22.5) return "북풍";
    if (degrees >= 22.5 && degrees < 67.5) return "북동풍";
    if (degrees >= 67.5 && degrees < 112.5) return "동풍";
    if (degrees >= 112.5 && degrees < 157.5) return "남동풍";
    if (degrees >= 157.5 && degrees < 202.5) return "남풍";
    if (degrees >= 202.5 && degrees < 247.5) return "남서풍";
    if (degrees >= 247.5 && degrees < 292.5) return "서풍";
    if (degrees >= 292.5 && degrees < 337.5) return "북서풍";
    return ""; // 기본값
}

function updateMapCenter() {
    var center = map.getCenter();
    centerlat = center.lat();
    centerlon = center.lng();
    console.log("New center: ", centerlat, centerlon);

    readCSV('/static/기상청_격자위경도.csv', function(data) {
        let { nearestLocation_s2, locX, locY } = processCSVData(data, centerlat, centerlon);
        let { formattedDate, formattedTime } = findnow();

        lastclickx = locX; 
        lastclicky = locY;
        lastClickTime = currentDate;

        if (nearestLocation_s2) {
            const xhr = new XMLHttpRequest();
            const apiUrl = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst';
            const serviceKey = 'EPhM94JT5WuG2cnWrA7xBy4Ip1zeWGD%2Fc9StwgvLEua3LPV6Qgp9%2Bu%2Fq5hyyC9%2FtVA%2BL4WipZChsLpNs4obZ%2Bw%3D%3D';
            const queryParams = '?' + encodeURIComponent('serviceKey') + '=' + serviceKey +
                                '&' + encodeURIComponent('pageNo') + '=' + encodeURIComponent('1') +
                                '&' + encodeURIComponent('numOfRows') + '=' + encodeURIComponent('8') +
                                '&' + encodeURIComponent('dataType') + '=' + encodeURIComponent('Json') +
                                '&' + encodeURIComponent('base_date') + '=' + encodeURIComponent(formattedDate) +
                                '&' + encodeURIComponent('base_time') + '=' + encodeURIComponent(formattedTime) +
                                '&' + encodeURIComponent('nx') + '=' + encodeURIComponent(locX) +
                                '&' + encodeURIComponent('ny') + '=' + encodeURIComponent(locY);

            xhr.open('GET', apiUrl + queryParams);
            xhr.onreadystatechange = function() {
                if (this.readyState === 4) {
                    const { temperature, humidity, weather, wdDirection, wdStrength } = findSource(this.responseText);

                    const weatherDescription = weatherDescriptions[weather] || "알 수 없음";
                    const windDirection = getWindDirection(parseFloat(wdDirection));
                    const weatherIcon = `/static/images/weather${weather}.png`;

                    const weatherHTML = `
                        <div class="weather-container">
                            <div class="location">${nearestLocation_s2}</div>
                            <div class="weather-info">
                                <div class="temperature">${temperature}°</div>
                                <img src="${weatherIcon}" alt="${weatherDescription}" class="weather-icon">
                            </div>
                            </div>
                            <div class="details">
                                <div>습도 : ${humidity} %</div>
                                <div>풍향 : ${windDirection}</div>
                                <div>풍속 : ${wdStrength} m/s</div>
                            </div>
                        </div>`;
                    $(".how_we").html(weatherHTML);
                }
            };
            xhr.send('');
        }
    });
}

    
        // CSV 파일 읽기
        function readCSV(url, callback) {
            $.ajax({
                url: url,
                dataType: 'text',
                beforeSend: function(xhr) {
                    xhr.overrideMimeType('text/plain; charset=euc-kr');
                },
                success: function(data) {
                    callback(data);
                },
                error: function() {
                    alert('CSV 파일을 읽는 데 실패했습니다.');
                }
            });
        }
    
    
        // CSV 파일에서 위경도를 불러오는 함수
        function processCSVData(data, centerlat, centerlon) {
        let lines = data.split("\n");
        let minDistance = Infinity;
        let nearestLocation_s2 = '';
        let locX = 0, locY = 0;
    
        // 가장 가까운 위치 찾기
        lines.slice(1).forEach(line => {
            line = line.trim();
            if (line) {
                let [ , , 읍면동, 위도, 경도,x,y] = line.split(",");
                let distance = getDistance(centerlat, centerlon, parseFloat(위도), parseFloat(경도));
                if (distance < minDistance) {
                    minDistance = distance;
                    nearestLocation_s2 = 읍면동;
                    locX = x; // 가장 가까운 위치의 위도 저장
                    locY = y; // 가장 가까운 위치의 경도 저장
                }
            }
        });
        
        console.log(`가장 가까운 위치: ${nearestLocation_s2}, 위도: ${locX}, 경도: ${locY}`);
        return { nearestLocation_s2, locX, locY };
        }   
    
        // 거리를 계산하는 함수
        function getDistance(lat1, lon1, lat2, lon2) {
        const radius = 6371; // 지구 반지름 (km)
        let toRad = (value) => (value * Math.PI) / 180;
        let dLat = toRad(lat2 - lat1);
        let dLon = toRad(lon2 - lon1);
        let a = Math.sin(dLat / 2) ** 2 +
                Math.cos(toRad(lat1)) * Math.cos(toRad(lat2)) * Math.sin(dLon / 2) ** 2;
        let c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
        return radius * c;
        }
       
        //클릭 시점의 현재 시간을 호출하는 함수
        function findnow() {
        let currentDate = new Date();
        
        // 포맷된 날짜 (YYMMDD)
        let year = String(currentDate.getFullYear());
        let month = String(currentDate.getMonth() + 1).padStart(2, '0');
        let day = String(currentDate.getDate()).padStart(2, '0');
        let formattedDate = `${year}${month}${day}`;
    
        // 포맷된 시간 (HHMM)
        let hours = String(currentDate.getHours()).padStart(2, '0');
        let minutes = (Math.floor(currentDate.getMinutes() / 10) * 10) - 10;
        if (minutes < 0) {
            minutes = 50; // 만약 minutes이 0보다 작아지면, 50으로 설정 (한 시간 전 50분)
            hours = String(currentDate.getHours() - 1).padStart(2, '0'); // 한 시간 전
        }
        let formattedTime = `${hours}${String(minutes).padStart(2, '0')}`;
        
        console.log(formattedDate); // 예: 20241210
        console.log(formattedTime); // 예: 1930
        return { formattedDate, formattedTime };
    }
    
    
    
    
        // 기상청 API > JSON 데이터에서 필요한 정보 추출
        function findSource(responseText) {
            let data = JSON.parse(responseText);
            let items = data.response.body.items.item;
            if(!items){alert("기상청 데이터를 조회하는데 실패했습니다."); return false;}
    
            // 변수 선언 및 초기화
            let temperature = '';
            let humidity = '';
            let weather = '';
            let wdDirection = '';
            let wdStrength = '';
    
            items.forEach(item => {
                if (item.category === "PTY") {
                    weather = item.obsrValue;
                } else if (item.category === "REH") {
                    humidity = item.obsrValue;
                } else if (item.category === "T1H") {
                    temperature = item.obsrValue;
                } else if (item.category === "VEC") {
                    wdDirection = item.obsrValue;
                } else if (item.category === "WSD") {
                    wdStrength = item.obsrValue;
                }
            });
    
            return { temperature, humidity, weather, wdDirection, wdStrength };
        }

    // puzzle함수
    function onClick(e) {
        var Clicklon = e.latLng.lng();
        var Clicklat = e.latLng.lat();
       if (isSquareMapActive) {
       reverseLabel(Clicklon, Clicklat);} }
	
	function reverseLabel(Clicklon, Clicklat) {
			zoomLevel = map.getZoom();
			if (zoomLevel < 15) zoomLevel = 15;
	
			var headers = {};
			headers["appKey"] = "IOWlgu3VCB5vrfwE0YE0w3e24rgK4g612MZZEILt";
	
			$.ajax({
					method: "GET",
					headers: headers,
					url: "https://apis.openapi.sk.com/tmap/geo/reverseLabel?version=1&format=json&callback=result",
					async: false,
					data: {
							reqLevel: zoomLevel,
							centerLon: Clicklon,
							centerLat: Clicklat,
							reqCoordType: "WGS84GEO",
							resCoordType: "WGS84GEO",
					},
					success: function (response) {
							var resultInfo = response.poiInfo;
							lat = resultInfo.poiLat;
							lon = resultInfo.poiLon;
							poiId = resultInfo.id;
							name = resultInfo.name;
	
							url = `https://apis.openapi.sk.com/tmap/puzzle/pois/${poiId}?format=json&appKey=IOWlgu3VCB5vrfwE0YE0w3e24rgK4g612MZZEILt&lat=${Clicklat}&lng=${Clicklon}`;
	
							reset();
							puzzle(url, lon, lat, Clicklon, Clicklat);
					},
					error: function (request, status, error) {
							console.log("code:" + request.status + "\n" + "message:" + request.responseText + "\n" + "error:" + error);
					},
			});
	}
	
    function reset(){
        if(InfoWindow != undefined){
            InfoWindow.setMap(null);
            InfoWindow = undefined;
        }
        if(marker != undefined){
            marker.setMap(null);
        }
        if(rect != undefined){
                rect.setMap(null);
                rect = undefined;
            }
	   }


	function puzzle(url, lon, lat, Clicklon, Clicklat) {
    // 이전 오버레이 삭제
    if (InfoWindow) {
        InfoWindow.setMap(null);
        InfoWindow = undefined;
    }

    $.ajax({
        method: "GET",
        url: url,
        async: false,
        data: {},
        success: function (response) {
            var rltm = response.contents.rltm;
            var congestion, congestionLevel, datetime;
            var congestion2, congestionLevel2, datetime2;

            for (var i = 0; i < rltm.length; i++) {
                if (rltm[i].type == 1) {
                    congestion = (Number(rltm[i].congestion) * 100).toFixed(2);
                    congestionLevel = rltm[i].congestionLevel;
                    datetime = rltm[i].datetime;
                } else if (rltm[i].type == 2) {
                    congestion2 = (Number(rltm[i].congestion) * 100).toFixed(2);
                    congestionLevel2 = rltm[i].congestionLevel;
                    datetime2 = rltm[i].datetime;
                }
            }

            const colorObj = congestionLevelColor(congestionLevel);
            const colorObj2 = congestionLevelColor(congestionLevel2);
            color = colorObj.color;
            congest = colorObj.congest;
            color2 = colorObj2.color;
            congest2 = colorObj2.congest;

            rect = new Tmapv2.Rectangle({
                bounds: new Tmapv2.LatLngBounds(
                    new Tmapv2.LatLng(Number(Clicklat) + 0.0014957, Number(Clicklon) - 0.0018867),
                    new Tmapv2.LatLng(Number(Clicklat) - 0.0014957, Number(Clicklon) + 0.0018867)
                ), // 사각형 영역 좌표
                strokeColor: "#000000", // 테두리 색상
                strokeWeight: 2.5,
                strokeOpacity: 1,
                fillColor: color2, // 사각형 내부 색상
                fillOpacity: 0.5,
                map: map, // 지도 객체
            });

            if (rltm.length >= 2) {
                var year = datetime.substr(0, 4);
                var month = datetime.substr(4, 2);
                var day = datetime.substr(6, 2);
                var hour = datetime.substr(8, 2);
                var min = datetime.substr(10, 2);
                var sec = datetime.substr(12, 2);
                var date = `${year}년 ${month}월 ${day}일 ${hour}시 ${min}분 ${sec}초`;

                var year2 = datetime2.substr(0, 4);
                var month2 = datetime2.substr(4, 2);
                var day2 = datetime2.substr(6, 2);
                var hour2 = datetime2.substr(8, 2);
                var min2 = datetime2.substr(10, 2);
                var sec2 = datetime2.substr(12, 2);
                var date2 = `${year2}년 ${month2}월 ${day2}일 ${hour2}시 ${min2}분 ${sec2}초`;

                result = `[장소] ${name} [${congest}, ${congestion}명/100m²]<br>`;
                result += `[주변] ${name} [${congest2}, ${congestion2}명/100m²]`;

                // 새로운 InfoWindow 생성
                InfoWindow = new Tmapv2.InfoWindow({
                    position: new Tmapv2.LatLng(Clicklat, Clicklon), // 사각형 중심 좌표
                    content: `<div style="background: rgba(255, 255, 255, 0.7); 
                                         border: 1px solid #000; 
                                         padding: 5px; 
                                         border-radius: 5px; 
                                         text-align: center;">
                                 ${result}
                             </div>`, // 텍스트 내용
                    type: 2, // type 2로 설정하면 지도 위 고정
                    map: map, // 지도 객체
                });
            } else {
                result = `[주변] ${name} [${congest2}, ${congestion2}명/100m²]`;

                // 새로운 InfoWindow 생성
                InfoWindow = new Tmapv2.InfoWindow({
                    position: new Tmapv2.LatLng(Clicklat, Clicklon), // 사각형 중심 좌표
                    content: `<div style="background: rgba(255, 255, 255, 0.7); 
                                         border: 1px solid #000; 
                                         padding: 5px; 
                                         border-radius: 5px; 
                                         text-align: center;">
                                 ${result}
                             </div>`, // 텍스트 내용
                    type: 2, // type 2로 설정하면 지도 위 고정
                    map: map, // 지도 객체
                });
            }

        },
        error: function (request, status, error) {
            if (request.status == "404") {
                result = `POI ID: ${poiId}, ${name}, 해당 좌표는 실시간 장소 혼잡도를 지원하고 있지 않습니다.`;
                $("").text(result);
            } else {
                console.log("code:" + request.status + "\n" + "message:" + request.responseText + "\n" + "error:" + error);
            }
            },
        });
    }
	
    // 혼잡도
	function squareMap() {
    resetActiveStates(); // 다른 기능 초기화
    isSquareMapActive = true; // squareMap 활성화

    $(".api_etc_btns > div#squareMap").addClass("__color_blue_fill");
    $("#map_wrap").html(`
        <div id="map_div" class="map_wrap" style='position: relative; bottom: -20px;'></div>
        <div style='position: relative; bottom: 135px; left: 10px; width: 95px; height: 140px; text-align: center; background: #ffffff; border: 1px solid #808080; border-radius: 3px; font-size: 12px'>
            장소혼잡도 단계
            <div style='width: 84px; height: 25px; border: 1px solid #808080; text-align: center; background: #9cf7bd; border-radius: 3px; margin: 3px auto'>여유</div>
            <div style='width: 84px; height: 25px; border: 1px solid #808080; text-align: center; background: #73b7ff; border-radius: 3px; margin: 3px auto'>보통</div>
            <div style='width: 84px; height: 25px; border: 1px solid #808080; text-align: center; background: #d9a8ed; border-radius: 3px; margin: 3px auto'>혼잡</div>
            <div style='width: 84px; height: 25px; border: 1px solid #808080; text-align: center; background: #ff96b4; border-radius: 3px; margin: 3px auto'>매우 혼잡</div>
        </div>
    `);
    }
    
    //혼잡도별 색상, 혼잡도 표시 함수
	   function congestionLevelColor(congestionLevel){
		   var congest = ""
		   var color = ""
		   
		   switch(congestionLevel){
			case 1:
				congest ="여유";
				color = '#9cf7bd';
				break;
			case 2:
				congest ="보통";
	  			color ='#73b7ff';
				break;
			case 3:
				congest ="혼잡";
		  		color ='#d9a8ed';
				break;
			case 4:
				congest ="매우 혼잡";
		  		color ='#ff96b4';
				break;
			}
		   return {"color":color,"congest":congest}
	   }

    function resetActiveStates() {
    // 모든 기능의 활성 상태를 초기화
    isSquareMapActive = false;
    isAutoTrafficActive = false;
    isMeasureDistanceActive = false;

    // 버튼 UI 초기화
    $(".api_etc_btns > div").removeClass("__color_blue_fill");
	$(".api_etc_labels > div").hide();

    // 지도 위 객체 초기화
    if (rect) {
        rect.setMap(null);
        rect = undefined;
    }
    if (InfoWindow) {
        InfoWindow.setMap(null);
        InfoWindow = undefined;
    }

		try {
      tData.autoTraffic(map, { trafficOnOff: false });
    } catch (error) {}
    // 지도 초기화
    $("#map_wrap").empty();
    }

    function resetMeasureObject() {
    $(".api_etc_btns > div").removeClass("__color_blue_fill");
    $(".api_etc_labels > div").hide();

    // 기본 정보 제거
    try {
      if (measureDistance) {
        measureDistance.remove();
      }
    } catch (error) {}

    // 교통정보 제거
    try {
      tData.autoTraffic(map, { trafficOnOff: false });
    } catch (error) {}

    // 추가적인 UI 초기화
    $("#map_wrap").empty();
    }
    // puzzle함수 끝

    // 교통정보 시작
    function autoTraffic() {
        resetActiveStates(); // 다른 기능 초기화
        isAutoTrafficActive = true; // autoTraffic 활성화

        $(".api_etc_btns > div#autoTraffic").addClass("__color_blue_fill");
        tData.autoTraffic(map, { trafficOnOff: true });

        $("#map_wrap").html(`
                <div id="map_div" class="map_wrap" style="position: relative; bottom: -20px;"></div>
                <div style="position: relative; bottom: 135px; left: 10px; width: 95px; height: 140px; text-align: center; background: #ffffff; border: 1px solid #808080; border-radius: 3px; font-size: 12px">
                        교통상황 단계
                        <div style="width: 84px; height: 25px; border: 1px solid #808080; text-align: center; background: #99cc00; border-radius: 3px; margin: 3px auto">여유</div>
                        <div style="width: 84px; height: 25px; border: 1px solid #808080; text-align: center; background: yellow; border-radius: 3px; margin: 3px auto">보통</div>
                        <div style="width: 84px; height: 25px; border: 1px solid #808080; text-align: center; background: orange; border-radius: 3px; margin: 3px auto">혼잡</div>
                        <div style="width: 84px; height: 25px; border: 1px solid #808080; text-align: center; background: #cc0000; border-radius: 3px; margin: 3px auto">매우 혼잡</div>
                </div>
        `);
	}
	   
	//혼잡도별 색상, 혼잡도 표시 함수
    function congestionLevelColor(congestionLevel){
        var congest = ""
        var color = ""
        
        switch(congestionLevel){
        case 1:
            congest ="여유";
            color = '#9cf7bd';
            break;
        case 2:
            congest ="보통";
            color ='#73b7ff';
            break;
        case 3:
            congest ="혼잡";
            color ='#d9a8ed';
            break;
        case 4:
            congest ="매우 혼잡";
            color ='#ff96b4';
            break;
        }
        return {"color":color,"congest":congest}
    }


    $(document).ready(function() {
        var currentKeyword = $('#searchKeyword').val();
        
        $(".hashtag").hover(
            function() {
                // 마우스가 요소 위에 있을 때
                $(this).css({
                    "background-color": "#FF9E44",
                    "color": "white"
                });
            },
            function() {
                // 마우스가 요소를 벗어났을 때
                if (!$(this).hasClass("active")) {
                    $(this).css({
                        "background-color": "#ffc792",
                        "color": "black"
                    });
                }
            }
        );

        $(".hashtag").on("click", function(e) {
            e.preventDefault(); // 기본 동작 방지
            var text = $(this).text().trim(); // 텍스트 가져오기
            var keyword = text.split('#')[1].trim().slice(0, -2); // # 제거 후 뒤의 단어 추출
            
            // 현재 클릭된 li가 이미 active 상태인지 확인
            if ($(this).hasClass("active")) {
                // active 상태일 경우 비활성화
                $(this).removeClass("active").css({
                    "background-color": "#ffc792",
                    "color": "black"
                });
    
                // 검색창 초기화 및 결과 지우기
                $('#searchKeyword').val("");
                $("#searchResult").html("");
                clearMarkers();
                updateCategoryImage(""); // 모든 li 이미지 상태 초기화
            } else {
                // active 상태가 아닐 경우 활성화
                $(".hashtag").removeClass("active").css({
                    "background-color": "#ffc792",
                    "color": "black"
                });
                $(this).addClass("active").css({
                    "background-color": "#FF9E44",
                    "color": "white"
                });
    
                // 검색창에 키워드 입력
                $("#searchKeyword").val(keyword);
                console.log(keyword);
                $("#btn_select").click(); // 검색 버튼 클릭 트리거 
            }
        });

        // 지도 검색창 기능
        $("#btn_select").on("click", function () {
            var searchKeyword = $('#searchKeyword').val(); // 검색 키워드
            var headers = {};
            headers["appKey"] = "IOWlgu3VCB5vrfwE0YE0w3e24rgK4g612MZZEILt";   
            
            $(".hashtag").each(function() {
                var text = $(this).text().trim();
                var hashtagText = text.split('#')[1].trim().slice(0, -2);
                // 입력된 검색어와 일치하는 해시태그를 활성화
                if (hashtagText === searchKeyword) {
                    $(this).addClass("active").css({
                        "background-color": "#FF9E44",
                        "color": "white"
                    });
                }
            });
            
            // 현재 지도 중심 좌표 가져오기
            var currentCenter, currentLat, currentLon;
            console.log("현재 지도 중심 좌표:", currentLat, currentLon);
            if (map && typeof map.getCenter === 'function') {
                currentCenter = map.getCenter();
                currentLat = currentCenter.lat();
                currentLon = currentCenter.lng();
            } else {
                console.log("map.getCenter() is not available");
            }

            // li 이미지 상태 업데이트
            updateCategoryImage(searchKeyword);

            // 카테고리와 관련 없는 키워드 검색 시 10개만 출력, 카테고리 관련 시 50개 출력
            var resultCount = (isCategoryRelated(searchKeyword)) ? 200 : 50;

            // 마커 이미지 결정
            var markerImage = getMarkerImage(searchKeyword);

            // 검색어가 비어있을 경우 마커와 결과 초기화
            if (!searchKeyword) {
                clearMarkers();  // 마커 및 결과 초기화
                $("#searchResult").html("");  // 검색 결과 목록 초기화
                return;
            }

            $.ajax({
                method: "GET", // 요청 방식
                headers: headers,
                url: "https://apis.openapi.sk.com/tmap/pois?version=1&format=json", // url 주소
                data: { // 요청 데이터 정보
                    "searchKeyword": searchKeyword, // 검색 키워드
                    "resCoordType": "EPSG3857", // 응답 좌표계
                    "centerLon": currentLon,
                    "centerLat": currentLat,
                    "count": resultCount // 출력되는 데이터 개수
                },
                success: function (response) {
                    var resultpoisData = response.searchPoiInfo.pois.poi;

                    // 기존 마커, 팝업 제거
                    clearMarkers();

                    var innerHtml = ""; // searchResult 결과값 노출 위한 변수
                    var positionBounds = new Tmapv2.LatLngBounds(); // LatLngBounds 객체 생성

                    // "주차장"이 포함되지 않도록 필터링
                    var filterData = resultpoisData.filter(function(poi) {
                        // 검색어가 "주차장"이 아닐 때만 "주차장"이 포함된 데이터를 제외
                        if (searchKeyword !== "주차장" && poi.name.includes("주차장")) {
                            return false;  // "주차장"이 포함된 POI는 제외
                        }
                        
                        return true;  // 나머지 POI는 포함
                    });

                    // POI 마커 표시
                    for (var k in filterData) {
                        var name = filterData[k].name;
                        var noorLat = Number(filterData[k].noorLat);
                        var noorLon = Number(filterData[k].noorLon);

                        if (name.includes("촬영지")) {
                            continue;
                        }

                        // 좌표 객체 생성
                        var pointCng = new Tmapv2.Point(noorLon, noorLat);

                        // EPSG3857 좌표계를 WGS84GEO 좌표계로 변환
                        var projectionCng = new Tmapv2.Projection.convertEPSG3857ToWGS84GEO(pointCng);

                        var lat = projectionCng._lat;
                        var lon = projectionCng._lng;

                        var markerPosition = new Tmapv2.LatLng(lat, lon);

                        // 마커 설정
                        var marker = new Tmapv2.Marker({
                            position: markerPosition, // 마커 위치
                            icon: markerImage, // 카테고리에 맞는 마커 이미지 사용
                            iconSize: new Tmapv2.Size(30, 35), // 마커 크기 (24x35)
                            title: name, // 마커 제목
                            map: map // 지도에 마커 등록
                        });

                        // 결과창에 나타날 HTML 구성
                        innerHtml += "<li><div><img src='" + markerImage + "' style='vertical-align:middle;' class='marker-img'>&nbsp;&nbsp;<span>"
                            + name
                            + "&nbsp;&nbsp;</span><button type='button' name='sendBtn' class='sendBtn' onClick='poiDetail(" + filterData[k].id + ");' style='font-size: 15px; width: 70px; height: 30px;'>상세보기</button></div></li><br>";

                        // 마커 배열에 저장
                        markerArr.push(marker);
                        positionBounds.extend(markerPosition); // LatLngBounds 확장
                    }

                    // 검색 결과 출력
                    $("#searchResult").html(innerHtml);

                    // 바운드 설정 없이, 맵 위치 고정
                    if (markerArr.length > 0) {
                        // 현재 맵의 줌 레벨을 저장
                        var currentZoom = map.getZoom();

                        // 마커들이 생성되었을 때만 중심을 설정하고 확대하지 않음
                        var centerPosition = markerArr[0].getPosition(); // 첫 번째 마커 위치로 맵 중심 설정
                        map.setCenter(currentCenter);

                        // 기존 줌 레벨을 유지
                        map.setZoom(currentZoom);
                    }
                },
                error: function (request, status, error) {
                    console.log("code:" + request.status + "\n"
                        + "message:" + request.responseText
                        + "\n" + "error:" + error);
                }
            });
        });
        
        
    });
    
    // 카테고리 함수 시작
    // 카테고리와 관련된 검색인지 확인하는 함수
    function isCategoryRelated(keyword) {
        var relatedKeywords = ["카페", "ATM", "주차장", "화장실", "약국", "주유소"];  // tmap 카테고리 관련 키워드 목록
        // var angkeywords = ["크리스마스", "와인/바", "비건식당", "연말파티", "브런치", "제철음식", "데이트"];  // 앙꼬 카테고리 관련 키워드 목록
        return relatedKeywords.includes(keyword);
        // return angkeywords.includes(keyword);
    }
    
    // 카테고리에 맞는 마커 이미지 반환 함수
    function getMarkerImage(keyword) {
        // 카테고리 관련 키워드에 맞는 마커 이미지 반환
        if (isCategoryRelated(keyword)) {
            switch (keyword) {
                case "카페":
                    return "/static/images/cafepin.png"; // 카페 마커 이미지
                case "ATM":
                    return "/static/images/atmpin.png"; // ATM 마커 이미지
                case "주차장":
                    return "/static/images/parkpin.png"; // 주차장 마커 이미지
                case "화장실":
                    return "/static/images/bath.png"; // 화장실 마커 이미지
                case "약국":
                    return "/static/images/mad.png"; // 약국 마커 이미지
                case "주유소":
                    return "/static/images/oilpin.png"; // 주유소 마커 이미지
                default:
                    return "/static/images/defaultpin.png"; // 기본 마커 이미지
            }
        } else {
            // 카테고리 관련 없는 경우 기본 마커 이미지
            return "/static/images/default.png"; 
        }
    }
    
    // 카테고리 관련된 li 이미지 업데이트 함수
    function updateCategoryImage(searchKeyword) {
        const listItems = document.querySelectorAll("#s_c li");
    
        listItems.forEach(item => {
            const text = item.textContent.trim(); // li의 텍스트 (카테고리명)
            const imageOff = item.getAttribute("data-image-off");
            const imageOn = item.getAttribute("data-image-on");
    
            if (text === searchKeyword) {
                // 검색어와 일치하는 li를 활성화 상태로 설정
                item.style.backgroundImage = `url(${imageOn})`;
                item.classList.add("active");
            } else {
                // 검색어와 일치하지 않는 li는 비활성화 상태로 설정
                item.style.backgroundImage = `url(${imageOff})`;
                item.classList.remove("active");
            }
        });
    }
    
    // 마커 및 결과 초기화 함수
    function clearMarkers() {
        // 기존 마커, 팝업 제거
        if (markerArr.length > 0) {
            for (var i in markerArr) {
                markerArr[i].setMap(null);
            }
            markerArr = [];
        }
    
        if (labelArr.length > 0) {
            for (var i in labelArr) {
                labelArr[i].setMap(null);
            }
            labelArr = [];
        }
    }
    
    // 카테고리 클릭 이벤트 리스너
    document.addEventListener("DOMContentLoaded", () => {
        const listItems = document.querySelectorAll("#s_c li");
    
        listItems.forEach(item => {
            const imageOff = item.getAttribute("data-image-off");
            item.style.backgroundImage = `url(${imageOff})`;
    
            item.addEventListener("click", () => {
                const searchKeyword = item.textContent.trim();
    
                // 현재 클릭된 카테고리가 이미 활성화 상태일 경우
                if (item.classList.contains("active")) {
                    // 검색창을 초기화하고, 마커와 결과도 초기화
                    $('#searchKeyword').val("");
                    $("#searchResult").html("");
                    clearMarkers();
                    updateCategoryImage(""); // 모든 li 이미지 상태 초기화
                } else {
                    // 모든 li를 초기화
                    listItems.forEach(otherItem => {
                        const otherImageOff = otherItem.getAttribute("data-image-off");
                        otherItem.style.backgroundImage = `url(${otherImageOff})`;
                        otherItem.classList.remove("active"); // 활성화 상태 제거
                    });
    
                    // 클릭한 li를 활성화 상태로 전환
                    const imageOn = item.getAttribute("data-image-on");
                    item.style.backgroundImage = `url(${imageOn})`;
                    item.classList.add("active");
    
                    // 검색창에 입력된 값도 동기화
                    $('#searchKeyword').val(searchKeyword);
    
                    // 검색 결과도 바로 출력
                    $("#btn_select").click();
                }
            });
        });
    });
    // 카테고리 함수 끝


var search_word = $("#searchKeyword").val();
var remote = $("#txt1").val()
console.log("remote :"+remote)
console.log("remote의타입 :"+typeof(remote))
if (remote == "1") {
    console.log("작동중")
    setTimeout(function() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function(position) {
                var lat = position.coords.latitude;
                var lon = position.coords.longitude;
                setMapCenter(lat, lon, search_word);
            })
        } else {
            console.log("작동실패")
            console.error("Geolocation is not supported by this browser.");
            // 기본 위치 값 사용
            var lat = currentLat;
            var lon = currentLon;
            setMapCenter(lat, lon, search_word);
        }

        updateMapCenter();
        $('#searchKeyword').val(search_word);
        $("#btn_select").trigger('click');

        console.log("Remote:", remote);
        console.log("search_word:", search_word);
    }, 70);  // 딜레이

}

// 수정
function checkPkey(pkey) {
    pkey = Number(pkey)
    var plist = [1114356301, 1040638501, 1093486001, 1104585101, 1134911301, 1137459301, 226314801, 1036699701, 581844301, 568556401, 1039723801, 539474201, 681503501, 1180605601, 299389301, 151146001, 226076800, 275446100, 151147201, 1089199001, 151146001, 236561100]

    if (plist.includes(pkey)) {
        alert("Ajax 호출")
        $.ajax({
            method: "GET",
            url: "/foodBoard/getImages/",
            data: {
                "pKey": pkey
            },
            success: function (response) {
                alert('ajax 호출완료')
                bNo = response.bNo;
                bFile1 = response.bFile1;
                bFile2 = response.bFile2;
                bFile3 = response.bFile3;
                TimeAvg = response.TimeAvg;
                // alert("bFile1: " + bFile1);
                // alert("bFile2: " + bFile2);
                // alert("bFile3: " + bFile3);
                // alert("TimeAvg: " + TimeAvg);
                rate_count = response.rate_count;
                rate_list = response.rate_list;
                alert("rate_list: " + rate_list); // 회원이 남긴 반응 ['1']
                alert("rate_count: " + rate_count); // 반응 개수 [0,0,0,0,0,0,0,0,0]
                
            }
        });
    }
}

// 수정



// 4. POI 상세 정보 API
//--- POI 상세 정보 API Sample >> https://tmapapi.tmapmobility.com/main.html#webservice/sample/WebSamplePoiDetail
async function poiDetail(poiId) {
    var headers = {};
    headers["appKey"] = "IOWlgu3VCB5vrfwE0YE0w3e24rgK4g612MZZEILt";

    $.ajax({
        method: "GET",
        headers: headers,
        url: "https://apis.openapi.sk.com/tmap/pois/" + poiId + "?version=1&resCoordType=EPSG3857&format=json",
        success: function(response) {
            var detailInfo = response.poiDetailInfo;
            var id = detailInfo.id;
            var pkey = detailInfo.pkey;
            
            // 수정
            checkPkey(pkey) // bFile1,2,3 img.url 호출완료
            //수정
            setTimeout(function () {
                
                
                // 샘플 데이터를 사용해 추가 상세 정보 가져오기
                var poiDetailData = getCustomPoiDetails(id, pkey);
                
                
                
                
                var coloredNewAddress = '';
                if (poiDetailData && poiDetailData.newAddress) {
                    coloredNewAddress = poiDetailData.newAddress.replace('①', '<span style="color: #263c96;">①</span>')
                    .replace('⑦', '<span style="color: #697215;">⑦</span>');
                }               
                
                
                // 상세보기 콘텐츠 생성
                var content = `
                <div style='position: relative; padding: 20px;'>
                <div style='position: absolute; top: 10px; right: 10px; cursor: pointer; font-size: 20px;' onclick='closeSlidePanel();'>×</div>
                <div>
            ${bFile1 ? `<input type="hidden" id="pkey" value="${pkey}">` : ''}
            ${bFile1 ? `<div class="imgContainer" style="width: 510px; height: 200px; overflow: hidden; margin-bottom: 10px; margin-top: 10px; box-sizing: border-box; position: relative; right: 40px; display: flex;">` : ""}
            ${bFile1 ? `<img src="${bFile1}" style="width: 170px; height: 200px; object-fit: cover;">` : ''} 
            ${bFile2 ? `<img src="${bFile2}" style="width: 170px; height: 200px; object-fit: cover;">` : ''}
            ${bFile3 ? `<img src="${bFile3}" style="width: 170px; height: 200px; object-fit: cover;">` : ''}
            ${bFile1 ? `</div>` : ""}
        
            
            <b class='Title2' style='color: black; font-size: 30px; line-height: 1.5;'><a href="/foodBoard/foodView/${bNo}/">${detailInfo.name}</a></b>
            ${poiDetailData && poiDetailData.subClassNmC ? `<b style='color: black; font-size: 15px; line-height: 1.5; font-weight: 400;'>&nbsp;${poiDetailData.subClassNmC}</b>` : ''}<br>
            ${poiDetailData && poiDetailData.desc ? `<b style='color: black; font-size: 18px; line-height: 1.5; font-weight: 400;'>&nbsp;${poiDetailData.desc}</b><br><br>` : '<br>'}
            
            ${TimeAvg != -1 ? `<b style='color: #60212E; font-size: 20px; line-height: 1.5; font-weight: 400;'><i class="fa-solid fa-hourglass-start" style='color: #c5c5c5;'></i>&nbsp; 평균 대기시간 : ${TimeAvg} 분</b></br>` : 
            `<b style='color: #60212E; font-size: 20px; line-height: 1.5; font-weight: 400;'><i class="fa-solid fa-hourglass-start" style='color: #c5c5c5;'></i>&nbsp; 평균 대기시간 : 정보 없음</b></br>`}
            <b style='color: black; font-size: 20px; line-height: 1.5; font-weight: 400;'><i class="fa-solid fa-location-dot" style='color: #c5c5c5;'></i>&nbsp; ${detailInfo.address} ${detailInfo.roadName} ${detailInfo.firstNo}-${detailInfo.secondNo}</b><br>
            ${coloredNewAddress ? `<b style='color: black; font-size: 18px; line-height: 1.5; font-weight: 400;'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;${coloredNewAddress}</b><br>` : ''}
            ${poiDetailData && poiDetailData.easycome ? `<b style='color: black; font-size: 20px; line-height: 1.5; font-weight: 400;'><i class="fa-solid fa-map" style='color: #c5c5c5;'></i>&nbsp; ${poiDetailData.easycome}</b><br>` : ''}
            ${poiDetailData && poiDetailData.time ? `<b style='color: black; font-size: 20px; line-height: 1.5; font-weight: 400;'><i class="fa-solid fa-clock" style='color: #c5c5c5;'></i>&nbsp; ${poiDetailData.time}</b><br>` : ''}
            ${poiDetailData && poiDetailData.telNo ? `<b style='color: black; font-size: 20px; line-height: 1.5; font-weight: 400;'><i class="fa-solid fa-phone" style='color: #c5c5c5;'></i>&nbsp; ${poiDetailData.telNo}</b><br>` : ''}
            ${poiDetailData && poiDetailData.instagram ? `
                <b style='color: black; font-size: 20px; line-height: 1.5; font-weight: 400;'>
                <i class="fa-solid fa-globe" style='color: #c5c5c5;'></i>&nbsp; 
                <a href="${poiDetailData.instagram}" target="_blank" style="color: black; text-decoration: none;">인스타그램</a>
                </b><br>` : ''}
                ${poiDetailData && poiDetailData.additionalInfo ? `<b style='color: black; font-size: 20px; line-height: 1.5; font-weight: 400;'><i class="fa-solid fa-store" style='color: #c5c5c5;'></i>&nbsp; ${poiDetailData.additionalInfo}</b>` : ''}
                </div>
                </div>

                ${bFile1 ?
                    `<div class="comment_div2">
                        <button type='button' class="comment_list2 ${rate_list.includes('1') ? 'comment_effective' : ''}">
                            <h4 class="comment_content2"><span class="comment_icon2">😋</span>음식이 맛있어요</h4>
                            <h4 class="comment_cnt2">${rate_count[0]}명</h4>
                            <input class="comment_rating2" type='hidden' value="1">
                        </button>
                        <button type='button' class="comment_list2 ${rate_list.includes('2') ? 'comment_effective' : ''}">
                            <h4 class="comment_content2"><span class="comment_icon2">🍚</span>양이 많아요</h4>
                            <h4 class="comment_cnt2">${rate_count[1]}명</h4>
                            <input class="comment_rating2" type='hidden' value="2">
                        </button>
                        <button type='button' class="comment_list2 ${rate_list.includes('3') ? 'comment_effective' : ''}">
                            <h4 class="comment_content2"><span class="comment_icon2">👀</span>매장이 넓어요</h4>
                            <h4 class="comment_cnt2">${rate_count[2]}명</h4>
                            <input class="comment_rating2" type='hidden' value="3">
                        </button>
                        <button type='button' class="comment_list2 ${rate_list.includes('4') ? 'comment_effective' : ''}">
                            <h4 class="comment_content2"><span class="comment_icon2">💸</span>가성비가 좋아요</h4>
                            <h4 class="comment_cnt2">${rate_count[3]}명</h4>
                            <input class="comment_rating2" type='hidden' value="4">
                        </button>
                        <button type='button' class="comment_list2 ${rate_list.includes('5') ? 'comment_effective' : ''}">
                            <h4 class="comment_content2"><span class="comment_icon2">💖</span>친절해요</h4>
                            <h4 class="comment_cnt2">${rate_count[4]}명</h4>
                            <input class="comment_rating2" type='hidden' value="5">
                        </button>
                        <button type='button' class="comment_list2 ${rate_list.includes('6') ? 'comment_effective' : ''}">
                            <h4 class="comment_content2"><span class="comment_icon2">🌱</span>재료가 신선해요</h4>
                            <h4 class="comment_cnt2">${rate_count[5]}명</h4>
                            <input class="comment_rating2" type='hidden' value="6">
                        </button>
                        <button type='button' class="comment_list2 ${rate_list.includes('7') ? 'comment_effective' : ''}">
                            <h4 class="comment_content2"><span class="comment_icon2">⛰️</span>뷰가 좋아요</h4>
                            <h4 class="comment_cnt2">${rate_count[6]}명</h4>
                            <input class="comment_rating2" type='hidden' value="7">
                        </button>
                        <button type='button' class="comment_list2 ${rate_list.includes('8') ? 'comment_effective' : ''}">
                            <h4 class="comment_content2"><span class="comment_icon2">✨</span>매장이 청결해요</h4>
                            <h4 class="comment_cnt2">${rate_count[7]}명</h4>
                            <input class="comment_rating2" type='hidden' value="8">
                        </button>
                        <button type='button' class="comment_list2 ${rate_list.includes('9') ? 'comment_effective' : ''}">
                            <h4 class="comment_content2"><span class="comment_icon2">🚘</span>주차장이 넓어요</h4>
                            <h4 class="comment_cnt2">${rate_count[8]}명</h4>
                            <input class="comment_rating2" type='hidden' value="9">
                        </button>
                    </div>`:""}
                `;
                
                // HTML 삽입
                
                setTimeout(function () { document.getElementById("slide_content").innerHTML = content; }, 500);
                
                // 슬라이드 패널 표시
                var slidePanel = document.getElementById("slide_panel");
                slidePanel.classList.add("active");
            }, 1000);
                
            // 지도 중심 이동 및 줌인
            if (detailInfo.frontLat && detailInfo.frontLon) {
                // EPSG3857 좌표계를 WGS84로 변환 (필요 시)
                var point = new Tmapv2.Point(detailInfo.frontLon, detailInfo.frontLat);
                var latLng = Tmapv2.Projection.convertEPSG3857ToWGS84GEO(point);

                // 지도 중심 이동 및 확대
                map.setCenter(new Tmapv2.LatLng(latLng._lat, latLng._lng));
                map.setZoom(17); // 줌 레벨 설정
            }

            // 슬라이드 패널 표시
            var slidePanel = document.getElementById("slide_panel");
            slidePanel.classList.add("active");
                
        },
        error: function(request, status, error) {
            console.log("code:" + request.status + "\n" + "message:" + request.responseText + "\n" + "error:" + error);
        }
    });
}

// 슬라이드 패널 닫기
function closeSlidePanel() {
    var slidePanel = document.getElementById("slide_panel");
    slidePanel.classList.remove("active");
}

// 샘플 데이터 기반 상세 정보 함수
function getCustomPoiDetails(id, pkey) {
    const sampleResponse = {
        "searchPoiInfo": {
            "totalCount": "65",
            "count": "2",
            "page": "1",
            "pois": {
                "poi": [
                    {
                        "id": "11143563",
                        "pkey": "1114356301",
                        "name": "커피사피엔스 가산 한라원앤원점",
                        "newAddress": "①,⑦ 가산디지털단지역 8번 출구에서 439m",
                        "easycome": "한라원앤원타워 1층 119호",
                        "telNo": "0507-2087-1057",
                        "desc": "한라원앤원타워 커피맛집",
                        "time": "평일 07:00 - 19:00",
                        "roadName": "가산디지털2로",
                        "subClassNmC": "카페",
                        "additionalInfo": "포장, 배달, 주차불가"
                    },
                    {
                        "id": "10406385",
                        "pkey": "1040638501",
                        "name": "인크커피 가산점",
                        "newAddress": "①,⑦ 가산디지털단지역 8번 출구에서 311m",
                        "easycome": "가산디지털단지역 6번 출구에서 도보 7분<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;대성디폴리스 지식산업센터 옆",
                        "telNo": "02-854-7200",
                        "desc": "금천구 카페계의 랜드마크",
                        "time": "매일 09:00 - 21:00",
                        "roadName": "가산디지털2로",
                        "instagram": "https://www.instagram.com/inccoffee__/",
                        "subClassNmC": "카페, 디저트",
                        "additionalInfo": "포장, 무선 인터넷, 남/녀 화장실 구분"
                    },
                    {
                        "id": "10934860",
                        "pkey": "1093486001",
                        "name": "원두서점",
                        "newAddress": "①,⑦ 가산디지털단지역 8번 출구에서 492m",
                        "easycome": "가산디지털단지역 8번 출구에서 도보 5분 거리",
                        "telNo": "02-6406-0588",
                        "desc": "작고 아늑한 분위기의 카페",
                        "time": "매일 08:00 - 20:00 / 정기휴무 (매주 일요일)",
                        "instagram": "https://www.instagram.com/coffeebeansbookstore/#",
                        "subClassNmC": "카페, 디저트",
                        "additionalInfo": "포장, 무선 인터넷, 간편결제"
                    },
                    {
                        "id": "11045851",
                        "pkey": "1104585101",
                        "name": "파란만잔 가산한라원앤원점",
                        "newAddress": "①,⑦ 가산디지털단지역 8번 출구에서 439m",
                        "easycome": "한라원앤원타워 104호 B동 건물외관 왼쪽",
                        "telNo": "0507-1411-2115",
                        "time": "매일 07:00 - 21:00 / 20:40 라스트오더",
                        "roadName": "",
                        "instagram": "https://www.instagram.com/paranmanjan_hallaoneandone/#",
                        "subClassNmC": "카페, 디저트",
                        "additionalInfo": "포장, 배달, 무선 인터넷, 예약, 단체 이용 가능"
                    },
                    {
                        "id": "11349113",
                        "pkey": "1134911301",
                        "name": "이에노",
                        "newAddress": "①,⑦ 가산디지털단지역 8번 출구에서 439m",
                        "easycome": "1층 120호 / 광장 커피사피엔스, 얌샘김밥 사이",
                        "telNo": "02-6406-0588",
                        "time": "매일 07:00 - 21:00 / 20:40 라스트오더",
                        "roadName": "",
                        "instagram": "https://www.instagram.com/lleno.kr/",
                        "subClassNmC": "카페, 디저트",
                        "additionalInfo": "포장, 예약, 반려동물 동반, 무선 인터넷, 예약, 단체 이용 가능"
                    },
                    {
                        "id": "11374593",
                        "pkey": "1137459301",
                        "name": "파더스베이글 가산디지털단지점",
                        "newAddress": "①,⑦ 가산디지털단지역 8번 출구에서 480m",
                        "easycome": "한라원앤원타워 주차장 입구 바로 오른편",
                        "telNo": "0507-2093-3096",
                        "time": "매일 09:00 - 20:00 / 정기휴무 (매주 일요일)",
                        "roadName": "",
                        "subClassNmC": "카페, 디저트",
                        "additionalInfo": "포장, 배달, 무선 인터넷, 남/녀 화장실 구분"
                    },
                    {
                        "id": "2263148",
                        "pkey": "226314801",
                        "name": "피오니",
                        "newAddress": "②,⑥ 합정역 3번 출구에서 452m",
                        "easycome": "젠틀몬스터 맞은편",
                        "telNo": "02-333-5325",
                        "desc": "홍대 딸기생크림 케이크 하면 생각나는 곳",
                        "time": "매일 12:00 - 22:00 / 21:00 라스트오더",
                        "instagram": "https://www.instagram.com/coffeebeansbookstore/#",
                        "subClassNmC": "카페, 디저트",
                        "tv": "생활의달인 320회(12.01.23. 케이크)",
                        "additionalInfo": "포장, 무선 인터넷, 간편결제"
                    },
                    {
                        "id": "10366997",
                        "pkey": "1036699701",
                        "name": "커피 벌스데이",
                        "newAddress": "② 홍대입구역 7번 출구에서 276m",
                        "telNo": "0507-1449-2353",
                        "time": "매일 11:00 - 20:50",
                        "instagram": "https://www.instagram.com/cbd.coffeebirthday/?utm_medium=copy_link",
                        "subClassNmC": "카페, 디저트",
                        "additionalInfo": "포장, 반려동물 동반, 무선 인터넷"
                    },
                    {
                        "id": "5818443",
                        "pkey": "581844301",
                        "name": "피오니 연남점",
                        "newAddress": "가좌역 1번 출구에서 665m",
                        "easycome": "연남로 59-1",
                        "telNo": "02-332-5325",
                        "desc": "홍대 연남동 딸기 케이크 맛집 피오니 peony 연남점",
                        "time": "매일 11:00 - 21:00 / 20:00 라스트오더",
                        "subClassNmC": "케이크전문",
                        "additionalInfo": "포장, 무선 인터넷, 간편결제"
                    },
                    {
                        "id": "5685564",
                        "pkey": "568556401",
                        "name": "1984",
                        "newAddress": "② 홍대입구역 2번 출구에서 161m",
                        "easycome": "혜원빌딩 1층",
                        "telNo": "0507-1374-3349",
                        "desc": "편집샵과 북카페로 유명한 연남동 카페",
                        "time": "매일 10:00 - 23:00 / 22:30 라스트오더",
                        "roadName": "",
                        "instagram": "https://www.instagram.com/1984store/",
                        "subClassNmC": "카페, 디저트",
                        "additionalInfo": "예약, 단체 이용 가능, 포장, 무선 인터넷"
                    },
                    {
                        "id": "10397238",
                        "pkey": "1039723801",
                        "name": "산리오러버스클럽",
                        "newAddress": "⑥ 상수역 1번 출구에서 455m",
                        "telNo": "0507-1382-6110",
                        "time": "매일 12:00 - 20:00 / 사전예약제로 운영 중",
                        "roadName": "",
                        "instagram": "https://www.instagram.com/sanrio_lovers_club/#",
                        "subClassNmC": "카페",
                        "additionalInfo": "예약, 무선 인터넷, 포장, 남/녀 화장실 구분"
                    },
                    {
                        "id": "5394742",
                        "pkey": "539474201",
                        "name": "딥커피",
                        "newAddress": "② 홍대입구역 2번 출구에서 239m",
                        "easycome": "마포구 동교동 209 1층",
                        "telNo": "02-303-2979",
                        "desc": "연남동 사이 애견동반 가능한 힙한 홍대카페",
                        "time": "매일 07:00 - 02:00 / 라운지 이용시간 1시간40분",
                        "roadName": "",
                        "subClassNmC": "카페",
                        "tv": "2TV저녁생생정보 123회(15.05.13. 1L 커피)",
                        "additionalInfo": "예약, 단체 이용 가능, 주차, 포장, 무선 인터넷"
                    },
                    {
                        "id": "6815035",
                        "pkey": "681503501",
                        "name": "테일러커피 연남1호점",
                        "newAddress": "② 홍대입구역 3번 출구에서 633m",
                        "easycome": "홍대입구역 3번 출구 7분 동교동 삼거리 7분",
                        "telNo": "02-326-0355",
                        "time": "매일 10:00 - 22:00",
                        "roadName": "",
                        "instagram": "https://www.instagram.com/tailor_coffee/",
                        "subClassNmC": "카페",
                        "additionalInfo": "포장, 단체 이용 가능, 무선 인터넷"
                    },
                    {
                        "id": "11806056",
                        "pkey": "1180605601",
                        "name": "씨더라이트",
                        "newAddress": "② 홍대입구역 8번 출구에서 145m",
                        "easycome": "1층 밥장인돼지찌개 건물",
                        "telNo": "0507-1389-9109",
                        "desc": "친구랑 너무 재밌게 놀고온 어바웃타임 암실카페",
                        "time": "매일 14:00 - 22:00 / 정기휴무 (매주 일요일)",
                        "roadName": "",
                        "instagram": "https://www.instagram.com/see_the_light_hd/",
                        "subClassNmC": "테마카페",
                        "additionalInfo": "단체 이용 가능, 남/녀 화장실 구분, 대기공간"
                    },
                    {
                        "id": "2993893",
                        "pkey": "299389301",
                        "name": "콘하스 연남점",
                        "newAddress": "② 홍대입구역 3번 출구에서 118m",
                        "easycome": "연희로 1-1 1,2층",
                        "telNo": "02-325-0792",
                        "time": "매일 10:00 - 23:00 / 22:00 라스트오더",
                        "roadName": "",
                        "instagram": "https://www.instagram.com/conhascoffee_co.ltd/#",
                        "subClassNmC": "카페, 디저트",
                        "additionalInfo": "무선 인터넷, 포장, 단체 이용 가능"
                    },
                    {
                        "id": "1511460",
                        "pkey": "151146001",
                        "name": "Tora.b",
                        "newAddress": "② 홍대입구역 8번 출구에서 262m",
                        "easycome": "어바웃미 홍대점에서 오른쪽 방향",
                        "telNo": "0507-1311-8041",
                        "desc": "홍대 카페 맛있는 파블로바맛집",
                        "time": "매일 12:00 - 21:30 / 정기휴무 (매주 일요일)",
                        "roadName": "",
                        "instagram": "https://www.instagram.com/tora___b/",
                        "subClassNmC": "카페",
                        "tv": "모닝와이드 6111회(15.08.04. 에스프레소 얼음)",
                        "additionalInfo": "단체 이용 가능, 포장, 배달, 예약"
                    },
                    {
                        "id": "2260768",
                        "pkey": "226076800",
                        "name": "위드커피",
                        "newAddress": "② 홍대입구역 8번 출구에서 128m",
                        "easycome": "오렌즈 왼쪽 골목에 위치",
                        "telNo": "0507-1426-7557",
                        "desc": "홍대 깔끔한 분위기 카페",
                        "time": "매일 09:00 - 23:30 / 23:00 라스트오더",
                        "roadName": "",
                        "subClassNmC": "카페",
                        "additionalInfo": "주차, 포장, 남/녀 화장실 구분"
                    },
                    {
                        "id": "2754461",
                        "pkey": "275446100",
                        "name": "앤트러사이트 합정점",
                        "newAddress": "⑥ 상수역 4번 출구에서 556m",
                        "easycome": "상수역, 합정역 사이",
                        "telNo": "02-336-7850",
                        "desc": "합정 공장카페 앤트러사이트 제대로 빈티지한 창고형카페",
                        "time": "매일 09:00 - 22:00 / 21:30 라스트오더",
                        "roadName": "",
                        "instagram": "https://www.instagram.com/anthracite_coffee_roasters/#",
                        "subClassNmC": "카페",
                        "tv": "굿모닝대한민국 783회(14.05.28.)",
                        "additionalInfo": "남/녀 화장실 구분, 포장, 반려동물 동반"
                    },
                    {
                        "id": "1511472",
                        "pkey": "151147201",
                        "name": "퐁포네뜨",
                        "newAddress": "② 홍대입구역 8번 출구에서 464",
                        "easycome": "어바웃미 홍대점에서 오른쪽 방향",
                        "telNo": "0507-1428-9012",
                        "desc": "홍대 카페 맛있는 파블로바맛집",
                        "time": "매일 10:30 - 21:00 / 20:30 라스트오더",
                        "roadName": "",
                        "subClassNmC": "베이커리",
                        "additionalInfo": "예약"
                    },
                    {
                        "id": "10891990",
                        "pkey": "1089199001",
                        "name": "오퍼",
                        "newAddress": "② 홍대입구역 9번 출구에서 306m",
                        "easycome": "상수동 카페거리 인근 위치",
                        "telNo": "0507-1486-9994",
                        "time": "매일 09:00 - 22:00 / 21:30 라스트오더",
                        "roadName": "",
                        "instagram": "https://www.instagram.com/offer_mapo/",
                        "subClassNmC": "카페, 디저트",
                        "tv": "모닝와이드 6111회(15.08.04. 에스프레소 얼음)",
                        "additionalInfo": "포장, 단체 이용 가능, 단체 이용 가능"
                    },
                    {
                        "id": "1511460",
                        "pkey": "151146001",
                        "name": "위드커피",
                        "newAddress": "② 홍대입구역 8번 출구에서 128m",
                        "easycome": "오렌즈 왼쪽 골목에 위치",
                        "telNo": "0507-1426-7557",
                        "desc": "홍대 깔끔한 분위기 카페",
                        "time": "매일 09:00 - 23:30 / 23:00 라스트오더",
                        "roadName": "",
                        "subClassNmC": "카페",
                        "additionalInfo": "주차, 포장, 남/녀 화장실 구분"
                    },
                    {
                        "id": "2365611",
                        "pkey": "236561100",
                        "name": "더카페 가산이노플렉스점",
                        "newAddress": "①,⑦ 가산디지털단지역 7번 출구에서 199m",
                        "easycome": "가산디지털단지 7번 출구 횡단보도 건너 바로 위치",
                        "telNo": "0507-2093-7909",
                        "time": "매일 07:00 - 19:00 / 정기휴무 (매주 일요일)",
                        "roadName": "",
                        "subClassNmC": "카페",
                        "instagram": "https://www.instagram.com/thecaffe_official/",
                        "additionalInfo": "포장, 무선 인터넷, 남/녀 화장실 구분"
                    },
                ]
            }
        }
    };

    // ID와 PKEY로 특정 장소 찾기
    const pois = sampleResponse.searchPoiInfo.pois.poi;
    return pois.find(poi => poi.id === id && poi.pkey === pkey) || null;

}


// 반응 클릭시 삭제/추가
$(document).on("click", ".comment_list2", function () {
    let csrftoken = $('meta[name="csrf-token"]').attr('content');
    var button = $(this);
    var pkey = $("#pkey").val();
    console.log(pkey);
    var rating = $(this).closest(".comment_list2").find(".comment_rating2").val();
    console.log(rating);
    var isEffective = button.hasClass('comment_effective');
    let status = isEffective ? "0" : "1";

    $.ajax({
        headers : {'X-CSRFToken': csrftoken},
        url: "/map/Rating2/",
        type: "POST",
        data: {
            "pKey": pkey,
            "rating": rating,
            "status": status
        },
        success: function (data) {
            console.log(data);
            if (data.result == "1") {
                alert(isEffective ? "반응을 삭제하였습니다." : "반응을 추가하였습니다.");
                button.toggleClass('comment_effective');
                let count = Number(button.find(".comment_cnt2").text().slice(0, -1));
                console.log("count : " + count)
                if (data.status == "1") { count += 1; }
                else if (data.status == "0") { count -= 1; }
                button.find(".comment_cnt2").text(count + "명")
            }
        },
    });


});







// 정보 초기화
$(document).ready(function() {
    // 필요 시 초기화 코드 추가
});

