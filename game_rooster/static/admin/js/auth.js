$('auth-button').click(
    function() {
        let email = $('#email').val();
        let password = $('#password')
        const CSRF = $('[name=csrfmiddlewaretoken]').val();

        if(!email) {
            alert('введите адрес электронной почты!')
        }

        if(!password) {
            alert('введите пороль');
        }

        let userData = {
            'email' : email,
            'password' : password,
            'csrfmiddlewaretoken' : CSRF
        }

        $.ajax({
            uri: '/auth/',
            type: 'POST',
            dataType: 'json',
            data: userData,
        });
    }
);