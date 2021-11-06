function startFun() {

    var inputPhone = $("#loginName")
      , passWord = $("input[name=password]")
      , loginBtn = $("#loginBtn")
      , loginPush = $(".submit-btn");

    if (loginBtn.val()) {
		addJs() // 

      inputPhone.val("xxxxxxxx")
      passWord.val("xxxxxxx")

      //  监听到拖动完成 点击登录
      window.addEventListener("dragOk", function (params) {
        loginBtn.click()
      })

    }

    loginPush.find("span").click() //某某跳转
  }
