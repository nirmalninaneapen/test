$(document).ready(function() {
  $(".digit-input").inputFilter(function(value) {
    return /^\d*$/.test(value);    // Allow digits only, using a RegExp
  });
  $('.select-all').click(function() {
        $('#branches option').prop('selected', true);
    });
  $('.select-all-fooditem').click(function() {
        console.log('1');
        $('#fooditems option').prop('selected', true);
    });
  $('.select-all-branch').click(function() {
        console.log('2');
        $('#branches option').prop('selected', true);
    });
  $('.select-all-category').click(function() {
        console.log('3');
        $('#categories option').prop('selected', true);
    });

  $(".tohide").hide();
   $("#fooditemsformgroup").show();
  $("input[name$='selectInputMultiple']").click(function() {
        var test = $(this).val();
        $(".tohide").hide();
        $("#" + test + "formgroup").show();
    });
  $('.pass-checkbox').change(function(){
    if(this.checked){
        $('.pass-formgroup').fadeIn('slow');
    }else{
         $('.pass-formgroup').fadeOut('slow');
    }
  });
});

// Restricts input for the set of matched elements to the given inputFilter function.

(function($) {
  $.fn.inputFilter = function(inputFilter) {
    return this.on("input keydown keyup mousedown mouseup select contextmenu drop", function() {
      if (inputFilter(this.value)) {
        this.oldValue = this.value;
        this.oldSelectionStart = this.selectionStart;
        this.oldSelectionEnd = this.selectionEnd;
      } else if (this.hasOwnProperty("oldValue")) {
        this.value = this.oldValue;
        this.setSelectionRange(this.oldSelectionStart, this.oldSelectionEnd);
      } else {
        this.value = "";
      }
    });
  };
}(jQuery));

$(function(){
	$('.preventSpecialChar').keyup(function()
	{console.log('tf');
		var yourInput = $(this).val();
		re = /[`~!@#$%^&*()_|+\-=?;:'",.<>\{\}\[\]\\\/]/gi;
		var isSplChar = re.test(yourInput);
		if(isSplChar)
		{
			var no_spl_char = yourInput.replace(/[`~!@#$%^&*()_|+\-=?;:'",.<>\{\}\[\]\\\/]/gi, '');
			$(this).val(no_spl_char);
		}
	});
});

function readURL(input) {
  if (input.files && input.files[0]) {
    var reader = new FileReader();

    reader.onload = function(e) {
      $('#img-prev').attr('src', e.target.result);
      $("#img-prev").css("display", "block");
      $('#img-prev-edit').attr('src', e.target.result);
      $("#img-prev-edit").css("display", "block");
    }

    reader.readAsDataURL(input.files[0]);
  }
}

$("#id_image").change(function() {
  readURL(this);
});

function update(repo,id,name){
    if(repo=="branch"){
       url = "/app-admin/admin/" + repo + "/delete/" + id;
       $(".modalLink").attr("href", url);
       document.getElementById("modalPara").innerHTML = "Are you sure of removing the branch " + name + "?";
    }else if(repo=="category"){
       url = "/app-admin/admin/" + repo + "/delete/" + id;
       $(".modalLink").attr("href", url);
       document.getElementById("modalPara").innerHTML = "Are you sure of removing the category " + name + "?";
    }else if(repo=="offer"){
       url = "/app-admin/admin/" + repo + "/delete/" + id;
       $(".modalLink").attr("href", url);
       document.getElementById("modalPara").innerHTML = "Are you sure of removing the offer " + name + "?";
    }else if(repo=="fooditem"){
       url = "/app-admin/admin/" + repo + "/delete/" + id;
       $(".modalLink").attr("href", url);
       document.getElementById("modalPara").innerHTML = "Are you sure of removing the fooditem " + name + "?";
    }else if(repo=="branchuser"){
       url = "/app-admin/admin/" + repo + "/delete/" + id;
       $(".modalLink").attr("href", url);
       document.getElementById("modalPara").innerHTML = "Are you sure of removing the branchuser " + name + "?";
    }else if(repo=="deliveryboys"){
       url = "/app-admin/admin/" + repo + "/delete/" + id;
       $(".modalLink").attr("href", url);
       document.getElementById("modalPara").innerHTML = "Are you sure of removing the delivery boy " + name + "?";
    }else if(repo=="deliveryboysapprove"){
       url = "/app-admin/admin/deliveryboys/approve/" + id;
       $(".modalLink").attr("href", url);
       document.getElementById("modalPara").innerHTML = "Are you sure to approve the delivery boy " + name + "?";
    }else if(repo=="area"){
       url = "/app-admin/branch/" + repo + "/delete/" + id;
       $(".modalLink").attr("href", url);
       document.getElementById("modalPara").innerHTML = "Are you sure to remove area " + name + "?";
    }
 }
 function update1(repo,id,name){
   if(repo=="menu"){
        url = "/app-admin/branch/" + repo + "/delete/" + id;
        $(".modalLink").attr("href", url);
        document.getElementById("modalPara").innerHTML = "Sure of removing the item " + name + " from menulist?";
   } else if(repo=="coupon"){
        url = "/app-admin/branch/" + repo + "/delete/" + id;
        $(".modalLink").attr("href", url);
        document.getElementById("modalPara").innerHTML = "Sure of removing the coupon " + name + "?";
   }
 }
 function update2(repo,id,name){
   if(repo=="menu"){
        url = "/app-admin/admin/" + repo + "/delete/" + id;
        $(".modalLink").attr("href", url);
        document.getElementById("modalPara").innerHTML = "Sure of removing the item " + name + " from menulist?";
   } else if(repo=="coupon"){
        url = "/app-admin/admin/" + repo + "/delete/" + id;
        $(".modalLink").attr("href", url);
        document.getElementById("modalPara").innerHTML = "Sure of removing the coupon " + name + "?";
   }
 }
 function quantClick(id){
   $('.quantityShow' + id).hide();
   $('.quantityForm' + id).fadeIn('slow');
   $('.quantityButton' + id).hide();
   $('.quantUpdateButton' + id).show();
 }
 function quantUpdate(id){
   $('.updateQuantForm' + id).submit();
 }
 function toggleCustomerStatus(status,id,name){
    url = "/app-admin/admin/customer/update/" + id;
    $('#toggleCustomerStatusForm').attr('action', url);
    $("#customerStatusInput").val(status);
    if(status==0){
         $('#customerStatusInputProceedBtn').removeClass("btn-outline-success");
         $('#customerStatusInputProceedBtn').addClass("btn-outline-danger");
         document.getElementById('customerStatusInputProceedBtn').innerHTML = "Block";
         document.getElementById("modalPara").innerHTML = "Sure of blocking the customer " + name + "?";
    }else if(status==1){
        document.getElementById('customerStatusInputProceedBtn').innerHTML = "Activate";
        document.getElementById("modalPara").innerHTML = "Sure of activating the customer " + name + "?";
    }
 }










