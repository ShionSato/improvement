import logging.config
from ast_processor import AstProcessor
from basic_info_listener import BasicInfoListener


if __name__ == '__main__':
    logging_setting_path = '../resources/logging/utiltools_log.conf'
    logging.config.fileConfig(logging_setting_path)
    logger = logging.getLogger(__file__)

    target_file_path = 'TourInfoServiceImpl.java'

    ast_info = AstProcessor(logging, BasicInfoListener()).execute(target_file_path)
