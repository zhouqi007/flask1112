$(function () {
    //修改
    $(".btn-info").click(function () {
        // console.log("已经点击");
        $current_btn = $(this);
        var p_id = $current_btn.parents("tr").children("td").first().text();
        $.ajax({
            url:"/api/updates",
            method:"get",
            data:{
                "p_id":p_id
            },
            success:function (res) {
                if(res.code==1){
                    window.open(res.data,target="_self")
                }
            }
        })
    })

    //删除
    $(".btn-danger").click(function () {
        var p_id = $(this).attr("p_id");
        var $current_btn = $(this);
        $.ajax({
            url:"/api/updates",
            method:"delete",
            data:{
                "p_id":p_id
            },
            success:function (res) {
                if(res.code==1){
                    $current_btn.parents("tr").remove();
                }else{
                    alert(res.msg)
                }
            }
        })
    })
})