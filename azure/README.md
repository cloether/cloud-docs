# Microsoft Azure

### Azure Logging and Monitoring

- [Data Collection Best Practices](https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-data-collection)

##### Azure Cloud Adoption Framework

- [Monitoring - Service Level Objectives](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/manage/monitor/service-level-objectives)
- [Cloud Models - Monitoring Overview](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/manage/monitor/cloud-models-monitor-overview)
- [Monitoring Strategy](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/strategy/monitoring-strategy)

##### Azure Monitor

- [Azure Monitor - Security Controls using Azure Policy](https://learn.microsoft.com/en-us/azure/azure-monitor/security-controls-policy#azure-security-benchmark)

##### Azure Monitor Logs

- [Azure Monitor Logs - Workspace Design](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/workspace-design)
- [Azure Monitor Logs - Data Retention and Archive](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/data-retention-archive?tabs=portal-1%2Cportal-2)

##### ARM Schemas

- [Github - Azure/azure-resource-manager-schemas](https://github.com/Azure/azure-resource-manager-schemas)

<hr>

##### Azure Platform Logs

- Activity Logs
    - Subscription-Level Events
    - Default Retention: `90 Days`
    - Automatically Collected/Generated
        - Forward to a Destination for Longer Retention
    - Log Analytics Table: `AzureActivity`


- Resource Logs
    - Resource-Level Events
    - Provide detailed diagnostic and auditing information for Azure resources
      and the Azure platform they depend on.
    - Are not collected until they're routed to a destination


- [Azure Active Directory Logs](https://learn.microsoft.com/en-us/azure/active-directory/reports-monitoring/overview-reports)
    - Tenant-Level Events
    - Automatically Collected/Generated
    - Cost
        - Sending to Log Analytics: No
        - Log Analytics Data Ingestion: Yes
        - Log Analytics Data Retention: Yes
    - [How-To Integrate Activity Logs with Log Analytics](https://learn.microsoft.com/en-us/azure/active-directory/reports-monitoring/howto-integrate-activity-logs-with-log-analytics)
    - [Azure Sentinel - Connect Azure AD Logs](https://learn.microsoft.com/en-us/azure/sentinel/connect-azure-active-directory)


- Log Destinations
    - Log Analytics
        - Retention
          Mechanism: [Archive Policy](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/data-retention-archive?tabs=portal-1%2Cportal-2)
        - [Pricing](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/cost-logs)
    - Storage Account
        - Retention
          Mechanism: [Lifecycle Management Policy](https://learn.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-policy-configure?tabs=azure-portal)
    - Event Hub
    - Partner Integrations
