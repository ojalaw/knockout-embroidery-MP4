
var basketCount = 0;

function addToBasket(productId) {

  $.ajax({
    url: '/basket/add/' + productId +'/',
    type: 'POST',
    success: function() {
      basketCount += 1; 
      
      $('#basket-count').text(basketCount); 

      showAlert('Added to basket!');
    }
  });

}

$('.remove-button').click(function() {

    var itemId = $(this).data('id')
  
    $.ajax({
      url: '/basket/remove/' + itemId + '/', 
      success: function() {
        
      }
    })
  
  })