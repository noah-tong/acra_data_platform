variable "project_name" {
  description = "Project prefix used for tagging and naming."
  type        = string
}

variable "environment" {
  description = "Deployment environment (e.g. dev, prod)."
  type        = string
}

variable "location" {
  description = "Azure region for all resources."
  type        = string
}

variable "resource_group_name" {
  description = "Name of the Azure resource group."
  type        = string
}

variable "storage_account_name" {
  description = "Globally unique name for the ADLS Gen2 storage account."
  type        = string
}

variable "filesystem_name" {
  description = "Name of the ADLS Gen2 filesystem (container)."
  type        = string
}

variable "databricks_workspace_name" {
  description = "Name of the Azure Databricks workspace."
  type        = string
}

variable "access_connector_name" {
  description = "Name of the Azure Databricks Access Connector."
  type        = string
}

variable "keyvault_name" {
  description = "Name of the Azure Key Vault."
  type        = string
}

variable "acr_name" {
  description = "Name of the Azure Container Registry."
  type        = string
}
