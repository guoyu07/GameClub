/**
 * Created by albert on 15-10-29.
 */

$(function(){

    //点击登陆按钮
    $("#tips-login-button").click(function(){
        $(".jumbotron").hide()
        $("#dia-login").fadeIn("slow")
    })

    //点击注册按钮
    $("#tips-reg-button").click(function(){
        $(".jumbotron").hide()
        $("#dia-reg").fadeIn("slow")
    })


    //右边导航固定
    //TODO 函数有问题

    $(window).scroll(function(){
        var dist_to_nav = $(".right-nav").scrollTop();
        if(dist_to_nav>=$('#navbar').height()){
            $(".right-nav").css({"position": "fixed"})
        }else{
            $(".right-nav").css({"position": "relative"})
        }
    })

})
