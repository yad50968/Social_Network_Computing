var id = 1; // unique id for list items

$(document).ready(function(e) {
	
	// click the remove 
	$("tbody").on("click", ".cross", function() {
		$(this).closest("tr").remove();
	});

	// click the itme 
	$("tbody").on("click", ".content", function() {
		var tdObj = $(this); 
	 	var text = tdObj.text();
	 	var inputObj = $("<input type='text' />"); 
	 	inputObj.val(tdObj.text());  
	    tdObj.html(""); 

	    // click the item 
	    // and append a input on origin span
	    // user can edit the content
	    inputObj.appendTo(tdObj);  
	    inputObj.trigger("focus").trigger("select");
	    inputObj.click(function() { 
			return false; 
		});
		inputObj.keyup(function(event) { 
			var keycode = event.which; 
			if (keycode == 13) { 
				var inputtext = $(this).val();
				tdObj.text(inputtext); 
			}
			if (keycode == 27) { 
				tdObj.html(text); 
			}
		}); 
 
	});

	// click the add
	$("#add").on("click", getInput);

	// click the delete all
	$("#deleteall").on("click", deleteall);

	$("tbody").on("click", ".box", function() {
		$(this).closest("tr").find("span").toggleClass("checked");
	});

	$()

});

// triggered on Enter
$(document).on("keydown", function(e) {
	if(e.keyCode === 13) {
		getInput();
	}
});




// Toggle delete icon when edit button is clicked

function deleteall() {
	id = 0;
	$("tbody").empty();

};

// Obtaining customer input and then calling addItem() with the input
function getInput() {
	var custInput = $(".custinput");
	var input = custInput.val();

	if ((input !== "") && ($.trim(input) !== "")) {
		addItem(input);
		custInput.val("");
	}
}


/******************************************************************************
	adding item to the list
	increment id counter for unique id
*******************************************************************************/
function addItem(message) {

	var d = new Date();
	var d_string =  d.getFullYear() + "/" + (d.getMonth()+1) + "/" + d.getDate();
	var checkbox = "<td class=\"check\">" + "<input type=\"checkbox\" id=\"item" + id + "\" class=\"box\">" + "<label for=\"item" + id + "\" class=\"check-label\"></label></td>";

	var content = "<td class=\"content\"><span>" + message + "</span></td>";

	var delIcon = "<td><img src=\"img/cross.png\" alt=\"cross\" class=\"cross\"></td>";

	var datetime = "<td class=\"date\"><span>" + d_string + "</span></td>";
	$("tbody").append("<tr>" + checkbox + content + datetime +delIcon  + "</tr>");
	$(".cross").show();
	id++;
}