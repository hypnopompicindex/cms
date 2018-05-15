(function($) {
    $(function() {
        var selectField = $('#id_content_type'),
            image_gallery = $('.field-image_gallery');
            text = $('.field-text');
            video = $('.field-video');
            video_text_overlay = $('.field-video_text_overlay');
            video_text = $('.field-video_text');
            invert_content_view = $('.field-invert_content_view');
            gallery = $(".changeform-tabs-item").not(".selected");
            thumbnail = $('.field-thumbnail');

        function toggleVerified(value) {
            if (value === '') {
                image_gallery.hide();
                text.hide();
                video.hide();
                video_text_overlay.hide();
                video_text.hide();
                invert_content_view.hide();
                gallery.hide();
                thumbnail.hide();
            }
            if (value === 'IMAGE_GALLERY') {
                image_gallery.show();
                gallery.show();
                text.hide();
                video.hide();
                video_text_overlay.hide();
                video_text.hide();
                invert_content_view.hide();
                thumbnail.hide();
            }
            if (value === 'TEXT') {
                text.show();
                image_gallery.hide();
                video.hide();
                video_text_overlay.hide();
                video_text.hide();
                invert_content_view.hide();
                gallery.hide();
                thumbnail.hide();
            }
            if (value === 'TEXT_GALLERY') {
                text.show();
                image_gallery.show();
                gallery.show();
                invert_content_view.show();
                video.hide();
                video_text_overlay.hide();
                video_text.hide();
                thumbnail.hide();
            }
            if (value === 'VIDEO') {
                video.show();
                image_gallery.hide();
                text.hide();
                video_text_overlay.hide();
                video_text.hide();
                invert_content_view.hide();
                gallery.hide();
                thumbnail.show();
            }
            if (value === 'VIDEO_TEXT') {
                text.show();
                video.show();
                invert_content_view.show();
                image_gallery.hide();
                video_text_overlay.hide();
                gallery.hide();
                thumbnail.show();
            }
            if (value === 'VIDEO_TEXT_OVERLAY') {
                video.show();
                text.show();
                image_gallery.hide();
                video_text.hide();
                invert_content_view.hide();
                gallery.hide();
                thumbnail.show();
            }
        }

        // show/hide on load based on pervious value of selectField
        toggleVerified(selectField.val());

        // show/hide on change
        selectField.change(function() {
            toggleVerified($(this).val());
        });
    });
})(django.jQuery);