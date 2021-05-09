

































from __future__ import with_statement

import sys
import codecs
from datetime import datetime
from os.path import dirname, basename, splitext, join

import sqlite3 as sqlite

try:
    import simstring
except ImportError:
    errorstr = 
    print >> sys.stderr, errorstr
    sys.exit(1)


DEFAULT_INPUT_ENCODING = 'UTF-8'



NORM_DB_STRING = 'NORM_DB_VERSION'
NORM_DB_VERSION = '1.0.1'


SQL_DB_FILENAME_EXTENSION = 'db'


SS_DB_FILENAME_EXTENSION = 'ss.db'


DEFAULT_NGRAM_LENGTH = 3


DEFAULT_INCLUDE_MARKS = False


MAX_ERROR_LINES = 100


TYPE_VALUES = ["n"a"m"e"","" 
CREATE TABLE entities (
  id INTEGER PRIMARY KEY,
  uid VARCHAR(255) UNIQUE
);

CREATE TABLE labels (
  id INTEGER PRIMARY KEY,
  text VARCHAR(255)
);

CREATE TABLE names (
  id INTEGER PRIMARY KEY,
  entity_id INTEGER REFERENCES entities (id),
  label_id INTEGER REFERENCES labels (id),
  value VARCHAR(255),
  normvalue VARCHAR(255)
);

CREATE TABLE attributes (
  id INTEGER PRIMARY KEY,
  entity_id INTEGER REFERENCES entities (id),
  label_id INTEGER REFERENCES labels (id),
  value VARCHAR(255),
  normvalue VARCHAR(255)
);

CREATE TABLE infos (
  id INTEGER PRIMARY KEY,
  entity_id INTEGER REFERENCES entities (id),
  label_id INTEGER REFERENCES labels (id),
  value VARCHAR(255)
);

SELECT DISTINCT(normvalue) FROM names
UNION 
SELECT DISTINCT(normvalue) from attributes;
