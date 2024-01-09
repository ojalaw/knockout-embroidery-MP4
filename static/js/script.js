function addToBasket(productId) {
    console.log('clicked!')
    var quantity = document.getElementById(`quantity_${productId}`).value;
    $.ajax({
        url: `/add_to_basket/${productId}/`,
        type: 'POST',
        data: {
            'csrfmiddlewaretoken': document.getElementsByName('csrfmiddlewaretoken')[0].value,
            'quantity': quantity
        },
        success: function(response) {
            if (response.success) {
                alert(response.message);
            }
        }
         
    });
}