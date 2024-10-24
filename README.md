# Rulesets in MRS Format
- the fundamental and vital component of Project META

## Overview

This repository is the fundamental and vital component of Project META containing rulesets in MRS format converted from extended [Loyalsoldier's rulesets](https://github.com/Loyalsoldier/clash-rules) merged with the corresponding [MetaCubeX's rulesets](https://github.com/MetaCubeX/meta-rules-dat). Use GitHub Actions to automatically build every day at 6:50 am Beijing time to ensure the rulesets kept up to date.

## URLs

| Ruleset | GitHub Raw | jsDelivr |
| ------- | -------------- | -------------- |
| ads | [https://raw.githubusercontent.com/Project-META/rules-mrs/release/ads.mrs](https://raw.githubusercontent.com/Project-META/rules-mrs/release/ads.mrs) | [https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@release/ads.mrs](https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@release/ads.mrs) |
| apple@cn | [https://raw.githubusercontent.com/Project-META/rules-mrs/release/apple@cn.mrs](https://raw.githubusercontent.com/Project-META/rules-mrs/release/apple@cn.mrs) | [https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@release/apple@cn.mrs](https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@release/apple@cn.mrs) |
| applications (can't be converted to MRS) | [https://raw.githubusercontent.com/Project-META/rules-mrs/release/applications.yaml](https://raw.githubusercontent.com/Project-META/rules-mrs/release/applications.yaml) | [https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@release/applications.yaml](https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@release/applications.yaml) |
| cncidr | [https://raw.githubusercontent.com/Project-META/rules-mrs/release/cncidr.mrs](https://raw.githubusercontent.com/Project-META/rules-mrs/release/cncidr.mrs) | [https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@release/cncidr.mrs](https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@release/cncidr.mrs) |
| direct | [https://raw.githubusercontent.com/Project-META/rules-mrs/release/direct.mrs](https://raw.githubusercontent.com/Project-META/rules-mrs/release/direct.mrs) | [https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@release/direct.mrs](https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@release/direct.mrs) |
| gfw | [https://raw.githubusercontent.com/Project-META/rules-mrs/release/gfw.mrs](https://raw.githubusercontent.com/Project-META/rules-mrs/release/gfw.mrs) | [https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@release/gfw.mrs](https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@release/gfw.mrs) |
| google@cn | [https://raw.githubusercontent.com/Project-META/rules-mrs/release/google@cn.mrs](https://raw.githubusercontent.com/Project-META/rules-mrs/release/google@cn.mrs) | [https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@release/google@cn.mrs](https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@release/google@cn.mrs) |
| greatfire | [https://raw.githubusercontent.com/Project-META/rules-mrs/release/greatfire.mrs](https://raw.githubusercontent.com/Project-META/rules-mrs/release/greatfire.mrs) | [https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@release/greatfire.mrs](https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@release/greatfire.mrs) |
| icloud | [https://raw.githubusercontent.com/Project-META/rules-mrs/release/icloud.mrs](https://raw.githubusercontent.com/Project-META/rules-mrs/release/icloud.mrs) | [https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@release/icloud.mrs](https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@release/icloud.mrs) |
| lancidr | [https://raw.githubusercontent.com/Project-META/rules-mrs/release/lancidr.mrs](https://raw.githubusercontent.com/Project-META/rules-mrs/release/lancidr.mrs) | [https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@release/lancidr.mrs](https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@release/lancidr.mrs) |
| private | [https://raw.githubusercontent.com/Project-META/rules-mrs/release/private.mrs](https://raw.githubusercontent.com/Project-META/rules-mrs/release/private.mrs) | [https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@release/private.mrs](https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@release/private.mrs) |
| proxy | [https://raw.githubusercontent.com/Project-META/rules-mrs/release/proxy.mrs](https://raw.githubusercontent.com/Project-META/rules-mrs/release/proxy.mrs) | [https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@release/proxy.mrs](https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@release/proxy.mrs) |
| telegramcidr | [https://raw.githubusercontent.com/Project-META/rules-mrs/release/telegramcidr.mrs](https://raw.githubusercontent.com/Project-META/rules-mrs/release/telegramcidr.mrs) | [https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@release/telegramcidr.mrs](https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@release/telegramcidr.mrs) |
| tld-!cn | [https://raw.githubusercontent.com/Project-META/rules-mrs/release/tld-!cn.mrs](https://raw.githubusercontent.com/Project-META/rules-mrs/release/tld-!cn.mrs) | [https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@release/tld-!cn.mrs](https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@release/tld-!cn.mrs) |

## Usage

***The way to use this repository is strongly recommended to use [META](https://github.com/Project-META) which has this repository integrated.***

- The following are examples of rule providers in the configuration, for reference only.

    ```yaml
    rule-providers:
        ads:
            type: http
            format: mrs
            interval: 86400
            behavior: domain
            path: ./ruleset/ads.mrs
            url: "https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@release/ads.mrs"
        apple@cn:
            type: http
            format: mrs
            interval: 86400
            behavior: domain
            path: ./ruleset/apple@cn.mrs
            url: "https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@release/apple@cn.mrs"
        applications:
            type: http
            format: yaml
            interval: 86400
            behavior: classical
            path: ./ruleset/applications.yaml
            url: "https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@release/applications.yaml"
        cncidr:
            type: http
            format: mrs
            interval: 86400
            behavior: ipcidr
            path: ./ruleset/cncidr.mrs
            url: "https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@release/cncidr.mrs"
        direct:
            type: http
            format: mrs
            interval: 86400
            behavior: domain
            path: ./ruleset/direct.mrs
            url: "https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@release/direct.mrs"
        google@cn:
            type: http
            format: mrs
            interval: 86400
            behavior: domain
            path: ./ruleset/google@cn.mrs
            url: "https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@release/google@cn.mrs"
        icloud:
            type: http
            format: mrs
            interval: 86400
            behavior: domain
            path: ./ruleset/icloud.mrs
            url: "https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@release/icloud.mrs"
        lancidr:
            type: http
            format: mrs
            interval: 86400
            behavior: ipcidr
            path: ./ruleset/lancidr.mrs
            url: "https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@release/lancidr.mrs"
        private:
            type: http
            format: mrs
            interval: 86400
            behavior: domain
            path: ./ruleset/private.mrs
            url: "https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@release/private.mrs"
        proxy:
            type: http
            format: mrs
            interval: 86400
            behavior: domain
            path: ./ruleset/proxy.mrs
            url: "https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@release/proxy.mrs"
        telegramcidr:
            type: http
            format: mrs
            interval: 86400
            behavior: ipcidr
            path: ./ruleset/telegramcidr.mrs
            url: "https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@release/telegramcidr.mrs"
        tld-!cn:
            type: http
            format: mrs
            interval: 86400
            behavior: domain
            path: ./ruleset/tld-!cn.mrs
            url: "https://cdn.jsdelivr.net/gh/Project-META/rules-mrs@release/tld-!cn.mrs"
    ```

- The following is an example of routing rules in the configuration, for reference only.

    ```yaml
    rules:
    - RULE-SET,applications,DIRECT
    - RULE-SET,lancidr,DIRECT
    - RULE-SET,private,DIRECT
    - RULE-SET,ads,REJECT
    - RULE-SET,icloud,DIRECT
    - RULE-SET,apple@cn,DIRECT
    - RULE-SET,google@cn,PROXY
    - RULE-SET,direct,DIRECT
    - RULE-SET,proxy,PROXY
    - RULE-SET,tld-!cn,PROXY
    - RULE-SET,telegramcidr,PROXY
    - RULE-SET,cncidr,DIRECT
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
