# Rulesets in MRS Format

## Overview

This repository is a fundamental and vital component of [Project META](https://github.com/Project-META) containing rulesets in MRS format.

## URLs

| Ruleset | GitHub Raw | jsDelivr |
| ------- | -------------- | -------------- |
| apple@cn | [https://raw.githubusercontent.com/Project-META/rules-mrs/basic/apple@cn.mrs](https://raw.githubusercontent.com/Project-META/rules-mrs/basic/apple@cn.mrs) | [https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@basic/apple@cn.mrs](https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@basic/apple@cn.mrs) |
| applications (can't be converted to MRS) | [https://raw.githubusercontent.com/Project-META/rules-mrs/basic/applications.yaml](https://raw.githubusercontent.com/Project-META/rules-mrs/basic/applications.yaml) | [https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@basic/applications.yaml](https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@basic/applications.yaml) |
| cncidr | [https://raw.githubusercontent.com/Project-META/rules-mrs/basic/cncidr.mrs](https://raw.githubusercontent.com/Project-META/rules-mrs/basic/cncidr.mrs) | [https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@basic/cncidr.mrs](https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@basic/cncidr.mrs) |
| direct | [https://raw.githubusercontent.com/Project-META/rules-mrs/basic/direct.mrs](https://raw.githubusercontent.com/Project-META/rules-mrs/basic/direct.mrs) | [https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@basic/direct.mrs](https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@basic/direct.mrs) |
| gfw | [https://raw.githubusercontent.com/Project-META/rules-mrs/basic/gfw.mrs](https://raw.githubusercontent.com/Project-META/rules-mrs/basic/gfw.mrs) | [https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@basic/gfw.mrs](https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@basic/gfw.mrs) |
| google@cn | [https://raw.githubusercontent.com/Project-META/rules-mrs/basic/google@cn.mrs](https://raw.githubusercontent.com/Project-META/rules-mrs/basic/google@cn.mrs) | [https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@basic/google@cn.mrs](https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@basic/google@cn.mrs) |
| greatfire | [https://raw.githubusercontent.com/Project-META/rules-mrs/basic/greatfire.mrs](https://raw.githubusercontent.com/Project-META/rules-mrs/basic/greatfire.mrs) | [https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@basic/greatfire.mrs](https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@basic/greatfire.mrs) |
| icloud | [https://raw.githubusercontent.com/Project-META/rules-mrs/basic/icloud.mrs](https://raw.githubusercontent.com/Project-META/rules-mrs/basic/icloud.mrs) | [https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@basic/icloud.mrs](https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@basic/icloud.mrs) |
| lancidr | [https://raw.githubusercontent.com/Project-META/rules-mrs/basic/lancidr.mrs](https://raw.githubusercontent.com/Project-META/rules-mrs/basic/lancidr.mrs) | [https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@basic/lancidr.mrs](https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@basic/lancidr.mrs) |
| private | [https://raw.githubusercontent.com/Project-META/rules-mrs/basic/private.mrs](https://raw.githubusercontent.com/Project-META/rules-mrs/basic/private.mrs) | [https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@basic/private.mrs](https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@basic/private.mrs) |
| proxy | [https://raw.githubusercontent.com/Project-META/rules-mrs/basic/proxy.mrs](https://raw.githubusercontent.com/Project-META/rules-mrs/basic/proxy.mrs) | [https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@basic/proxy.mrs](https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@basic/proxy.mrs) |
| reject | [https://raw.githubusercontent.com/Project-META/rules-mrs/basic/reject.mrs](https://raw.githubusercontent.com/Project-META/rules-mrs/basic/reject.mrs) | [https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@basic/reject.mrs](https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@basic/reject.mrs) |
| telegramcidr | [https://raw.githubusercontent.com/Project-META/rules-mrs/basic/telegramcidr.mrs](https://raw.githubusercontent.com/Project-META/rules-mrs/basic/telegramcidr.mrs) | [https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@basic/telegramcidr.mrs](https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@basic/telegramcidr.mrs) |
| tld-!cn | [https://raw.githubusercontent.com/Project-META/rules-mrs/basic/tld-!cn.mrs](https://raw.githubusercontent.com/Project-META/rules-mrs/basic/tld-!cn.mrs) | [https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@basic/tld-!cn.mrs](https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@basic/tld-!cn.mrs) |

## Usage

***The way to use this repository is strongly recommended to use [META](https://github.com/Project-META) that has perfectly integrated this repository, because that is what this repository was created for.***

- The following are examples of rule providers in the configuration, for reference only.

    ```yaml
    rule-providers:
        reject:
            type: http
            format: mrs
            interval: 86400
            behavior: domain
            path: ./ruleset/reject.mrs
            url: "https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@basic/reject.mrs"
        apple@cn:
            type: http
            format: mrs
            interval: 86400
            behavior: domain
            path: ./ruleset/apple@cn.mrs
            url: "https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@basic/apple@cn.mrs"
        applications:
            type: http
            format: yaml
            interval: 86400
            behavior: classical
            path: ./ruleset/applications.yaml
            url: "https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@basic/applications.yaml"
        cncidr:
            type: http
            format: mrs
            interval: 86400
            behavior: ipcidr
            path: ./ruleset/cncidr.mrs
            url: "https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@basic/cncidr.mrs"
        direct:
            type: http
            format: mrs
            interval: 86400
            behavior: domain
            path: ./ruleset/direct.mrs
            url: "https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@basic/direct.mrs"
        google@cn:
            type: http
            format: mrs
            interval: 86400
            behavior: domain
            path: ./ruleset/google@cn.mrs
            url: "https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@basic/google@cn.mrs"
        icloud:
            type: http
            format: mrs
            interval: 86400
            behavior: domain
            path: ./ruleset/icloud.mrs
            url: "https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@basic/icloud.mrs"
        lancidr:
            type: http
            format: mrs
            interval: 86400
            behavior: ipcidr
            path: ./ruleset/lancidr.mrs
            url: "https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@basic/lancidr.mrs"
        private:
            type: http
            format: mrs
            interval: 86400
            behavior: domain
            path: ./ruleset/private.mrs
            url: "https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@basic/private.mrs"
        proxy:
            type: http
            format: mrs
            interval: 86400
            behavior: domain
            path: ./ruleset/proxy.mrs
            url: "https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@basic/proxy.mrs"
        telegramcidr:
            type: http
            format: mrs
            interval: 86400
            behavior: ipcidr
            path: ./ruleset/telegramcidr.mrs
            url: "https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@basic/telegramcidr.mrs"
        tld-!cn:
            type: http
            format: mrs
            interval: 86400
            behavior: domain
            path: ./ruleset/tld-!cn.mrs
            url: "https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@basic/tld-!cn.mrs"

        bilibili:
            type: http
            format: mrs
            interval: 86400
            behavior: domain
            path: ./ruleset/bilibili.mrs
            url: "https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@universal/bilibili.mrs"
        ...
    ```

- The following is an example of routing rules in the configuration, for reference only.

    ```yaml
    rules:
    - RULE-SET,applications,DIRECT
    - RULE-SET,lancidr,DIRECT
    - RULE-SET,private,DIRECT
    - RULE-SET,reject,Advertising
    - RULE-SET,bilibili,bilibili
    ...
    - RULE-SET,icloud,iCloud
    - RULE-SET,apple@cn,DIRECT
    - RULE-SET,google@cn,PROXY
    - RULE-SET,direct,Mainland China
    - RULE-SET,proxy,PROXY
    - RULE-SET,tld-!cn,PROXY
    - RULE-SET,telegramcidr,Telegram
    - RULE-SET,cncidr,Mainland China
    - MATCH,PROXY
    ```

## Disclaimer

1. This project is strictly for educational and research purposes.
2. Use at your own risk. The project assumes no responsibility for potential issues.
3. No guarantee of accuracy, completeness, or reliability.
4. Not liable for data loss or damages.
5. Ensure compliance with relevant licenses and legal regulations.
6. No endorsement of third-party hardware/software.
7. User modifications are their own responsibility.
8. Terms may change at any time. By using this project, you agree to these terms.

## License

Copyright &copy; 2024 Project META. All rights reserved.

Licensed under the [GPL-3.0](https://github.com/Project-META/rules-mrs/blob/main/LICENSE) license.  
