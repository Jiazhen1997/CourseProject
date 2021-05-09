import os
import re
import io

top_dir = "/Users/bianjunyu/Desktop/NYU/2021Spring/DL/Project/Data/idf"

# 标识状态
S_INIT              = 0
S_SLASH             = 1
S_BLOCK_COMMENT     = 2
S_LINE_COMMENT      = 3
S_STR               = 4
S_STR_ESCAPE        = 5
S_DOT_1             = 6
S_DOT_2             = 7
S_DOT_BACK_1        = 8
S_DOT_BACK_2        = 9
S_DDOT_1            = 10
S_DDOT_2            = 11
S_DDOT_BACK_1       = 12
S_DDOT_BACK_2       = 13
S_DBLOCK_COMMENT    = 14

# 处理文件夹
def trim_dir(path):
    print("dir:" + path)
    for root, dirs, files in os.walk(path):
        print("***")
        print(files)
        for name in files:
            trim_file(os.path.join(root,name))

# 处理文件
def trim_file(path):
    print("file:" + path)
    if re.match(r".*?\.(py)$",path):
        print("process!")
    else:
        print("ignore")
        return

    bak_file = path + ".bak"
    try:
        os.rename(path,bak_file)
    except:
        print("bak exception -->" + bak_file)

    fp_src = open(bak_file)
    fp_dst = open(path,'w')
    cnt = 0

    state = S_INIT
    for line in fp_src.readlines():
        print("--> Processing %d row" %cnt)
        print(line)
        cnt += 1

        for c in line:
            # State INIT
            if state == S_INIT:
                if c == '\'':
                    state = S_DOT_1
                elif c == '#':
                    state = S_LINE_COMMENT
                elif c == '"':
                    state = S_DDOT_1
                else:
                    fp_dst.write(c)
            # State Double Dot:
            elif state == S_DDOT_1:
                if c == '"':
                    state = S_DDOT_2
                else:
                    fp_dst.write('"')
                    fp_dst.write(c)
                    # state = S_STR   
            # State Double Dot 2:
            elif state == S_DDOT_2:
                if c == '"':
                    state = S_DBLOCK_COMMENT
                else:
                    fp_dst.write('""')
                    fp_dst.write(c)  
            # State Double Block_comment state 
            elif state == S_DBLOCK_COMMENT:
                if c == '"':
                    state = S_DDOT_BACK_1
                else:
                    state = S_DBLOCK_COMMENT
            # state double dot_back_1
            elif state  == S_DDOT_BACK_1:
                if c == '"': 
                    state = S_DDOT_BACK_2
                else:
                    state = S_DBLOCK_COMMENT 
            # state double dot_back_2
            elif state  == S_DDOT_BACK_2:
                if c == '"': 
                    state = S_INIT
                else:
                    state = S_DBLOCK_COMMENT                        
            # State Dot:
            elif state == S_DOT_1:
                if c == '\'':
                    state = S_DOT_2
                else:
                    fp_dst.write('\'')
                    fp_dst.write(c)
                    state = S_INIT
            # State Dot2:
            elif state == S_DOT_2:
                if c == '\'':
                    state = S_BLOCK_COMMENT
                else:
                    fp_dst.write('\'\'')
                    fp_dst.write(c)
                    state = S_INIT
            # State Block_comment state 
            elif state == S_BLOCK_COMMENT:
                if c == '\'':
                    state = S_DOT_BACK_1
                else:
                    state = S_BLOCK_COMMENT
            # state dot_back_1
            elif state  == S_DOT_BACK_1:
                if c == '\'': 
                    state = S_DOT_BACK_2
                else:
                    state = S_BLOCK_COMMENT 
            # state dot_back_2
            elif state  == S_DOT_BACK_2:
                if c == '\'': 
                    state = S_INIT
                else:
                    state = S_BLOCK_COMMENT                 

            # state line comment
            elif state == S_LINE_COMMENT:
                if c == '\n':
                    state = S_INIT
                    fp_dst.write(c)
            # # state str
            # elif state == S_STR:
            #     if c =='\\':
            #         state = S_STR_ESCAPE
            #     elif c == '"':
            #         state = S_INIT
            #     fp_dst.write(c)
            # # state str_escape
            # elif state == S_STR_ESCAPE:
            #     state = S_STR
            #     fp_dst.write(c)

    fp_src.close()
    os.remove(bak_file)
    fp_dst.close()

trim_dir(top_dir)
