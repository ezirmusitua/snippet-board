-- DROP TABLE IF EXISTS snippet;
CREATE TABLE snippet(
   id          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
   link_hash   TEXT    NOT NULL,
   create_at   INTEGER,
   raw_content TEXT,
   create_by   TEXT
);

-- INSERT INTO snippet (link_hash, create_at, raw_content, create_by)
-- VALUES ('0dbeaf4d8c0d88aa095b5deee78998fc21081b9d', 1492616636890, 'Date: 2017-4-19[23:44]\nContent:\n组织你的项目', 'jferroal');

CREATE TABLE download_task(
   id           INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
   title        TEXT    NOT NULL,
   create_at    INTEGER,
   create_by    TEXT,
   download_id  TEXT,
   download_uri TEXT
);

-- SELECT * from snippet WHERE create_by = 'jferroal';
