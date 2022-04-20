import logging

from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger(__name__)


class CloseCsrfMiddleware(MiddlewareMixin):

    def process_request(self, request):
        request.csrf_processing_done = True  # csrf处理完毕
        logger.info('csrf全局禁用')
