from reviewboard.extensions.base import Extension
from reviewboard.extensions.hooks import ReviewUIHook
from reviewboard.extensions.hooks import FileAttachmentThumbnailHook
from reviewboard.attachments.mimetypes import TextMimetype
from reviewboard.reviews.ui.base import FileAttachmentReviewUI

class IpynbMimetype(TextMimetype):

    supported_mimetypes = ['application/ipynb', 'text/ipynb']

    def _generate_preview_html(self, data_string):
         return data_string


class IpynbReviewUIExtension(Extension):

    def initialize(self):
        ReviewUIHook(self, [IpynbReviewUI])
        FileAttachmentThumbnailHook(self, [IpynbMimetype])


class XMLReviewUI(FileAttachmentReviewUI):

    supported_mimetypes = IpynbMimetype.supported_mimetypes

    template_name = 'rbxmlreview/xml.html'
    object_key = 'ipynb'

    def render(self):

        return ''
