


























from .constants import eStart, eError, eItsMe



BIG5_cls = (
    1,1,1,1,1,1,1,1,  
    1,1,1,1,1,1,0,0,  
    1,1,1,1,1,1,1,1,  
    1,1,1,0,1,1,1,1,  
    1,1,1,1,1,1,1,1,  
    1,1,1,1,1,1,1,1,  
    1,1,1,1,1,1,1,1,  
    1,1,1,1,1,1,1,1,  
    2,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,1,  
    4,4,4,4,4,4,4,4,  
    4,4,4,4,4,4,4,4,  
    4,4,4,4,4,4,4,4,  
    4,4,4,4,4,4,4,4,  
    4,3,3,3,3,3,3,3,  
    3,3,3,3,3,3,3,3,  
    3,3,3,3,3,3,3,3,  
    3,3,3,3,3,3,3,3,  
    3,3,3,3,3,3,3,3,  
    3,3,3,3,3,3,3,3,  
    3,3,3,3,3,3,3,3,  
    3,3,3,3,3,3,3,3,  
    3,3,3,3,3,3,3,3,  
    3,3,3,3,3,3,3,3,  
    3,3,3,3,3,3,3,3,  
    3,3,3,3,3,3,3,0  
)

BIG5_st = (
    eError,eStart,eStart,     3,eError,eError,eError,eError,
    eError,eError,eItsMe,eItsMe,eItsMe,eItsMe,eItsMe,eError,
    eError,eStart,eStart,eStart,eStart,eStart,eStart,eStart
)

Big5CharLenTable = (0, 1, 1, 2, 0)

Big5SMModel = {'classTable': BIG5_cls,
               'classFactor': 5,
               'stateTable': BIG5_st,
               'charLenTable': Big5CharLenTable,
               'name': 'Big5'}



EUCJP_cls = (
    4,4,4,4,4,4,4,4,  
    4,4,4,4,4,4,5,5,  
    4,4,4,4,4,4,4,4,  
    4,4,4,5,4,4,4,4,  
    4,4,4,4,4,4,4,4,  
    4,4,4,4,4,4,4,4,  
    4,4,4,4,4,4,4,4,  
    4,4,4,4,4,4,4,4,  
    4,4,4,4,4,4,4,4,  
    4,4,4,4,4,4,4,4,  
    4,4,4,4,4,4,4,4,  
    4,4,4,4,4,4,4,4,  
    4,4,4,4,4,4,4,4,  
    4,4,4,4,4,4,4,4,  
    4,4,4,4,4,4,4,4,  
    4,4,4,4,4,4,4,4,  
    5,5,5,5,5,5,5,5,  
    5,5,5,5,5,5,1,3,  
    5,5,5,5,5,5,5,5,  
    5,5,5,5,5,5,5,5,  
    5,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,2,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,5  
)

EUCJP_st = (
          3,     4,     3,     5,eStart,eError,eError,eError,
     eError,eError,eError,eError,eItsMe,eItsMe,eItsMe,eItsMe,
     eItsMe,eItsMe,eStart,eError,eStart,eError,eError,eError,
     eError,eError,eStart,eError,eError,eError,     3,eError,
          3,eError,eError,eError,eStart,eStart,eStart,eStart
)

EUCJPCharLenTable = (2, 2, 2, 3, 1, 0)

EUCJPSMModel = {'classTable': EUCJP_cls,
                'classFactor': 6,
                'stateTable': EUCJP_st,
                'charLenTable': EUCJPCharLenTable,
                'name': 'EUC-JP'}



EUCKR_cls  = (
    1,1,1,1,1,1,1,1,  
    1,1,1,1,1,1,0,0,  
    1,1,1,1,1,1,1,1,  
    1,1,1,0,1,1,1,1,  
    1,1,1,1,1,1,1,1,  
    1,1,1,1,1,1,1,1,  
    1,1,1,1,1,1,1,1,  
    1,1,1,1,1,1,1,1,  
    1,1,1,1,1,1,1,1,  
    1,1,1,1,1,1,1,1,  
    1,1,1,1,1,1,1,1,  
    1,1,1,1,1,1,1,1,  
    1,1,1,1,1,1,1,1,  
    1,1,1,1,1,1,1,1,  
    1,1,1,1,1,1,1,1,  
    1,1,1,1,1,1,1,1,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,2,2,2,2,2,2,2,  
    2,2,2,2,2,3,3,3,  
    2,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,2,  
    2,3,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,0   
)

EUCKR_st = (
    eError,eStart,     3,eError,eError,eError,eError,eError,
    eItsMe,eItsMe,eItsMe,eItsMe,eError,eError,eStart,eStart 
)

EUCKRCharLenTable = (0, 1, 2, 0)

EUCKRSMModel = {'classTable': EUCKR_cls,
                'classFactor': 4,
                'stateTable': EUCKR_st,
                'charLenTable': EUCKRCharLenTable,
                'name': 'EUC-KR'}



EUCTW_cls = (
    2,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,0,0,  
    2,2,2,2,2,2,2,2,  
    2,2,2,0,2,2,2,2,  
    2,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,2,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,6,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,3,4,4,4,4,4,4,  
    5,5,1,1,1,1,1,1,  
    1,1,1,1,1,1,1,1,  
    1,1,1,1,1,1,1,1,  
    1,1,3,1,3,3,3,3,  
    3,3,3,3,3,3,3,3,  
    3,3,3,3,3,3,3,3,  
    3,3,3,3,3,3,3,3,  
    3,3,3,3,3,3,3,3,  
    3,3,3,3,3,3,3,3,  
    3,3,3,3,3,3,3,3,  
    3,3,3,3,3,3,3,0   
)

EUCTW_st = (
    eError,eError,eStart,     3,     3,     3,     4,eError,
    eError,eError,eError,eError,eError,eError,eItsMe,eItsMe,
    eItsMe,eItsMe,eItsMe,eItsMe,eItsMe,eError,eStart,eError,
    eStart,eStart,eStart,eError,eError,eError,eError,eError,
         5,eError,eError,eError,eStart,eError,eStart,eStart,
    eStart,eError,eStart,eStart,eStart,eStart,eStart,eStart 
)

EUCTWCharLenTable = (0, 0, 1, 2, 2, 2, 3)

EUCTWSMModel = {'classTable': EUCTW_cls,
                'classFactor': 7,
                'stateTable': EUCTW_st,
                'charLenTable': EUCTWCharLenTable,
                'name': 'x-euc-tw'}



GB2312_cls = (
    1,1,1,1,1,1,1,1,  
    1,1,1,1,1,1,0,0,  
    1,1,1,1,1,1,1,1,  
    1,1,1,0,1,1,1,1,  
    1,1,1,1,1,1,1,1,  
    1,1,1,1,1,1,1,1,  
    3,3,3,3,3,3,3,3,  
    3,3,1,1,1,1,1,1,  
    2,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,4,  
    5,6,6,6,6,6,6,6,  
    6,6,6,6,6,6,6,6,  
    6,6,6,6,6,6,6,6,  
    6,6,6,6,6,6,6,6,  
    6,6,6,6,6,6,6,6,  
    6,6,6,6,6,6,6,6,  
    6,6,6,6,6,6,6,6,  
    6,6,6,6,6,6,6,6,  
    6,6,6,6,6,6,6,6,  
    6,6,6,6,6,6,6,6,  
    6,6,6,6,6,6,6,6,  
    6,6,6,6,6,6,6,6,  
    6,6,6,6,6,6,6,6,  
    6,6,6,6,6,6,6,6,  
    6,6,6,6,6,6,6,6,  
    6,6,6,6,6,6,6,0   
)

GB2312_st = (
    eError,eStart,eStart,eStart,eStart,eStart,     3,eError,
    eError,eError,eError,eError,eError,eError,eItsMe,eItsMe,
    eItsMe,eItsMe,eItsMe,eItsMe,eItsMe,eError,eError,eStart,
         4,eError,eStart,eStart,eError,eError,eError,eError,
    eError,eError,     5,eError,eError,eError,eItsMe,eError,
    eError,eError,eStart,eStart,eStart,eStart,eStart,eStart 
)






GB2312CharLenTable = (0, 1, 1, 1, 1, 1, 2)

GB2312SMModel = {'classTable': GB2312_cls,
                  'classFactor': 7,
                  'stateTable': GB2312_st,
                  'charLenTable': GB2312CharLenTable,
                  'name': 'GB2312'}



SJIS_cls = (
    1,1,1,1,1,1,1,1,  
    1,1,1,1,1,1,0,0,  
    1,1,1,1,1,1,1,1,  
    1,1,1,0,1,1,1,1,  
    1,1,1,1,1,1,1,1,  
    1,1,1,1,1,1,1,1,  
    1,1,1,1,1,1,1,1,  
    1,1,1,1,1,1,1,1,  
    2,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,1,  
    3,3,3,3,3,3,3,3,  
    3,3,3,3,3,3,3,3,  
    3,3,3,3,3,3,3,3,  
    3,3,3,3,3,3,3,3,  
    
    
    2,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,2,  
    2,2,2,2,2,2,2,2,  
    3,3,3,3,3,3,3,3,  
    3,3,3,3,3,4,4,4,  
    4,4,4,4,4,4,4,4,  
    4,4,4,4,4,0,0,0   
)


SJIS_st = (
    eError,eStart,eStart,     3,eError,eError,eError,eError,
    eError,eError,eError,eError,eItsMe,eItsMe,eItsMe,eItsMe,
    eItsMe,eItsMe,eError,eError,eStart,eStart,eStart,eStart 
)

SJISCharLenTable = (0, 1, 1, 2, 0, 0)

SJISSMModel = {'classTable': SJIS_cls,
               'classFactor': 6,
               'stateTable': SJIS_st,
               'charLenTable': SJISCharLenTable,
               'name': 'Shift_JIS'}



UCS2BE_cls = (
    0,0,0,0,0,0,0,0,  
    0,0,1,0,0,2,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,3,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,3,3,3,3,3,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,4,5   
)

UCS2BE_st  = (
          5,     7,     7,eError,     4,     3,eError,eError,
     eError,eError,eError,eError,eItsMe,eItsMe,eItsMe,eItsMe,
     eItsMe,eItsMe,     6,     6,     6,     6,eError,eError,
          6,     6,     6,     6,     6,eItsMe,     6,     6,
          6,     6,     6,     6,     5,     7,     7,eError,
          5,     8,     6,     6,eError,     6,     6,     6,
          6,     6,     6,     6,eError,eError,eStart,eStart 
)

UCS2BECharLenTable = (2, 2, 2, 0, 2, 2)

UCS2BESMModel = {'classTable': UCS2BE_cls,
                 'classFactor': 6,
                 'stateTable': UCS2BE_st,
                 'charLenTable': UCS2BECharLenTable,
                 'name': 'UTF-16BE'}



UCS2LE_cls = (
    0,0,0,0,0,0,0,0,  
    0,0,1,0,0,2,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,3,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,3,3,3,3,3,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,0,0,  
    0,0,0,0,0,0,4,5   
)

UCS2LE_st = (
          6,     6,     7,     6,     4,     3,eError,eError,
     eError,eError,eError,eError,eItsMe,eItsMe,eItsMe,eItsMe,
     eItsMe,eItsMe,     5,     5,     5,eError,eItsMe,eError,
          5,     5,     5,eError,     5,eError,     6,     6,
          7,     6,     8,     8,     5,     5,     5,eError,
          5,     5,     5,eError,eError,eError,     5,     5,
          5,     5,     5,eError,     5,eError,eStart,eStart 
)

UCS2LECharLenTable = (2, 2, 2, 2, 2, 2)

UCS2LESMModel = {'classTable': UCS2LE_cls,
                 'classFactor': 6,
                 'stateTable': UCS2LE_st,
                 'charLenTable': UCS2LECharLenTable,
                 'name': 'UTF-16LE'}



UTF8_cls = (
    1,1,1,1,1,1,1,1,  
    1,1,1,1,1,1,0,0,  
    1,1,1,1,1,1,1,1,  
    1,1,1,0,1,1,1,1,  
    1,1,1,1,1,1,1,1,  
    1,1,1,1,1,1,1,1,  
    1,1,1,1,1,1,1,1,  
    1,1,1,1,1,1,1,1,  
    1,1,1,1,1,1,1,1,  
    1,1,1,1,1,1,1,1,  
    1,1,1,1,1,1,1,1,  
    1,1,1,1,1,1,1,1,  
    1,1,1,1,1,1,1,1,  
    1,1,1,1,1,1,1,1,  
    1,1,1,1,1,1,1,1,  
    1,1,1,1,1,1,1,1,  
    2,2,2,2,3,3,3,3,  
    4,4,4,4,4,4,4,4,  
    4,4,4,4,4,4,4,4,  
    4,4,4,4,4,4,4,4,  
    5,5,5,5,5,5,5,5,  
    5,5,5,5,5,5,5,5,  
    5,5,5,5,5,5,5,5,  
    5,5,5,5,5,5,5,5,  
    0,0,6,6,6,6,6,6,  
    6,6,6,6,6,6,6,6,  
    6,6,6,6,6,6,6,6,  
    6,6,6,6,6,6,6,6,  
    7,8,8,8,8,8,8,8,  
    8,8,8,8,8,9,8,8,  
    10,11,11,11,11,11,11,11,  
    12,13,13,13,14,15,0,0    
)

UTF8_st = (
    eError,eStart,eError,eError,eError,eError,     12,   10,
         9,     11,     8,     7,     6,     5,     4,    3,
    eError,eError,eError,eError,eError,eError,eError,eError,
    eError,eError,eError,eError,eError,eError,eError,eError,
    eItsMe,eItsMe,eItsMe,eItsMe,eItsMe,eItsMe,eItsMe,eItsMe,
    eItsMe,eItsMe,eItsMe,eItsMe,eItsMe,eItsMe,eItsMe,eItsMe,
    eError,eError,     5,     5,     5,     5,eError,eError,
    eError,eError,eError,eError,eError,eError,eError,eError,
    eError,eError,eError,     5,     5,     5,eError,eError,
    eError,eError,eError,eError,eError,eError,eError,eError,
    eError,eError,     7,     7,     7,     7,eError,eError,
    eError,eError,eError,eError,eError,eError,eError,eError,
    eError,eError,eError,eError,     7,     7,eError,eError,
    eError,eError,eError,eError,eError,eError,eError,eError,
    eError,eError,     9,     9,     9,     9,eError,eError,
    eError,eError,eError,eError,eError,eError,eError,eError,
    eError,eError,eError,eError,eError,     9,eError,eError,
    eError,eError,eError,eError,eError,eError,eError,eError,
    eError,eError,    12,    12,    12,    12,eError,eError,
    eError,eError,eError,eError,eError,eError,eError,eError,
    eError,eError,eError,eError,eError,    12,eError,eError,
    eError,eError,eError,eError,eError,eError,eError,eError,
    eError,eError,    12,    12,    12,eError,eError,eError,
    eError,eError,eError,eError,eError,eError,eError,eError,
    eError,eError,eStart,eStart,eStart,eStart,eError,eError,
    eError,eError,eError,eError,eError,eError,eError,eError 
)

UTF8CharLenTable = (0, 1, 0, 0, 0, 0, 2, 3, 3, 3, 4, 4, 5, 5, 6, 6)

UTF8SMModel = {'classTable': UTF8_cls,
               'classFactor': 16,
               'stateTable': UTF8_st,
               'charLenTable': UTF8CharLenTable,
               'name': 'UTF-8'}


