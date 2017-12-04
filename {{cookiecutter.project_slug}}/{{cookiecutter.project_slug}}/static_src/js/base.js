$(document).ready(function () {
    var burger = document.querySelector('.nav-toggle');
    var menu = document.querySelector('.nav-menu');
    burger.addEventListener('click', function() {
        burger.classList.toggle('is-active');
        menu.classList.toggle('is-active');
    });

  document.getElementById("saveButtonProfile").addEventListener("click", function () {
    if (!document.getElementsByTagName("fieldset")[0].disabled)
      document.getElementById('userProfileForm').submit()
  });
  document.getElementById("editButtonProfile").addEventListener("click", function () {
    document.getElementsByTagName("fieldset")[0].disabled = !document.getElementsByTagName("fieldset")[0].disabled;
  });

  /* -----------------
  Messages - dismissal
  ------------------- */
  var messageBox = $('.message-box .message');

  messageBox.find('.delete').on('click', function () {
    $(this).closest('.message').fadeOut();
  });

});