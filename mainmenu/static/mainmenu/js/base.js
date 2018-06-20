(function($) {
    $(function() {
        var selectField = $('#id_content_type'),
            image_gallery = $('.field-image_gallery');
            text = $('.field-text');
            text_header = $('.field-text_header');
            video = $('.field-video');
            video_path = $('.field-video_path');
            video_text_overlay = $('.field-video_text_overlay');
            video_text = $('.field-video_text');
            invert_content_view = $('.field-invert_content_view');
            text_position = $('.field-text_position');
            gradient_overlay = $('.field-overlay_image');
            thumbnail = $('.field-thumbnail');
            linksToCards = $('a[href="#/tab/inline_1/"]');
            gallery = $('a[href="#/tab/inline_0/"]');

        function toggleVerified(value) {
            if (value === '') {
                image_gallery.hide();
                text.hide();
                text_header.hide();
                video.hide();
                video_text_overlay.hide();
                video_text.hide();
                invert_content_view.hide();
                gallery.hide();
                text_position.hide();
                gradient_overlay.hide();
                thumbnail.hide();
                linksToCards.show();
                video_path.hide();
            }
            if (value === 'IMAGE_GALLERY') {
                image_gallery.show();
                gallery.show();
                text.hide();
                text_header.hide();
                video.hide();
                video_text_overlay.hide();
                video_text.hide();
                invert_content_view.hide();
                text_position.hide();
                gradient_overlay.hide();
                thumbnail.hide();
                linksToCards.show();
                video_path.hide();
            }
            if (value === 'TEXT') {
                text.show();
                text_header.show();
                image_gallery.hide();
                video.hide();
                video_text_overlay.hide();
                video_text.hide();
                invert_content_view.hide();
                gallery.hide();
                text_position.hide();
                gradient_overlay.hide();
                thumbnail.hide();
                linksToCards.show();
                video_path.hide();
            }
            if (value === 'TEXT_GALLERY') {
                text.show();
                text_header.show();
                image_gallery.show();
                gallery.show();
                invert_content_view.hide();
                video.hide();
                video_text_overlay.hide();
                video_text.hide();
                text_position.show();
                gradient_overlay.hide();
                thumbnail.hide();
                linksToCards.show();
                video_path.hide();
            }
            if (value === 'VIDEO') {
                video.show();
                image_gallery.hide();
                text.hide();
                text_header.hide();
                video_text_overlay.hide();
                video_text.hide();
                invert_content_view.hide();
                gallery.hide();
                text_position.hide();
                gradient_overlay.hide();
                thumbnail.show();
                linksToCards.show();
                video_path.hide();
            }
            if (value === 'VIDEO_TEXT') {
                text.show();
                text_header.show();
                video.show();
                invert_content_view.hide();
                image_gallery.hide();
                video_text_overlay.hide();
                gallery.hide();
                text_position.show();
                gradient_overlay.hide();
                thumbnail.show();
                linksToCards.show();
                video_path.hide();
            }
            if (value === 'VIDEO_TEXT_OVERLAY') {
                video.show();
                text.show();
                text_header.show();
                image_gallery.hide();
                video_text.hide();
                invert_content_view.hide();
                gallery.hide();
                text_position.show();
                gradient_overlay.show();
                thumbnail.show();
                linksToCards.show();
                video_path.hide();
            }
            if (value === 'STOCK CARD') {
                video.hide();
                text.hide();
                text_header.hide();
                image_gallery.hide();
                video_text.hide();
                invert_content_view.hide();
                gallery.hide();
                text_position.hide();
                gradient_overlay.hide();
                thumbnail.hide();
                linksToCards.show();
                video_path.hide();
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