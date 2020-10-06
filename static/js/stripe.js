
$(document).ready(function () {

    let stripe_pk = $("#id_stripe_public_key").text().slice(1, -1);
    let clientSecret = $("#id_client_secret").text().slice(1, -1);
    
    var stripe = Stripe(stripe_pk);
    var elements = stripe.elements();
    var style = {
        base: {
            color: '#666666',
            fontSmoothing: 'antialiased',
            fontSize: '16px',
            '::placeholder': {
                color: '#666666',
                fontSize: '16px',
            }
        },
        invalid: {
            color: '#dc3545',
            iconColor: '#dc3545'
        }
    };
    

    var card = elements.create("card")
    card.mount("#card-element");

    var form = document.getElementById('payment_form');
    console.log(form)
    
    card.addEventListener('change', function (event) {
        var errorDiv = document.getElementById('errorDiv');
        console.log(errorDiv)
        if (event.error) {
            var html = `
                <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                </span>
                <span>${event.error.message}</span>`;
            $(errorDiv).html(html);
        } else {
            errorDiv.innerHTML = '';
        }
    });

    form.addEventListener('submit', function(ev) {
        ev.preventDefault();
        stripe.createToken(card).then(function(result) {
            if (result.error) {
                // Inform the customer that there was an error.
                var errorElement = document.getElementById('errorDiv');
                errorElement.textContent = result.error.message;
            } else {
                var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
                var postData = {
                    'csrfmiddlewaretoken': csrfToken,
                    'client_secret': clientSecret,
                    'form': $('#payment_form').serialize(),
                    'token': result.token.id
                };
                var url = '/bag/checkout_process';

                $.post(url, postData).done(function() {
                    stripe.confirmCardPayment(clientSecret, {
                        payment_method: {
                            card: card,
                            billing_details: {
                                name: $.trim(form.first_name.value) + $.trim(form.last_name.value),
                                email: $.trim(form.email.value),
                                phone: $.trim(form.phone.value),
                                address:{
                                    city: $.trim(form.city.value),
                                    country: $.trim(form.country.value),
                                    line1: $.trim(form.address_line_1.value),
                                    line2: $.trim(form.address_line_2.value),
                                    }
                                }
                            }
                        })
                    }).then(function(result) {

                        title_holder.textContent = result.message;
                        $("#checkoutModal").modal("show")
                        order_confirmed_url = `/bag/order_success/${result.order.id}`
                        window.location.replace(order_confirmed_url);
                    });
                };
            })
        });
        
        
    });
