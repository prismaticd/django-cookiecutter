$(document).ready(function () {
    var burger = document.querySelector('.navbar-burger');
    var menu = document.querySelector('.navbar-menu');
    burger.addEventListener('click', function() {
        burger.classList.toggle('is-active');
        menu.classList.toggle('is-active');
    });

  var saveButton = document.getElementById("saveButtonProfile")
  if (saveButton) {
    saveButton.addEventListener("click", function () {
        if (!document.getElementsByTagName("fieldset")[0].disabled)
          document.getElementById('userProfileForm').submit()
      });
  }
  var editButton = document.getElementById("editButtonProfile")
  if (editButton) {
    editButton.addEventListener("click", function () {
      document.getElementsByTagName("fieldset")[0].disabled = !document.getElementsByTagName("fieldset")[0].disabled;
    });
  }

  /* -----------------
  Messages - dismissal
  ------------------- */
  var messageBox = $('.message-box .message');

  messageBox.find('.delete').on('click', function () {
    $(this).closest('.message').fadeOut();
  });

});