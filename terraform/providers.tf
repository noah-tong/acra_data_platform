provider "azurerm" {
  # Required when shared_access_key_enabled = false on the storage account.
  storage_use_azuread = true

  features {}
}

# Databricks provider is declared for future Unity Catalog configuration (v2+).
# Version 1 provisions Azure resources only via azurerm.
