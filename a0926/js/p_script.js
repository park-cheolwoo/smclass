$(function () {
  var count = 0;
  $("#searchBtn").click(function () {
    alert("클릭");
    
    let searchWord = $("#search_txt").val();
    let surl = `https://apis.data.go.kr/B551011/PhotoGalleryService1/gallerySearchList1?serviceKey=EPhM94JT5WuG2cnWrA7xBy4Ip1zeWGD%2Fc9StwgvLEua3LPV6Qgp9%2Bu%2Fq5hyyC9%2FtVA%2BL4WipZChsLpNs4obZ%2Bw%3D%3D&numOfRows=10&pageNo=1&MobileOS=ETC&MobileApp=AppTest&arrange=A&_type=json&keyword=`;
    surl += searchWord;

    $.ajax({
      url: surl,
      type: "get",
      data: "",
      datatype: "json",
      success: function (data) {
        alert("성공");
        console.log(data);
        var datalist = data.response.body.items.item;
        s_data = "";
        for (i = 0; i < datalist.length; i++) {
          var s_title = datalist[i].galTitle;
          var s_galPhotographer = datalist[i].galPhotographer;
          var s_galModifiedtime = datalist[i].galModifiedtime;
          var s_galWebImage = datalist[i].galWebImageUrl;
          
          s_data += `<tr>`
          s_data += `<td id="${count}">${count}<td>`
          s_data += `<td>${s_title}</td>`
          s_data += `<td>${s_galPhotographer}</td>`
          s_data += `<td>${s_galModifiedtime}</td>`
          s_data += `<td>${s_galWebImage}</td>`
          s_data += `</tr>`
          count++;
        }
        $("#tbody").html(s_data);
        s_data = "";
      },
      error: function () {
        alert("실패");
      }//error

    });//ajax

  });//검색버튼클릭

});//제이쿼리 선언