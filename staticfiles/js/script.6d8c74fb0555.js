function handleSpinners(input) {
    var value = parseInt($(input).val());
    
    var minReached = value <= 1;
  
    $(input).closest('.input-group')
             .find('.decrement-qty')
             .prop('disabled', minReached);
  
  }
  
  // Increment quantity
  $('.increment-qty').click(function(e) {
    e.preventDefault();
    
    var input = $(this).closest('.input-group').find('.qty_input');
    var value = parseInt($(input).val()); 
    
    $(input).val(value + 1);
    
    handleSpinners(input);
  });
  
  // Decrement quantity 
  $('.decrement-qty').click(function(e) {
    e.preventDefault();
  
    var input = $(this).closest('.input-group').find('.qty_input');
    var value = parseInt($(input).val());
  
    $(input).val(value - 1);
    
    handleSpinners(input);  
  });
  
  
  // Check on change as well
  $('.qty_input').change(function() {  
    handleSpinners(this);
  });

  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.toast .close').forEach(function(closeButton) {
        closeButton.addEventListener('click', function () {
            this.closest('.toast').remove();
        });
    });
});