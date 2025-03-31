-- PERSONAL_INFO TABLE
CREATE TABLE public.personal_info (
    info_id SERIAL PRIMARY KEY,
    full_name VARCHAR(100),
    bio TEXT,
    location VARCHAR(100),
    email VARCHAR(100),
    picture TEXT
);

-- PROJECTS TABLE
CREATE TABLE public.projects (
    project_id SERIAL PRIMARY KEY,
    project_name VARCHAR(200) NOT NULL,
    demo_url TEXT,
    image TEXT,
    description TEXT
);

-- USERS TABLE
CREATE TABLE public.users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100)
);

-- Insert Paddington into personal_info
INSERT INTO public.personal_info (full_name, bio, location, email, picture) VALUES
(
    'Paddington Bear',
    'A well-mannered bear from Darkest Peru, fond of marmalade sandwiches and adventures.',
    'Darkest Peru',
    'paddington@bearmail.com',
    "https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Paddington_Bear%2C_all_alone_%2850285504591%29.jpg/1280px-Paddington_Bear%2C_all_alone_%2850285504591%29.jpg"
);

-- Insert Paddington as a user
INSERT INTO public.users (username, password, email) VALUES
(
    'paddington',
    'marmalade123',  -- In real apps, this would be hashed!
    'paddington@bearmail.com'
);

-- Insert some projects Paddington might work on
INSERT INTO public.projects (project_name, demo_url, image, description) VALUES
(
    'Marmalade Maker 3000',
    'https://paddington.io/demo/marmalade',
    'https://placehold.co/600x400/EEE/31343C',
    'A delightful web app to craft and share homemade marmalade recipes.'
),
(
    'Peru Travel Guide',
    'https://paddington.io/demo/peru-guide',
    'https://placehold.co/600x400/EEE/31343C',
    'An interactive guide to the sights, sounds, and snacks of Darkest Peru.'
);
