
function user_login(){
	var username = $("#login_username").val()
	var password = $("#login_password").val()
	  $.post("http://127.0.0.1:5000/login",
	  {
	    username:username,
	    password:password
	  },
	  function(data,status){
	    alert("Data: " + data + "\nStatus: " + status);
	  });
}