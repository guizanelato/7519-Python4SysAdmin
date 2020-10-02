function addRow(){
	var row = $("<tr>")

	row.append($('<td><input type="text" class="w-50 form-control form-control-sm" id="username" aria-describedby="emailHelp" placeholder="Email"></td>'))
	   .append($('<td><input type="text" class="w-50 form-control form-control-sm" id="email" aria-describedby="usernameHelp" placeholder="Username"></td>'))
	   .append($('<td style="text-align: center"> <input class="form-check-input" type="checkbox" value="" id="isadmin" <label class="form-check-label" for="defaultCheck1"> </td>'))
           .append($('<td><a href="javascript:void(0)" onclick="formSubmit()" >add</a> <a href="">cancel</a></td>'));

	
	$("#users tbody").append(row)
	document.getElementById("addRowBtn").disabled= true

}

function getCheckBoxStatus(checkbox_id){
	if (document.getElementById(checkbox_id).checked == true){
		return "True"
	}
	else {
		return "False"
	}
}

function formSubmit(){
	var form = $('<form style:"position: absolute; width:0, height:0; opacity:0;display: none; visibility: hidden;" method="POST" action="/add/users">')

	form.append('<input type="hidden" name="email" value="' + document.getElementById("email").value + '">');
	form.append('<input type="hidden" name="username" value="' + document.getElementById("username").value + '">');
	form.append('<input type="hidden" name="is_admin" value="' + getCheckBoxStatus("isadmin") + '">');
	
	$("body").append(form);

	form.submit();

}

