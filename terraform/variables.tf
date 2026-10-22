variable "resource_group_name" {
  type    = string
  default = "rg-connected-vehicle-lab"
}

variable "location" {
  type    = string
  default = "canadacentral"
}

variable "name" {
  type    = string
  default = "connected-vehicle-lab"
}

variable "api_image" {
  type        = string
  description = "Container registry image, e.g. myregistry.azurecr.io/vehicle-api:latest"
}
