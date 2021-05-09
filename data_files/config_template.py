






















ADMIN_CONTACT_EMAIL = CHANGE_ME







BASE_DIR = CHANGE_ME
DATA_DIR = CHANGE_ME
WORK_DIR = CHANGE_ME




















USER_PASSWORD = {

}

















MAX_SEARCH_RESULT_NUMBER = 1000





DEBUG = False



TUTORIALS = False





LL_DEBUG, LL_INFO, LL_WARNING, LL_ERROR, LL_CRITICAL = range(5)
LOG_LEVEL = LL_WARNING








try:
    assert DATA_DIR != BACKUP_DIR, 'DATA_DIR cannot equal BACKUP_DIR'
except NameError:
    pass 















