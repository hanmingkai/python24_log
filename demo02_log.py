

#导入
from loguru import logger


#输出日志到文件
#logger.add('文件名',格式化，级别)
logger.add('a.log',format="{time}{level}{message}",level='DEBUG')

logger.debug(' debug')
logger.info(' info')
