DROP TABLE IF EXISTS snippet;
CREATE TABLE snippet(
   link_hash   TEXT     NOT NULL   PRIMARY KEY,
   create_at   INTEGER,
   raw_content TEXT,
   create_by   TEXT
);

INSERT INTO snippet (link_hash, create_at, raw_content, create_by)
VALUES ('0dbeaf4d8c0d88aa095b5deee78998fc21081b9d', 1492616636890, 'Date: 2017-4-19[23:44]\nContent:\n组织你的项目', 'jferroal');

SELECT * from snippet WHERE create_by = 'jferroal';
