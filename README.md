# Color Grounds

## Goal

Color grounds is a web app to create Tailwind css color paletts by entering a color value, it will return to the user a total of 10 shades based on entry color. Output can be copy and paste into tailwind config file. Colours are customizable and palette can be saved by creating an account.

## Users

This project will target creative minds such us UI, graphic designers and frontend-developers

## Data

For this project I will use "TheColorAPI" by Josh Beckman

## Database Tables

1. Users
   (id, email, password, first_name, last_name)

2. Palettes
   (id, name, color_code, user_id)

3. Projects
   (id, name, public, user_id)

4. Palettes_projects
   (user_id, project_id, palette_id)
