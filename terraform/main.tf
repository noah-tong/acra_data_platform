data "azurerm_client_config" "current" {}

locals {
  tags = {
    project     = var.project_name
    environment = var.environment
    managed_by  = "terraform"
  }
}

# 1. Resource Group
resource "azurerm_resource_group" "main" {
  name     = var.resource_group_name
  location = var.location
  tags     = local.tags
}

# 2. Storage Account (ADLS Gen2)
resource "azurerm_storage_account" "main" {
  name                     = var.storage_account_name
  resource_group_name      = azurerm_resource_group.main.name
  location                 = azurerm_resource_group.main.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  account_kind             = "StorageV2"

  is_hns_enabled                       = true
  min_tls_version                      = "TLS1_2"
  https_traffic_only_enabled           = true
  allow_nested_items_to_be_public      = false
  shared_access_key_enabled            = false
  public_network_access_enabled        = true
  cross_tenant_replication_enabled     = false
  default_to_oauth_authentication      = true

  tags = local.tags
}

# 3. Data Lake Gen2 Filesystem
resource "azurerm_storage_data_lake_gen2_filesystem" "main" {
  name               = var.filesystem_name
  storage_account_id = azurerm_storage_account.main.id
}

# 4. Azure Databricks Workspace (Premium)
resource "azurerm_databricks_workspace" "main" {
  name                = var.databricks_workspace_name
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_resource_group.main.location
  sku                 = "premium"

  tags = local.tags
}

# 5. Azure Databricks Access Connector (System Assigned Managed Identity)
resource "azurerm_databricks_access_connector" "main" {
  name                = var.access_connector_name
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_resource_group.main.location

  identity {
    type = "SystemAssigned"
  }

  tags = local.tags
}

# 6. RBAC: Access Connector -> Storage Blob Data Contributor on Storage Account
resource "azurerm_role_assignment" "access_connector_storage" {
  scope                = azurerm_storage_account.main.id
  role_definition_name = "Storage Blob Data Contributor"
  principal_id         = azurerm_databricks_access_connector.main.identity[0].principal_id

  depends_on = [azurerm_databricks_access_connector.main]
}

# 7. Azure Key Vault (RBAC authorization)
resource "azurerm_key_vault" "main" {
  name                       = var.keyvault_name
  location                   = azurerm_resource_group.main.location
  resource_group_name        = azurerm_resource_group.main.name
  tenant_id                  = data.azurerm_client_config.current.tenant_id
  sku_name                   = "standard"
  soft_delete_retention_days = 7
  purge_protection_enabled   = false
  rbac_authorization_enabled = true

  tags = local.tags
}

# 8. Azure Container Registry (Basic)
resource "azurerm_container_registry" "main" {
  name                = var.acr_name
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_resource_group.main.location
  sku                 = "Basic"
  admin_enabled       = false

  tags = local.tags
}
