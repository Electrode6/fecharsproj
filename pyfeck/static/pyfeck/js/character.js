/**
 * Created by octo on 23-May-16.
 */

$(document).on('change', 'input:radio[id^="op_"]', function (event) {
    window.location.replace(event.target.value);
})

$(document).ready(function (){
    $("#ex8").slider({
    tooltip: 'always'
    });

});

// var slider = new Slider(document.getElementById('ex8'));

