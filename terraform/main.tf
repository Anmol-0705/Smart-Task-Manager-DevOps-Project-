terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "3.0.2"
    }
  }
}

provider "docker" {}

resource "docker_image" "app_image" {
  name = "docker-app:latest"
}

resource "docker_container" "app_container" {
  name  = "smart-task-manager-container"
  image = docker_image.app_image.name

  ports {
    internal = 5000
    external = 5000
  }
}