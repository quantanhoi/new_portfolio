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
('URL Alias Store', 'https://github.com/quantanhoi/url_alias_store', 'url_alias_store.png'),
('4x4 Gewinnt on Raspberry Pi', 'https://github.com/quantanhoi/4x4_gewinnt_mit_CoAp', '4x4_gewinnt.png'),
('Recipe Book API', 'https://github.com/quantanhoi/Recipe_Book_API', 'rezept_buch.png'),
('This Portfolio Website', 'https://github.com/quantanhoi/new_portfolio', 'portfolio.png');

INSERT INTO contact (name, detail) VALUES
('Mobile', '+49 1794159439'),
('Email', 'thieuquangtrung1999@gmail.com'),
('Facebook', 'https://www.facebook.com/thieuquang.trung.9'),
('Github', 'https://github.com/quantanhoi');

INSERT INTO topics VALUES (1, 'Code');
INSERT INTO topics VALUES (2, 'AI');
INSERT INTO topics VALUES (3, 'Technology');
INSERT INTO topics VALUES (5, 'Industry');
INSERT INTO topics VALUES (6, 'Science');
INSERT INTO topics VALUES (7, 'Economy');
INSERT INTO newspapers VALUES (1, 'Simple REST API using Flask and Peewee', 'https://medium.com/@prabhath_kiran/simple-rest-api-using-flask-and-peewee-3d75c7bff515', 'Code');
INSERT INTO newspapers VALUES (2, 'penAI wants to make a walking, talking humanoid robot smarter', 'https://www.popsci.com/technology/openai-wants-to-make-a-walking-talking-humanoid-robot-smarter/', 'AI');
INSERT INTO newspapers VALUES (3, 'High-speed humanoid feels like a step change in robotics', 'https://newatlas.com/robotics/sanctuary-phoenix-autonomous-speed-hands/', 'AI');
INSERT INTO newspapers VALUES (4, 'How to Build AWS-Compatible APIs: AWS Sigv4', 'https://www.aspiring.dev/building-aws-sigv4-into-your-app/', 'Code');
INSERT INTO newspapers VALUES (5, 'HTTP Response Status Code', 'https://developer.mozilla.org/en-US/docs/Web/HTTP/Status', 'Code');
INSERT INTO newspapers VALUES (6, 'Getting Started with Python and Flask on MacOS', 'https://gist.github.com/dineshviswanath/af72af0ae2031cd9949f', 'Code');
INSERT INTO newspapers VALUES (7, 'Adobe''s New Prototype Generative AI Tool', 'https://www.theverge.com/2024/2/28/24085551/adobe-project-music-genai-control-prototype-tool-hot-pod', 'AI');
INSERT INTO newspapers VALUES (8, 'Tesla Footage Optimus Walking', 'https://www.teslarati.com/tesla-footage-optimus-walking/?utm_source=tldrnewsletter', 'Technology');
INSERT INTO newspapers VALUES (9, 'Test flights on tap for Space Perspective’s luxury high-altitude balloon', 'https://arstechnica.com/space/2024/02/test-flights-on-tap-for-space-perspectives-luxury-high-altitude-balloon/?utm_source=tldrnewsletter', 'Technology');
INSERT INTO newspapers VALUES (10, 'Creating API with Python and Flask', 'https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask', 'Code');
INSERT INTO newspapers VALUES (11, 'The next Starship mission has a tentative launch date: March 14', 'https://arstechnica.com/space/2024/03/the-next-starship-mission-has-a-tentative-launch-date-march-14/', 'Technology');
INSERT INTO newspapers VALUES (12, 'Apple terminates Epic Games developer account calling it a ‘threat’ to the iOS ecosystem', 'https://www.techcrunch.com/2024/03/06/apple-terminates-epic-games-developer-account-calling-it-a-threat-to-the-ios-ecosystem/', 'Industry');
INSERT INTO newspapers VALUES (13, 'Company that plans to bring back the mammoth takes a key step', 'https://arstechnica.com/science/2024/03/de-extinction-company-manages-to-generate-first-elephant-stem-cells/', 'Science');
INSERT INTO newspapers VALUES (14, 'Stadt Frankfurt ermöglicht 14 neue Hochhäuser', 'https://www.hessenschau.de/wirtschaft/stadt-frankfurt-ermoeglicht-14-neue-hochhaeuser-v1,hochhaus-entwicklung-frankfurt-100.html', 'Economy');
INSERT INTO newspapers VALUES (15, 'Angeblicher Tesla-Hack mit Flipper Zero entpuppt sich als Sturm im Wasserglas', 'https://www.heise.de/news/Angeblicher-Tesla-Hack-mit-Flipper-Zero-entpuppt-sich-als-Sturm-im-Wasserglas-9650018.html', 'Technology');


