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
('URL Alias Store', 'https://github.com/quantanhoi/url_alias_store', 'https://cdn.discordapp.com/attachments/695104338078597133/1153431888585834496/url.png?ex=65f8a827&is=65e63327&hm=3cfacd5bc9a0806225c83571319313db3ceab83d21eacc7bd1ca8d53211b88be&'),
('4x4 Gewinnt on Raspberry Pi', 'https://github.com/quantanhoi/4x4_gewinnt_mit_CoAp', 'https://cdn.discordapp.com/attachments/695104338078597133/1153431875642212393/4x4_gewinnt.png?ex=65f8a824&is=65e63324&hm=d700041244fb08f5893303309b48b0a132287afb20b546b4448ecd71f44d9bbf&'),
('Recipe Book API', 'https://github.com/quantanhoi/Recipe_Book_API', 'https://cdn.discordapp.com/attachments/1168685873903177840/1216550025396490301/icons8-cookbook-100.png?ex=6600cb80&is=65ee5680&hm=23a9babb799901b458d5285f232df87ae083d098416045f766d303e7780fe33d&'),
('This Portfolio Website', 'https://github.com/quantanhoi/new_portfolio', 'https://cdn.discordapp.com/attachments/1168685873903177840/1216569340741288006/image.png?ex=6600dd7d&is=65ee687d&hm=49689f3811a45d9646fd43f9315062c38b3b72874f71aaa7f331f87bf2c1b06e&');

INSERT INTO contact (name, detail) VALUES
('Mobile', '+49 1794159439'),
('Email', 'thieuquangtrung1999@gmail.com'),
('Facebook', 'https://www.facebook.com/thieuquang.trung.9'),
('Github', 'https://github.com/quantanhoi');