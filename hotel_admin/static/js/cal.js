$(document).ready(function(){
  $(".date1").click(function (){
      var todaydt = new Date();
      var month = todaydt.getMonth() + 1;
      var day = todaydt.getDate();
      var year = todaydt.getFullYear();
      if(month < 10)
        month = '0' + month.toString();
      if(day < 10)
        day = '0' + day.toString();
      
      var maxdate = year + '-' + month + '-' + day;
      $('.date1').attr('min',maxdate);
    });
  })