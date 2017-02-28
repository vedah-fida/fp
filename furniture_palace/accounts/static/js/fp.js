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

//deposit functionality.
    $('#order_name_select').change(function(){

        $.getJSON(
            "/furniture_palace/catalog/get_furniture_price/",
            function(data){
                $.each(JSON.parse(data), function(key, value){
                   if (value.fields.furniture_name==$('#order_name_select').val()){
                        $('#price_per_item').val(value.fields.material_price*1.7);
                        return false;
                   }
                });
            }
        );
    });

    $('#quantity').keyup(function(){
        $('#deposit').val($('#price_per_item').val()*$('#quantity').val()*0.4);
        $('#total_price').text("Total amount: "+$("#price_per_item").val()*$('#quantity').val());
        $('#balance').text("Balance: "+(($("#price_per_item").val()*$('#quantity').val())-($('#price_per_item').val()*$('#quantity').val()*0.4)));
    });

    $('#deposit').keyup(function(){
        $('#balance').text("Balance: "+(($("#price_per_item").val()*$('#quantity').val())-($("#deposit").val())));
    });
 });