
(function($) {
    $(function() {
        var selectField = $('#id_parent');
            secret = $('.field-secret');

        function toggleVerified(value) {
            if (value === '') {
                secret.show();
        	}
            else {
                secret.hide();
        	}
        }

        // show/hide on load based on previous value of selectField
        toggleVerified(selectField.val());

        // show/hide on change
        selectField.change(function() {
            toggleVerified($(this).val());
        });
    });
})(django.jQuery);