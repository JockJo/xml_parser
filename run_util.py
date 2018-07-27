# -*- coding: utf-8 -*-
import zip_util

if __name__ == '__main__':
    zip_rootdir = r'/media/jockjo/data/textual_parser/zip'
    zip_target_path = r'/media/jockjo/data/textual_parser/parser'
    zip_finish_path = r'/media/jockjo/data/textual_parser/zip_finish'
    z = zip_util.ZIPUTIL(zip_rootdir,zip_target_path,zip_finish_path)

    z.parse_zip()
