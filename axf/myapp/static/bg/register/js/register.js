$(function () {
    $("#btn").click(function () {
        //先获取用户输入数据
        var email = $("#email").val();
        var pwd = $("#pwd").val();
        var pwd_confirm = $("#pwd_confirm").val();
        //判断用户输入数据格式
        if (email.length <= 3){
            alert("邮箱不正确")
        }
        if (pwd.length < 3){
            alert("密码太短")
        }
        if (pwd_confirm != pwd){
            alert("两次密码不匹配")
        }
        //加密
        //发送请求
        $.ajax({
            url:"/api/register",
            method:"post",
            data:{
                email:email,
                pwd:md5(pwd),
                pwd_confirm:md5(pwd_confirm)
            },
            success:function (res) {
                if(res.code==1){
                    //注册成功，跳转
                    window.open(res.data,target="_self");
                }else{
                    alert(res.msg);
                }
            }
            
        })

    })
})