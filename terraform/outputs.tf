output "resource_group" {
  value = azurerm_resource_group.main.name
}

output "api_url" {
  value = "https://${azurerm_container_app.api.ingress[0].fqdn}"
}
