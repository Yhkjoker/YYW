function widthsize(){
  var windowWidth = $(window).width();
  if(windowWidth < 992) {
      //右侧浮动导航 开始   
      $('.Right-Nav ul li').click(function(){
        $(this).addClass('active').siblings('li').removeClass('active');
        $('.Jd').show();
      });   
      $('.Jd').click(function(){
        $(this).hide();
        $('.Right-Nav ul li').removeClass('active');
      });
      //右侧浮动导航 结束
  };

};

/*浏览器动态检测*/
widthsize();
$(window).resize(function(){
  widthsize();
});

/*头部搜索框*/
// $("*").click(function () {
//  $('#header .Nav-Wra .Top2-Nav ul li').eq(0).removeClass('active');
// });
// $('#header .Nav-Wra .Top2-Nav ul li').eq(0).click(function(event){
//        $(this).addClass('active');
//        $(this).find("input[type='text']").focus();
//        event.stopPropagation();
// });

// 页脚点击事件
$(function(){
  $(".page li a").click(function(){
    var fathers = $(this).parent("li[class]").siblings();
    fathers.each(function(){
      $(this).find("a").removeClass("active_page")
    });
    $(this).addClass("active_page");
  });
});

      

//截取字符
var hide_txt1 = 75;
$(".News-Div-Wra .row > a p").each(function() {
    if ($(this).text().length > hide_txt1) {
        $(this).html($(this).text().replace(/\s+/g, "").substr(0, hide_txt1) + "...")
    }
 });

// 轮播图
$(function(){
  var an1 = animation('.animated1', 'fadeInUp');
  //首页第一部分banner切换
  var swiper = new Swiper('.header-swiper', {
      pagination: '.header-swiper .swiper-pagination',
      nextButton: '.header-swiper .swiper-button-next',
      prevButton: '.header-swiper .swiper-button-prev',
      paginationClickable: true,
      simulateTouch: true,//禁止滑动
      centeredSlides: true,
      autoplay: 6000,
      fade: {
          crossFade: true,
      },
      autoplayDisableOnInteraction: false,
      effect: 'fade',//渐变
      loop: true
  });
  //首页第二部分banner切换
  var swiper = new Swiper('.Home-A-swiper', {
      pagination: '.Home-A-swiper .swiper-pagination',
      nextButton: '.Home-A-swiper .swiper-button-next',
      prevButton: '.Home-A-swiper .swiper-button-prev',
      paginationClickable: true,
      simulateTouch: true,//禁止滑动
      centeredSlides: true,
      autoplay: 6000,
      fade: {
          crossFade: true,
      },
      autoplayDisableOnInteraction: false,
      effect: 'fade',//渐变
      loop: true
  });
})





/*移动端导航显示 开始*/
var navToggle = 1; //nav-toggle是否点击控制器
$("#header .container-fluid .navbar-toggle").click(function(event) {
    if (navToggle) {
        $(this).addClass("active-toggle");
        $('#header .container-fluid .navbar-collapse').stop(false,true).stop().stop(false,true).stop().animate({'left':'0px'},500);
        navToggle = 0
    } else {
        $(this).removeClass("active-toggle");
        navToggle = 1
    };
});
/*移动端导航显示 结束*/



/*返回顶部*/
$(document).ready(function(){
  $('#Return-Top').click(function(){
      $("html, body").animate({scrollTop: 0+ "px"}, 400);
      return false;
  });
});

$(document).ready(function(){
    $(document).scroll(function(){
        //页面右侧浮动导航 开始
        $('.Right-Nav ul li').removeClass('active');
        $('.Jd').hide();
        var top = $(document).scrollTop();
        if(top < 500){
            $('.Right-Nav').removeClass('active');
        }
        else if(top > 500){
            $('.Right-Nav').addClass('active');
        };
        //页面右侧浮动导航 结束
    });
});

//页面动画
function animation(obj, animate) {//两个参数 第一个是时间 第二个是动画方式
    var sh = $(document).scrollTop(); //滚动条高度
    var wh = $(window).height(); //浏览器下窗口可视区域高度
    $(obj).each(function(index, el) {
        var tt = $(this).offset().top;  //偏移头部的距离
        var delay = "delay" + parseInt(index + 1);
        if (tt < sh + wh) {
            $(this).addClass(animate + " " + delay);
        }
    });

    $(window).scroll(function() {
        sh = $(document).scrollTop(); //滚动条高度
        wh = $(window).height(); //浏览器时下窗口可视区域高度
        $(obj).each(function() {
            var tt = $(this).offset().top;
            if (tt < sh + wh) {
                $(this).addClass('delay1 ' + animate);
            }
        });
    })
}


function cart(){
  //订单
  list = $('.Order-Div-Wra')
  // 订单中数量与总额
  list.each(function(){
  // 总额
  var total = 0 
  // 数量
  var num = 0 
  lists = $(this).find(".man")
  num = lists.length
  //数量标签
  quantity = $(this).find(".num")
  //总额标签
  amount = $(this).find(".total b")
  //计算总额
  lists.each(function(){
    price = $(this).find("b")
    price = parseFloat(price.text())
    total += price
  })
  quantity.text(num)
  amount.text(total)
  })
  //底部总额标签
  total_foot = $(".Order-Footer").find("span").eq(0).find("b")

  //计算订单总额
  function sum(){
    var total_amount = 0
    //选中的订单
    parents = $("input:checked")
    parents.each(function(){
      total = 0
      parent = $(this).parent("li")
      bro = parent.siblings(".total").find("b")
      total = parseFloat(bro.text())
      total_amount += total
    })
    total_foot.text(total_amount)
  }
  //选择订单
  $("input[type='checkbox']").click(function(){
    sum();
  }
  )

  //取消订单
  $(".cancel").click(function(){
    $(this).parents(".Order-Div-Wra").remove()
    sum();
  })
}


function append(){
  var id =0
  $("input[type='checkbox']").click(function(){
    var check = $(this).attr('check')
    if(check == '0'){
      $(this).attr('check','1')
      check = '1'
    }else{
      $(this).attr('check','0')
      check = '0'
    }

    index = $(this).attr('value')
    parent = $(this).parents(".Common").siblings(".Information")
    parent.eq(index).toggle()
    id = parent.eq(index).find('input').attr("value")
    if(check == '1'){
      man_info = parent.eq(index).find('input').clone()
      man = parent.eq(index).find('.man').clone()
        man.css('display','block')
      $(".order").append(man_info)
      $(".add").append(man)
      order_total()
    }else{
      list_info = $('.order input.man_id');
      list_man = $('.add .man');
      list_info.each(function(){
        var value = $(this).attr("value")
        if(value == id){
          console.log(value)
          $(this).remove()
        }
      });
      list_man.each(function(){
        var value = $(this).attr('value')
        if(value == id){
          $(this).remove()
        }
      });
      order_total();
    }

  });
  var agree = true
  $(".poa").find('input').click(function(){
    if(agree){
      $(this).parents(".poa").find('.submit').removeClass('disabled')
      agree = false
    }else{
      $(this).parents(".poa").find('.submit').addClass('disabled')
      agree = true
    }
  })
};

//订单页计算总额
function order_total(){
  var lists_man = $('.add .man')
  var total_amount = 0
  lists_man.each(function(){
  var price = $(this).find('b').text()
  total_amount += parseFloat(price)
  })
  total = $('.add').siblings('.f-r')
  total.find('b').text(total_amount)
}
order_total()
//刷新验证码
$(".captcha").hover(function(){
  $(this).css('cursor','pointer');
  $(this).click(function(){
      $.get("/captcha/refresh/?"+Math.random(), function(result){
        $('.captcha').attr("src",result.image_url);
        $('#id_captcha_0').attr("value",result.key);
    });
    return false;
  })
});

//错误信息以及验证码与输入框的样式
$(document).ready(function(){
  $(".captcha").addClass("button f-r");
  $("#id_captcha_1").addClass("txt f-l");
  $("#id_captcha_1").removeAttr('style');
  $("#Land .Land-Div .Land-Input span").css({"border":"0px","color":"#ee0000"})
});

//保存为出行人的按钮
var click = true
$('.userman').click(function(){
  if(click){
    console.log(0)
    $(this).attr("checked","checked");
    $(this).parents('.text-left').siblings('input').removeAttr("checked")
    click = false
  }else{
    console.log(1)
    $(this).removeAttr("checked");
    $(this).parents('.text-left').siblings('input').attr("checked",'checked')
    click = true
  }
});


//顶部搜索栏搜索方法
function search_click(){
    console.log(3)
    var type = $('#jsSelectOption').text(),
        keywords = $('#search_keywords').val(),
        request_url = '';
    if(keywords == ""){
        return
    }
    if(type == "identical_list"){
        console.log(1)
        request_url = "/identical_list/?keywords="+keywords
    }else if(type == "short_list"){
        request_url = "/short_list/?keywords="+keywords
    }else if(type == "long_list"){
        request_url = "/long_list/?keywords="+keywords
    }
    window.location.href = request_url
}


$('.search_keywords').click(function () {
    search_click();
    console.log(2)
});





