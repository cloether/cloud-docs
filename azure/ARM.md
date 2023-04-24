# Azure Resource Manager (ARM)


##### List the Available API Version for all Resource Types in a Given Cloud

```shell
az provider list --query "[].{namespace:namespace, resourceType:resourceType[]}"
```

### References

- [Azure Control Plane and Data 
Plane](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/control-plane-and-data-plane)
- [Develop ARM templates for cloud consistency](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/template-cloud-consistency)
- [Resource iteration in ARM templates](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/copy-resources)
- [Understand the structure and syntax of ARM templates](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/syntax)
