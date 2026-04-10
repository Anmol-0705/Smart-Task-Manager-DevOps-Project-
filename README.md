# Smart Task Manager
# Smart Task Manager

A simple REST API task manager built with Flask and DevOps practices.

## Features
- Create task
- Get all tasks
- Mark task complete

## Git Workflow
- main → production
- develop → integration
- feature/* → new features

## Example Commit Messages
- feat: add create task API
- fix: correct task completion bug

## Pull Request Example
Title: Add task completion feature  
Description: Implements PUT endpoint to mark tasks complete.

---

## Run Locally with Docker

```bash
cd docker
docker-compose up --build