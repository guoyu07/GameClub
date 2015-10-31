/**
 * Created by albert on 15-10-29.
 */
/*类似于继承了jquery扩展jquery

函数(全局变量不介绍)      功能
 lqcGetUrlParam        获取get请求地址栏的参数
 showLoadDialog        加载提示窗口
 showOKDialog          成功提示窗口
 showErrorDialog       出错提示窗口
 getTimeBySQL          计算距离现在的时间
 showGroupsInfo        加载用户所在圈子信息
*/
(function($){
    //定义全局变量
    //config
    //每次加载帖子个数
    $.LQC_POST_LOAD_COUNT = 5;
    //每次加载评论数目
    $.LQC_COMMENT_LOAD_COUNT = 3;

    //获取GET请求的参数:正则表达式
    //参考来源：http://www.cnblogs.com/fishtreeyu/archive/2011/02/27/1966178.html
    $.lqcGetUrlParam = function(name){
        var reg = new RegExp("(^|&)"+ name +"=([^&]*)(&|$)");
        var r = window.location.search.substr(1).match(reg);
        if(r!=null)
            return  unescape(r[2]);
        return null;
    }

    //提示窗口
    //TODO 添加图标例如加载图标啥的
    $.showLoadDialog = function(str){
        $('#dia-load').css(
            'background', 'url(../image/...gif) no-repeat 20px center'
        )
            .html(str)
            .dialog('open');
    }

    $.showOKDialog = function(str, func){
        var len = arguments.length; //获取参数个数，爽
        $('#dia-load').css('background', 'url(../image/...gif) no-repeat 20px center')
            .html(str)
            .dialog('open')
        //1s后自动关闭窗口
        setTimeout(function () {
            $('#dia-load').dialog('close')
            if(len==2) func();
        }, 1000)
    }
    $.showErrorDialog = function(str, func){
        var len = arguments.length;
        $('#dia-load').css('background', 'url(image/...gif) no-repeat 20px center')
            .html(str)
            .dialog('open');
        //1s后自动关闭窗口
        setTimeout(function(){
            $('#dia-load').dialog('close');
            if(len==2) func();
        }, 1000)
    }

    // 从MySql的DATETIME计算距离现在的时间
    $.getTimeBySQL = function (date) {
        date = Date(date);
        now = new Date();
        time = '';
        if((now-date)/60000<60){
            time = Math.floor((now-date)/60000)+'分钟';
        }else if((now-date)/(60000*60)<24){
            time = Math.floor((now-date)/(60000*60))+'小时';
        }else{
            time = Math.floor((now-date)/(60000*60*24))+'天';
        }
        return time + '前';

    }
    /** 加载用户所在的圈子信息
    * @p1 用户ID
    * @p2
    * */
    $.showGroupsInfo = function (user_id, appendToWhat) {
        $.ajax({
            url:'',
            type:'POST',
            data:{
                id:user_id
            },
        })
            .done(function (response) {
                json = eval("("+response+")");
                //由于json是以”{}”的方式来开始以及结束的，
                //在JS中，它会被当成一个语句块来处理，所以
                //必须强制性的将它转换成一种表达式
                $.each(json, function(index, val){
                    item = $('<a class="show-toolkit group-item"></a>');
                    item.attr('group-id', val.id);
                    item.attr('href', "..."+val.id);
                    item.html(val.name);
                    item.appendTo(appendToWhat)
                });
                $.updateShowToolKit();
            })
    }

    /*
    * 显示头像
    * @param size， 默认为origin
    * */

})(jQuery);

