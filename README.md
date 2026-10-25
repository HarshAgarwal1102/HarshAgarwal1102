<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/banner-light.svg">
  <img alt="Harsh Agarwal, DevSecOps & Cloud Engineer" src="assets/banner-dark.svg" width="100%">
</picture>

<p align="center">
  <a href="https://drive.google.com/file/d/1NM0YT_uRSXG6S4tKwD47B3GF6WAhz4dG/view?usp=drive_link"><img src="https://img.shields.io/badge/Résumé-FF7A1A?style=for-the-badge&logo=googledrive&logoColor=white" alt="Résumé"></a>
  <a href="https://harshagarwal-portfolio.netlify.app/"><img src="https://img.shields.io/badge/Portfolio-0B1020?style=for-the-badge&logo=netlify&logoColor=00C7B7" alt="Portfolio"></a>
  <a href="https://www.linkedin.com/in/harsh4404/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="https://medium.com/@harshagarwal2225/"><img src="https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white" alt="Medium"></a>
  <a href="mailto:harshagarwal.4404@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"></a>
</p>

<p align="center">
  <img src="assets/terminal.svg" alt="Terminal: whoami, terraform plan with no drift, 2885 tests passing" width="820">
</p>

> I design and automate **Azure platforms that are scalable, secure, governed and cost-aware**: landing zones, hub-and-spoke networks, Terraform with policy guardrails, and pipelines that catch drift, secrets and cost surprises before production does.
> Every design starts from one question: **what is the business, and what is the functional domain?**

---

## ⚡ At a Glance

```yaml
# $ kubectl get engineer harsh-agarwal -o yaml
apiVersion: people/v1
kind: Engineer
metadata:
  name: harsh-agarwal
  labels:
    role: devsecops-cloud-engineer
    cloud: azure
spec:
  currentlyAt: Hansa Solutions India Pvt Ltd
  platform:  [azure-landing-zones, hub-and-spoke, entra-id, azure-policy, pim]
  iac:       [terraform, bicep, cloud-init]
  pipelines: [github-actions, azure-devops, oidc-federation, sha-pinned-actions]
  security:  [tflint, trivy, checkov, gitleaks, trufflehog, defender-for-cloud]
  finops:    [infracost, azure-retail-prices-api, rightsizing, reservations]
  aiops:     [python, langgraph]
  education: "B.Tech CSE, DIT University (2024)"
status:
  building: ai-terraform-drift-detector Level 2 (local-first CLI)
  openTo:   [platform-engineering, cloud-architecture, devsecops]
```

---

## 🚀 Featured Engineering

### 🔍 [AI-Powered Terraform Drift Detection & Remediation Platform](https://github.com/HarshAgarwal1102/ai-terraform-drift-detector)

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=flat-square&logo=terraform&logoColor=white)
![Azure](https://img.shields.io/badge/Azure-0078D4?style=flat-square&logo=microsoftazure&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=flat-square&logo=langchain&logoColor=white)
![Release](https://img.shields.io/badge/release-level1--v1.0.0-FF7A1A?style=flat-square)

Finds out when Azure no longer matches Terraform, explains **who changed what, when, and what it costs**, and raises it before it becomes an incident.

```mermaid
flowchart LR
    AZ[("Azure<br/>live state")] --> PLAN["Scheduled plan<br/>GitHub Actions + OIDC"]
    PLAN --> ENG["Deterministic<br/>drift engine (Python)"]
    ENG --> ISS["GitHub Issue<br/>per drifted resource"]
    ENG --> INV["Activity Log<br/>who / when / what"]
    ENG --> AI["LangGraph analysis<br/>LLM opt-in"]
    ENG --> COST["Infracost +<br/>unmanaged resources"]
    INV & AI & COST --> UI["Local dashboard"]
```

| Engineering rigour | |
| :--- | :--- |
| ✅ **2,885 tests**, 98.85 % coverage of the drift engine | 🧪 **135-case** end-to-end matrix with failure injection |
| 🔐 OIDC trust limited to `main`, **no client secrets** | 📌 Every workflow action **pinned by full commit SHA** |
| 🛡️ TFLint · Trivy · TruffleHog in CI | 🚦 Protected `main`: PR + **6 required checks** |
| 💰 Flagged 5 resources created outside Terraform in a live Azure test (≈ $44.85/mo list price) | 🧭 Remediation designed human-in-the-loop: safety spec first, no write access |

### 🏗️ [Azure Infrastructure Landing Zone](https://github.com/HarshAgarwal1102/Azure-Infra-Landing-Zone)

![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=flat-square&logo=terraform&logoColor=white)
![Azure](https://img.shields.io/badge/Azure-0078D4?style=flat-square&logo=microsoftazure&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)
![Gitleaks](https://img.shields.io/badge/Gitleaks-DC3545?style=flat-square&logo=git&logoColor=white)

A modular, fully automated Azure landing zone in Terraform.

- **9 reusable modules:** VNet, Subnet, Application Gateway, Load Balancer, Bastion, Key Vault, VM, Public IP, Resource Group
- **Environment separation:** `preprod` and `prod` compose the same modules with their own variables
- **Bootstrap stage** creates the remote-state storage idempotently, with TLS 1.2 and no public blob access
- **Pipeline:** bootstrap → `init` / `validate` / `plan` → `apply`, with Gitleaks secret scanning

---

## 🏛️ The 10 Pillars I Build Against

| | | | | |
|:---:|:---:|:---:|:---:|:---:|
| 📈 **Scalable** | 🧱 **Robust** | 🔐 **Secure** | ✅ **Reliable** | 📦 **Portable** |
| 🧭 **Governed** | ♻️ **Highly Available** | 💰 **Cost-Optimized** | 💾 **Backed Up** | 📊 **Compliant & Monitored** |

---

## 🧩 How I Design

<details>
<summary><b>🏗️ Enterprise governance & landing zones (Microsoft CAF)</b></summary>
<br>

**Strategy → Plan → Ready → Adopt → Govern → Secure & Manage**

```
                        [ Microsoft Entra ID Tenant ]
                                      |
                            [ Tenant Root Group ]
                                      |
       +------------------------------+------------------------------+
       |                              |                              |
 [ Platform MG ]            [ Landing Zones MG ]          [ Sandbox / Decommissioned ]
  |-- Identity (AD/DNS)       |-- Corp   (internal only)
  |-- Management (Logs/Mon)   |-- Online (public / DMZ)
  `-- Connectivity (Hub/FW)   `-- Dev | UAT | Prod subscriptions
```

- **Subscription boundaries** per environment and function to contain blast radius
- **Azure Policy initiatives** (CIS, MCSB) at Management Group scope; audit/deny with time-bound, documented exemptions
- **Group-based RBAC + PIM** for just-in-time privileged access with multi-stage approval

</details>

<details>
<summary><b>🌐 Hub-and-spoke networking</b></summary>
<br>

```mermaid
flowchart TB
    OnPrem["On-Premises"] -- "ExpressRoute / S2S VPN" --> GW
    subgraph HUB["HUB VNet"]
        GW["VPN / ER Gateway"]
        FW["Azure Firewall Premium"]
        DNS["Private DNS Zones"]
    end
    subgraph S1["Spoke: App VNet"]
        APP["App tier"] --- DB["DB tier"] --- PE["Private Endpoints"]
    end
    subgraph S2["Spoke: Shared Services"]
        RUN["CI/CD runners"] --- BAS["Bastion"] --- SEC["Security tooling"]
    end
    FW <-- "peering + UDR 0.0.0.0/0" --> S1
    FW <-- "peering + UDR 0.0.0.0/0" --> S2
    NET(("Internet")) -- "Front Door / App GW + WAF" --> S1
```

- **IPAM first:** no overlap between on-prem CIDRs and Azure address spaces
- **Forced tunnelling** of default and inter-spoke traffic through the firewall
- **Private-only PaaS** through Private Endpoints and hub-linked Private DNS

</details>

<details>
<summary><b>🛡️ Defense in depth</b></summary>
<br>

| Layer | Controls |
| :--- | :--- |
| **Identity** | Entra ID, Conditional Access, MFA, PIM, Managed Identities instead of secrets |
| **Network** | NSG/ASG micro-segmentation, Azure Firewall Premium, Private Endpoints, DDoS Protection |
| **Governance** | Azure Policy, CIS / ISO 27001 benchmarks, Defender for Cloud Secure Score |
| **Compute** | Defender for Servers, vulnerability scanning, CMK disk encryption, patch baselines |

</details>

<details>
<summary><b>⚙️ Terraform delivery pipeline</b></summary>
<br>

```mermaid
flowchart LR
    A["PR"] --> B["fmt · validate · tflint"]
    B --> C["Gitleaks · Checkov · Trivy"]
    C --> D["Infracost"]
    D --> E["Plan artifact + drift check"]
    E --> F{"Approval<br/>UAT / Prod"}
    F -->|approved| G["Apply<br/>locked remote state"]
    G -->|failure| H["Rollback"]
```

- Remote state in private Storage with blob-lease locking, reached through a least-privilege Managed Identity
- Semantically versioned modules · nightly `plan -detailed-exitcode` drift checks
- Trunk-based development; `main` protected with no direct push, 2 reviewers and `CODEOWNERS`

</details>

<details>
<summary><b>🚚 Migration of 100+ workloads (Dev / UAT / Prod)</b></summary>
<br>

```mermaid
flowchart LR
    D["Discovery"] --> A["Assessment<br/>& TCO"] --> R["Readiness"] --> C["Cutover"] --> H["Hypercare"]
```

| Phase | Checklist |
| :--- | :--- |
| **Pre-migration** | Azure Migrate discovery, dependency mapping, bandwidth sizing, backup verification |
| **Cutover** | Replication sync, DNS TTL reduction, traffic rerouting, validation tests |
| **Post-migration** | Telemetry, user sanity tests, performance benchmarks, 2–4 weeks of hypercare |

</details>

<details>
<summary><b>💰 FinOps · 💾 DR · 📡 Observability</b></summary>
<br>

| Area | Practice |
| :--- | :--- |
| **FinOps** | Remove orphaned disks, snapshots and IPs; rightsize on 30-day P95; Reservations and Savings Plans; non-prod schedules; DCR log filtering |
| **DR / HA** | LRS → ZRS → GRS by criticality; VMSS across zones; ASR to the paired region; explicit RTO and RPO per workload |
| **Observability** | Central Log Analytics per landing zone; Azure Monitor Agent with DCRs; Action Groups to Teams, Slack or PagerDuty |

</details>

<details>
<summary><b>🤝 Leadership & delivery governance</b></summary>
<br>

`RFI → RFP → Evaluation matrix → SOW → Milestones → Acceptance sign-off`

- Knowledge-transfer sessions, mentoring, interview panels
- Pre-sales estimates, POCs and RFP responses
- RACI and escalation matrices with one accountable owner per deliverable
- SOPs, runbooks, ADRs and blameless retrospectives

</details>

---

## 🛠️ Toolbox

<p align="center">
  <img src="https://skillicons.dev/icons?i=azure,terraform,githubactions,docker,kubernetes,ansible&theme=dark" alt="Cloud and IaC"><br>
  <img src="https://skillicons.dev/icons?i=linux,bash,powershell,python,git,github&theme=dark" alt="Scripting and source control"><br>
  <img src="https://skillicons.dev/icons?i=prometheus,grafana,cs,dotnet,java,react&theme=dark" alt="Observability and development">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Azure_DevOps-0078D7?style=flat-square&logo=azuredevops&logoColor=white" alt="Azure DevOps">
  <img src="https://img.shields.io/badge/Bicep-0078D4?style=flat-square&logo=microsoftazure&logoColor=white" alt="Bicep">
  <img src="https://img.shields.io/badge/Entra_ID-0078D4?style=flat-square&logo=microsoft&logoColor=white" alt="Entra ID">
  <img src="https://img.shields.io/badge/Trivy-1904DA?style=flat-square&logo=aqua&logoColor=white" alt="Trivy">
  <img src="https://img.shields.io/badge/Checkov-4B32C3?style=flat-square&logo=paloaltonetworks&logoColor=white" alt="Checkov">
  <img src="https://img.shields.io/badge/TFLint-7B42BC?style=flat-square&logo=terraform&logoColor=white" alt="TFLint">
  <img src="https://img.shields.io/badge/Gitleaks-DC3545?style=flat-square&logo=git&logoColor=white" alt="Gitleaks">
  <img src="https://img.shields.io/badge/Infracost-DB44B8?style=flat-square&logo=terraform&logoColor=white" alt="Infracost">
  <img src="https://img.shields.io/badge/LangGraph-1C3C3C?style=flat-square&logo=langchain&logoColor=white" alt="LangGraph">
</p>

---

## ✍️ Latest Writing

<!-- BLOG-POST-LIST:START -->
- [What is DevOps? A Simple & Complete Guide for Beginners](https://medium.com/@harshagarwal2225/what-is-devops-9066e3f22cb8) <sub>· Nov 2025</sub>
- [My Virtual Internship Experience at Oasis Infobyte](https://medium.com/@harshagarwal2225/my-virtual-internship-experience-at-oasis-infobyte-60b2b6a90a07) <sub>· Oct 2023</sub>
- [About TicTacToe Game](https://medium.com/@harshagarwal2225/about-tictactoe-game-1a1351c327fd) <sub>· Jun 2023</sub>
<!-- BLOG-POST-LIST:END -->

---

## 📈 Activity

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/HarshAgarwal1102/HarshAgarwal1102/output/github-snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/HarshAgarwal1102/HarshAgarwal1102/output/github-snake.svg">
  <img alt="Contribution graph being eaten by a snake" src="https://raw.githubusercontent.com/HarshAgarwal1102/HarshAgarwal1102/output/github-snake.svg" width="100%">
</picture>

<p align="center">
  <img height="160" src="https://github-readme-stats.vercel.app/api?username=HarshAgarwal1102&theme=tokyonight&hide_border=true&include_all_commits=true&count_private=true&show_icons=true" alt="GitHub stats">
  <img height="160" src="https://github-readme-streak-stats.herokuapp.com/?user=HarshAgarwal1102&theme=tokyonight&hide_border=true" alt="GitHub streak">
</p>

---

## 🤖 This Profile Is Code

This README is maintained the way I run infrastructure: versioned, automated and least-privilege.

| Workflow | What it does |
| :--- | :--- |
| [![snake](https://github.com/HarshAgarwal1102/HarshAgarwal1102/actions/workflows/snake.yml/badge.svg)](.github/workflows/snake.yml) | Regenerates the contribution snake daily and publishes it to the `output` branch |
| [Dependabot](.github/dependabot.yml) | Keeps every action, pinned by commit SHA, up to date |
| 🔒 Branch protection | `main` is locked and PR-only, just like production |

Header and terminal art are hand-built SVGs in [`assets/`](assets), with dark and light variants.

<details>
<summary>🦖 Off duty</summary>
<br>
<p align="center">
  <img src="https://github.com/HarshAgarwal1102/HarshAgarwal1102/assets/117922914/61d89383-610c-46c1-a1d8-b0b06e57a9c8" alt="Chrome dino game" width="600">
</p>
<p align="center">I travel a lot to places near where I live, and I'm always up for a conversation about life, cloud, or both.</p>
</details>

<p align="center"><sub><i>Automate the boring · Govern the critical · Measure everything</i></sub></p>
