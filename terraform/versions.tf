terraform {
  required_version = ">= 1.8"

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 4.80"
    }
    databricks = {
      source  = "databricks/databricks"
      version = "~> 1.121"
    }
  }
}
