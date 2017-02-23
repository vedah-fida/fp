 $(document).ready(function() {
// initialize the select button
    $('select').material_select();
//submit complete_status form on the orders table
    $('#order_status').change(function(){
        $('#order_status_form').submit();
    });
//submit complete_status form on the orders table
    $('#customer_select').change(function(){
        $('#customer_form').submit();
    });

    $('#carpenter_select').change(function(){
        $('#carpenter_form').submit()
    });

//activate and initialize the datepicker
    $('.datepicker').pickadate({
        selectMonths: true, // Creates a dropdown to control month
        selectYears: 15, // Creates a dropdown of 15 years to control year
    });
 });
