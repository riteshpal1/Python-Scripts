-- SQLite
CREATE TABLE todo (
  id INTEGER PRIMARY KEY,
  title TEXT,
  description TEXT,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
