
$(document).ready(function () {

    let stripe_pk = $("#id_stripe_public_key").text().slice(1, -1);
    let clientSecret = $("#id_client_secret").text().slice(1, -1);
    
    var stripe = Stripe(stripe_pk);
    var elements = stripe.elements();
    var style = {
        base: {
            color: '#666666',
            fontFamily: 'Philosopher, sans-serif',
            fontSmoothing: 'antialiased',
            fontSize: '16px',
            '::placeholder': {
                color: '#666666',
                fontFamily: 'Philosopher, sans-serif',
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
    
    
    card.addEventListener('change', function (event) {
        var errorDiv = document.getElementById('card-errors');
        if (event.error) {
            var html = `
                <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                </span>
                <span>${event.error.message}</span>`;
            $(errorDiv).html(html);
        } else {
            errorDiv.textContent = '';
        }
    });

    form.addEventListener('submit', function(ev) {
        ev.preventDefault();
        stripe.createToken(card).then(function(result) {
            if (result.error) {
            // Inform the customer that there was an error.
            var errorElement = document.getElementById('card-errors');
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
                                name: $.trim(form.firstname),
                                // email: $.trim(form.email.value),
                                // phone: $.trim(form.phone_number.value),
                                // address: {
                                //     line1: $.trim(form.street_address.value),
                                //     city: $.trim(form.town_or_city.value),
                                //     country: $.trim(form.country.value),
                                // }
                            }
                        }
                    }).then(function(result) {
                        if (result.error) {
                        // Show error to your customer (e.g., insufficient funds)
                        console.log(result.error.message);
                        } else {
                        // The payment has been processed!
                        if (result.paymentIntent.status === 'succeeded') {
                            // Show a success message to your customer
                            // There's a risk of the customer closing the window before callback
                            // execution. Set up a webhook or plugin to listen for the
                            // payment_intent.succeeded event that handles any business critical
                            // post-payment actions.
                                // console.log(result)
                                // location.reload()
                            }
                        }
                    });
                });
            }
        });

        
    
        
    });

});