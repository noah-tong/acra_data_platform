output "resource_group_name" {
  description = "Name of the deployed resource group."
  value       = azurerm_resource_group.main.name
}

output "storage_account_name" {
  description = "Name of the ADLS Gen2 storage account."
  value       = azurerm_storage_account.main.name
}

output "storage_account_dfs_endpoint" {
  description = "Primary DFS endpoint for the storage account."
  value       = azurerm_storage_account.main.primary_dfs_endpoint
}

output "filesystem_name" {
  description = "Name of the ADLS Gen2 filesystem."
  value       = azurerm_storage_data_lake_gen2_filesystem.main.name
}

output "databricks_workspace_url" {
  description = "URL of the Azure Databricks workspace."
  value       = azurerm_databricks_workspace.main.workspace_url
}

output "databricks_workspace_id" {
  description = "Azure resource ID of the Databricks workspace."
  value       = azurerm_databricks_workspace.main.id
}

output "access_connector_id" {
  description = "Azure resource ID of the Databricks Access Connector."
  value       = azurerm_databricks_access_connector.main.id
}

output "managed_identity_principal_id" {
  description = "Principal ID of the Access Connector system-assigned managed identity."
  value       = azurerm_databricks_access_connector.main.identity[0].principal_id
}

output "key_vault_name" {
  description = "Name of the Azure Key Vault."
  value       = azurerm_key_vault.main.name
}

output "container_registry_login_server" {
  description = "Login server URL for the Azure Container Registry."
  value       = azurerm_container_registry.main.login_server
}
