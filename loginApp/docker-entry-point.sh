#!/bin/bash


# Apply database migrations
echo "create database migrations"
python manage.py makemigrations

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate
