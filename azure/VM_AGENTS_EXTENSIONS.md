# Azure VM Agents and Extensions

### VM Agents and Extensions Security Responsibilities

### Azure Monitor Agent

Azure Monitor Agent is implemented as an Azure VM extension with the details in the following table. You can install it
by using any of the methods to install virtual machine extensions including the methods described in this article.

| Property           | Windows                                                                                   | Linux                                                                                 |
|:-------------------|:------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------|
| Publisher          | Microsoft.Azure.Monitor                                                                   | Microsoft.Azure.Monitor                                                               |
| Type               | AzureMonitorWindowsAgent                                                                  | AzureMonitorLinuxAgent                                                                |
| TypeHandlerVersion | See [Azure Monitor agent extension versions](./azure-monitor-agent-extension-versions.md) | [Azure Monitor agent extension versions](./azure-monitor-agent-extension-versions.md) |

##### New Capabilities

- Ingestion-Time Transformations
- Filtering
- Scoping
- Multi-Homing

##### Considerations

- Prerequisites
    - Permissions
        - Deployment/Management
    - Azure/Non-Azure
        - To install the agent on physical servers and virtual machines hosted outside of Azure (that is, on-premises)
          or in other clouds, you must install the Azure Arc Connected Machine agent first, at no added cost.
    - Authentication
        - Managed identity must be enabled on Azure virtual machines. Both user-assigned and system-assigned managed
          identities are supported.
    - Networking
        - Access
            - `global.handler.control.monitor.azure.com`
            - `<virtual-machine-region-name>.handler.control.monitor.azure.com`
                - example: eastus2.handler.control.azure.com
                - example: centralus.handler.control.azure.com
            - `<log-analytics-workspace-id>.ods.opinsights.azure.com`
- Installation
- Configuration
- Disk Space
- Log Rotation
- Log Retention
- Data Collection Rule(s)
    - Sentinel Syslog Forwarder Data Collection Rule

##### Filepaths

- /var/opt/microsoft/azuremonitoragent
- /etc/opt/microsoft/azuremonitoragent/mdsd.xml
- /etc/rsyslog.d/10-azuremonitoragent.conf
- /run/azuremonitoragent/
- /etc/logrotate.d/rsyslog
- /etc/rsyslog.conf

##### Discover VM Extensions

> az vm extension image list

> az deployment group create --resource-group "<resource-group-name>" --template-file "<path-to-template>"
> --parameters "@<parameter-filename.json>"

### References

##### GitHub

- [GitHub - Open Management Infrastructure](https://github.com/microsoft/omi)
- [GitHub - Azure VM Linux Extensions](https://github.com/Azure/azure-linux-extensions)

##### YouTube

- [Everything You Ever Wanted to Know About Using the New Azure Monitor Agent with Microsoft Sentinel](https://www.youtube.com/watch?v=Tvs-5JbGK-c)

##### Official Documentation

- [Discover VM Extensions for Linux](https://learn.microsoft.com/en-us/azure/virtual-machines/extensions/features-linux)
- [Discover VM Extensions for Windows](https://learn.microsoft.com/en-us/azure/virtual-machines/extensions/features-windows)
- [Automatic Extension Upgrade](https://docs.microsoft.com/en-us/azure/virtual-machines/automatic-extension-upgrade#supported-extensions)
- [Microsoft Sentinel Support for Ingestion Time Data](https://techcommunity.microsoft.com/t5/microsoft-sentinel-blog/microsoft-sentinel-support-for-ingestion-time-data/ba-p/3244531)
- [Additional Guidance Regarding OMI Vulnerabilities within Azure VM Management Extensions](https://msrc-blog.microsoft.com/2021/09/16/additional-guidance-regarding-omi-vulnerabilities-within-azure-vm-management-extensions/)

##### Blogs

- [Sentinel Syslog Forwarder with Azure Monitor Agent](https://starkonsec.com/2022/04/18/sentinel-syslog-forwarder-with-the-azure-monitor-agent/)
- [Understanding the security responsibilities of Azure VM Agents and Extensions](https://davidokeyode.medium.com/understanding-the-security-responsibilities-of-azure-vm-agents-and-extensions-omigod-30296ca645e6)
