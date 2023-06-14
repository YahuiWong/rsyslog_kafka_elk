import logging
import logging.config
import os
import socket
from logging.handlers import SysLogHandler

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEBUG = True  # 标记是否在开发环境

LOGGING = {
    # 基本设置
    'version': 1,  # 日志级别
    'disable_existing_loggers': False,  # 是否禁用现有的记录器

    # 日志格式集合
    'formatters': {
        # 标准输出格式
        'rsyslog': {
            # [具体时间][线程名:线程ID][日志名字:日志级别名称(日志级别ID)] [输出的模块:输出的函数]:日志内容
            'format': '[%(name)s][%(asctime)s][%(threadName)s:%(thread)d][%(name)s:%(levelname)s(%(lineno)d)][%('
                      'module)s:%(funcName)s]:%(message)s '
        }
    },

    # 处理器集合
    'handlers': {
        # 输出到控制台
        'console': {
            'level': 'DEBUG',  # 输出信息的最低级别
            'class': 'logging.StreamHandler',
            'formatter': 'rsyslog',  # 使用standard格式
        },
        # 输出到rsyslog
        'rsyslog': {
            'class': 'logging.handlers.SysLogHandler',
            'address': ("127.0.0.1", 514,),
            'facility': logging.handlers.SysLogHandler.LOG_UUCP,
            'formatter': 'rsyslog',
            'socktype': socket.SOCK_DGRAM,
            # 'socktype': socket.SOCK_STREAM,
        },
    },

    # 日志管理器集合
    'loggers': {
        # 管理器
        'default': {
            'handlers': ['console', 'rsyslog'],
            'level': 'DEBUG',
            'propagate': True,  # 是否传递给父记录器
        },
    }
}


def log_main():
    # 加载前面的标准配置
    logging.config.dictConfig(LOGGING)

    # 获取loggers其中的一个日志管理器
    new_logger = logging.getLogger("default")
    return new_logger


logger = log_main()
logger.debug('文件debug？ ')
logger.info('汉字information')
logger.warning('this is warning message')
logger.error('this is error message')
logger.fatal('this is fatal message, it is same as logger.critical')
logger.critical('this is critical message')