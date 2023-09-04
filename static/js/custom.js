$(document).ready(function(){
	wow = new WOW(
	  {
		animateClass: 'animated',
		offset:       100,
		callback:     function(box) {
		  console.log("WOW: animating <" + box.tagName.toLowerCase() + ">")
		}
	  }
	);
	wow.init();
	
	$(".prodctd-link .prodctd-right h4").next().addClass("prodff");
	$(".prodctd-link .prodctd-left h4").next().addClass("prodff");
	 
	
	
	$(".product-detail.prdfix").parent().next("footer").addClass("footfix");
	$(".product-detail.prdfix").parent().prev("header").addClass("headfix");
	$(".scrollbtn").click(function(){
		$('html,body').animate({ scrollTop: $(this).parents().next("section").offset().top - 115}, 'slow');
	});
	$(".menubtnt1").click(function(){		
		$(".sidemenu").addClass("sidemenu2");
		$("body").addClass("fadec");
	});
	
	
	
	
	
	
	
	
	
	
	
	
	$(".menubtnt3").click(function(){
		$(".sidemenu").removeClass("sidemenu2");
		$("body").removeClass("fadec");
	});
	$(".menubtnt2").click(function(){
		$(".header-search").addClass('header-searchfix');
		$(".header-search .menubtnt2").addClass('acbtn');
	});
	$(".hcls-btn").click(function(){
		$(".header-search").removeClass('header-searchfix');
		$(".header-search .menubtnt2").removeClass('acbtn');		
	});
	
	
	
	$(".searchbox .closebtn").click(function(){
		$(".searchbox").fadeOut(500);
		$(".menubtnt2").show();
		
	});	
	
});

