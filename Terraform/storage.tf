resource "azurerm_storage_container" "data" {
  name                  = "newdata"
  storage_account_name  = azurerm_storage_account.sa.name
  container_access_type = "private"
}