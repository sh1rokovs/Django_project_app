'use strict';

window.onload = function () {
    console.log('DOM ready');
    let basketList = $('.basket_list')
    basketList.on('change', 'input[type=number].product_input', function (event){
        console.log(event.target);
        $.ajax({
            url: '/basket/change/' + event.target.name + '/quantity/' + event.target.value + '/',
            success: function (data) {
                // console.log(data)
                basketList.html(data.basket_items);
            }
        })
    })
}