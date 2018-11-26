$(function () {
    $("select").change(function () {
        var $current=$(this);
        var statu = $current.find("option:selected").attr("value");
        var o_id = $current.attr("o_id");
        $.ajax({
            url:"/api/statu_update",
            method:"patch",
            data:{
                "statu":statu,
                "o_id":o_id
            },
            success:function (res) {
                if(res.code==1){
                    //修改显示的订单状态
                    $current.parents("tr").find(".o_statu").html(res.data)
                }
            }
        })
    })
})

