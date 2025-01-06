def main():
    """
    1. Conecta ao SharePoint;
    2. Move o arquivo vrm para a pasta backup;
    3. Move o arquivo vendor_risk para a pasta backup;
    4. Executa o código-fonte do Monday Automation;
    5. Transfere o arquivo VRM novo para a pasta VRM;
    6. Transfere o arquivo vendor_risk novo para a pasta vendor_risk.

    connect_to_sharepoint()
    move_file(vrm_file)
    move_file(vendor_risk_file)
    execute_monday_automation()
    upload_file(new_vrm_file)
    upload_file(new_vendor_risk_file)
    """
    ...


if __name__ == '__main__':
    main()
