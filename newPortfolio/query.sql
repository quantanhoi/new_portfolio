-- Drop tables if they exist
DROP TABLE IF EXISTS skill;
DROP TABLE IF EXISTS project;
DROP TABLE IF EXISTS contact;
DROP TABLE IF EXISTS newspapers;
DROP TABLE IF EXISTS topics;
-- Create skill table
CREATE TABLE skill (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255)
);

-- Create project table
CREATE TABLE project (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  url VARCHAR(255),
  icon VARCHAR(2083)
);

-- Create contact table
CREATE TABLE contact (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  detail VARCHAR(255)
);


CREATE TABLE topics (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL
);

-- Optionally, create an index on the 'name' field for the 'topics' table
CREATE INDEX idx_topics_name ON topics (name);

-- Create the 'newspapers' table
CREATE TABLE newspapers (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    url TEXT NOT NULL,
    topic varchar(255) NOT NULL,
    FOREIGN KEY (topic) REFERENCES topics (name) ON DELETE SET NULL
);

INSERT INTO skill (name) VALUES
('C/C++'),
('Javascript'),
('Node.js'),
('HTML, CSS'),
('Python'),
('Postgresql'),
('Jira, Trello');

INSERT INTO project (name, url, icon) VALUES
('URL Alias Store', 'https://github.com/quantanhoi/url_alias_store', 'https://cdn.discordapp.com/attachments/695104338078597133/1153431888585834496/url.png'),
('4x4 Gewinnt on Raspberry Pi', 'https://github.com/quantanhoi/4x4_gewinnt_mit_CoAp', 'https://cdn.discordapp.com/attachments/695104338078597133/1153431875642212393/4x4_gewinnt.png'),
('Recipe Book API', 'https://github.com/quantanhoi/Recipe_Book_API', 'https://cdn.discordapp.com/attachments/695104338078597133/1153431899428094103/verteiltes_system.png');

INSERT INTO contact (name, detail) VALUES
('Mobile', '+49 1794159439'),
('Email', 'thieuquangtrung1999@gmail.com'),
('Facebook', 'https://www.facebook.com/thieuquang.trung.9'),
('Github', 'https://github.com/quantanhoi');