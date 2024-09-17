document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, options);
  });

  document.addEventListener('DOMContentLoaded', function() {
    // initialize modal
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems, {
        dismissible: true, // Modal can be dismissed by clicking outside of it
        onCloseEnd: function(modal) {
            // Automatically close modal on another open
            // prevents multiple modals from opening
            if (document.getElementsByClassName('modal open').length > 0) {
                var openedModal = document.getElementsByClassName('modal open')[0];
                var instance = M.Modal.getInstance(openedModal);
                instance.close();
            }
        }
    });
});