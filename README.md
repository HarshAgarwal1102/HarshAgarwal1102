<h1 align="center">
  <img src="https://github.com/HarshAgarwal1102/HarshAgarwal1102/assets/117922914/0c0075b0-9185-4576-82b9-9c34f9f2667b" alt="HarshAgarwal1102" />
  <br>
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=32&pause=1200&color=FF7722&center=true&vCenter=true&width=820&height=70&lines=Hi%2C+I'm+Harsh+Agarwal+%F0%9F%91%8B;DevSecOps+%26+Cloud+Engineer;Azure+%7C+Terraform+%7C+Kubernetes;Landing+Zones+%E2%80%A2+Migrations+%E2%80%A2+FinOps" alt="Typing SVG" />
  </a>
</h1>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=king4404&color=FF7722&style=flat-square&label=Profile+Views" alt="profile views" />
  <a href="https://drive.google.com/file/d/1NM0YT_uRSXG6S4tKwD47B3GF6WAhz4dG/view?usp=drive_link"><img src="https://img.shields.io/badge/Resume-View-FF7722?style=flat-square&logo=googledrive&logoColor=white" alt="Resume" /></a>
  <a href="https://www.linkedin.com/in/harsh4404/"><img src="https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="mailto:harshagarwal.4404@gmail.com"><img src="https://img.shields.io/badge/Email-Reach_Out-D14836?style=flat-square&logo=gmail&logoColor=white" alt="Email" /></a>
</p>

<h3 align="center">I design cloud platforms that are <i>scalable, secure, governed and cost-aware</i> — and automate everything in between.</h3>

---

## 💫 About Me

<img align="right" alt="cloud" width="320" src="https://i.pinimg.com/originals/81/17/8b/81178b47a8598f0c81c4799f2cdd4057.gif">

- 🏢 Currently building @ <a href="https://www.linkedin.com/company/hansa-solutions-india-pvt-ltd/">Hansa Solutions India Pvt Ltd</a>
- ☁️ Focused on **Azure landing zones, Infrastructure as Code, DevSecOps pipelines and cloud migration**
- 🧠 I start every design with one question: **"What is the business, and what is the functional domain?"**
- 🔭 B.Tech (CSE) — 2024 graduate, DIT University 🎓
- 📝 I write about cloud architecture, ADRs and post-mortems on [Medium](https://medium.com/@harshagarwal2225/)
- 📫 **harshagarwal.4404@gmail.com** · ⚡ Fun fact: I travel a lot to places near where I live

<br clear="right"/>

---

## 🏛️ The 10 Pillars I Build Against

Every workload I design or migrate is measured against these pillars:

| | | | | |
|:---:|:---:|:---:|:---:|:---:|
| 📈 **Scalable** | 🧱 **Robust** | 🔐 **Secure** | ✅ **Reliable** | 📦 **Portable** |
| 🧭 **Governed** | ♻️ **Highly Available** | 💰 **Cost-Optimized** | 💾 **Backed Up** | 📊 **Compliant & Monitored** |

---

## 🧩 Core Expertise

<details open>
<summary><b>🏗️ Enterprise Governance & Landing Zones (Microsoft CAF)</b></summary>
<br>

I follow the **Cloud Adoption Framework** end to end: **Strategy → Plan → Ready → Adopt → Govern → Secure & Manage**.

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

- **Subscription boundaries** per environment and function to isolate blast radius and avoid noisy neighbours
- **Azure Policy & Initiatives** (CIS Benchmark, MCSB) assigned at Management Group scope, with audit/deny effects and time-bound, documented exemptions
- **Group-based RBAC + PIM** — just-in-time privileged access with multi-stage approvals

</details>

<details open>
<summary><b>🌐 Hub-and-Spoke Networking</b></summary>
<br>

```mermaid
flowchart TB
    OnPrem["🏢 On-Premises Datacenter"] -- "ExpressRoute / S2S VPN" --> GW

    subgraph HUB["HUB VNet — Central Connectivity"]
        GW["GatewaySubnet<br/>VPN / ER Gateway"]
        FW["Azure Firewall Premium<br/>/ NVA"]
        DNS["Private DNS Zones"]
    end

    subgraph S1["Spoke 1 — App VNet"]
        APP["App Tier"] --- DB["DB Tier"] --- PE["Private Endpoints"]
    end

    subgraph S2["Spoke 2 — Shared Services VNet"]
        RUN["CI/CD Runners"] --- BAS["Bastion"] --- SEC["Security Tooling"]
    end

    FW <-- "Peering + UDR 0.0.0.0/0 → FW" --> S1
    FW <-- "Peering + UDR 0.0.0.0/0 → FW" --> S2
    Internet(("🌍 Internet")) -- "Front Door / App Gateway + WAF" --> S1
```

- **IPAM first** — audit on-prem CIDRs so no Azure VNet address space overlaps
- **Centralised inspection** — UDRs force default and inter-spoke traffic through the firewall
- **Controlled ingress/egress** — WAF at the edge, TLS-inspected egress through the hub
- **Private-only PaaS** — Private Endpoints for Key Vault, Storage and SQL, resolved through hub-linked Private DNS Zones

</details>

<details open>
<summary><b>🛡️ Defense-in-Depth Security</b></summary>
<br>

| Layer | Controls |
| :--- | :--- |
| **Identity** | Microsoft Entra ID, Conditional Access, MFA, PIM, Managed Identities over secrets |
| **Network** | Hub-and-spoke, NSG/ASG micro-segmentation, Azure Firewall Premium, Private Endpoints, DDoS Protection |
| **Governance** | Azure Policy, CIS / ISO 27001 benchmarks, Defender for Cloud Secure Score |
| **Compute** | Defender for Servers, vulnerability scanning, disk encryption with CMK, automated patch baselines |

</details>

<details open>
<summary><b>⚙️ Terraform & DevSecOps Pipelines</b></summary>
<br>

```mermaid
flowchart LR
    A["📝 Git PR"] --> B["🧹 fmt · validate · tflint"]
    B --> C["🔍 Gitleaks · Checkov · Trivy · tfsec"]
    C --> D["💵 Infracost"]
    D --> E["📋 Plan artifact<br/>+ drift check"]
    E --> F{"👥 Approval gate<br/>UAT / Prod"}
    F -->|approved| G["🚀 Apply<br/>remote state, locked"]
    G -->|failure| H["↩️ Automated rollback"]
```

- **Remote state** in a private Azure Storage Account — blob-lease locking, encrypted at rest, reached via least-privilege Managed Identity
- **Reusable modules** with strict semantic versioning
- **Nightly drift detection** using `terraform plan -detailed-exitcode` to catch manual portal changes
- **Trunk-based development** with short-lived `feature/*` and `fix/*` branches
- **Branch policies on `main`:** no direct push, no delete, PR with 2 senior reviewers, `CODEOWNERS` enforced
- **Bootstrapping** via Cloud-Init / custom data for baseline config and agent install

</details>

<details>
<summary><b>🚚 End-to-End Cloud Migration (100+ workloads · Dev / UAT / Prod)</b></summary>
<br>

```mermaid
flowchart LR
    D["🔎 Discovery<br/>inventory & dependencies"] --> A["📐 Assessment<br/>compatibility & TCO"]
    A --> R["🏗️ Readiness<br/>landing zone ready"]
    R --> C["🔀 Cutover<br/>downtime window"]
    C --> H["🛟 Hypercare<br/>24x7 war room"]
```

| Phase | Checklist |
| :--- | :--- |
| **Pre-migration** | Azure Migrate discovery, dependency mapping, bandwidth sizing, landing zone verification, backup verification |
| **Cutover** | DB replication sync, DNS TTL reduction, traffic rerouting, validation tests |
| **Post-migration** | Health telemetry, user sanity testing, performance benchmarks, 2–4 weeks of hypercare |

</details>

<details>
<summary><b>💰 FinOps — Cloud Financial Management</b></summary>
<br>

- **Eliminate waste:** unattached disks, stale snapshots, orphaned public IPs, idle compute
- **Rightsize** using 30-day CPU/memory utilisation percentiles
- **Commit smartly:** 1- or 3-year Reserved Instances and Azure Savings Plans for steady-state load
- **Schedule** automatic start/stop for non-production outside business hours
- **Tune log ingestion** with Data Collection Rules to drop noisy diagnostics at the source

</details>

<details>
<summary><b>💾 Backup, DR & High Availability</b></summary>
<br>

| Concept | Approach |
| :--- | :--- |
| **Storage redundancy** | LRS (3 copies, 1 datacenter) → ZRS (3 zones) → GRS (paired region) |
| **HA compute** | VM Scale Sets across Availability Zones |
| **RTO** | Maximum tolerable downtime before service is restored |
| **RPO** | Maximum tolerable data loss, e.g. ≤ 15 minutes of transactions |
| **Region strategy** | Active primary region, Azure Site Recovery replicating to the paired region |

</details>

<details>
<summary><b>📡 Observability</b></summary>
<br>

- Central **Log Analytics Workspace** per landing zone
- **Azure Monitor Agent** with DCR filtering at source for cost and performance
- **Action Groups** routing alerts to Teams, Slack or PagerDuty by severity

</details>

<details>
<summary><b>🤝 Leadership, Vendor & Delivery Governance</b></summary>
<br>

```
RFI ─▶ RFP ─▶ Technical Evaluation Matrix ─▶ SOW & Commercials ─▶ Sprints & Milestones ─▶ Acceptance Sign-off
```

- **Team growth:** KT sessions, mentoring juniors, sitting on interview panels
- **Pre-sales:** estimates, POCs, RFP/RFI responses
- **Vendor governance:** SOW scope and acceptance criteria, scored evaluation matrices, SLA tracking
- **RACI & escalation matrices** so every deliverable has one accountable owner and a clear escalation path
- **Delivery hygiene:** SOPs, runbooks, incident retrospectives, ADRs, and structured handover before sign-off

</details>

---

## 🛠️ Tech Stack

**☁️ Cloud & Platform**<br>
![Azure](https://img.shields.io/badge/Microsoft_Azure-0089D6?style=for-the-badge&logo=microsoftazure&logoColor=white)
![Entra ID](https://img.shields.io/badge/Entra_ID-0078D4?style=for-the-badge&logo=microsoft&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonwebservices&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

**🏗️ IaC & Config Management**<br>
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white)
![Bicep](https://img.shields.io/badge/Bicep-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white)
![Ansible](https://img.shields.io/badge/Ansible-EE0000?style=for-the-badge&logo=ansible&logoColor=white)
![Cloud-Init](https://img.shields.io/badge/Cloud--Init-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)

**🔁 CI/CD & GitOps**<br>
![Azure DevOps](https://img.shields.io/badge/Azure_DevOps-0078D7?style=for-the-badge&logo=azuredevops&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)
![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

**📦 Containers & Orchestration**<br>
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![Helm](https://img.shields.io/badge/Helm-0F1689?style=for-the-badge&logo=helm&logoColor=white)

**🔐 DevSecOps**<br>
![Checkov](https://img.shields.io/badge/Checkov-4B32C3?style=for-the-badge&logo=paloaltonetworks&logoColor=white)
![Trivy](https://img.shields.io/badge/Trivy-1904DA?style=for-the-badge&logo=aqua&logoColor=white)
![Gitleaks](https://img.shields.io/badge/Gitleaks-DC3545?style=for-the-badge&logo=git&logoColor=white)
![SonarQube](https://img.shields.io/badge/SonarQube-4E9BCD?style=for-the-badge&logo=sonarqube&logoColor=white)
![Defender for Cloud](https://img.shields.io/badge/Defender_for_Cloud-0078D4?style=for-the-badge&logo=microsoft&logoColor=white)

**📡 Observability & FinOps**<br>
![Azure Monitor](https://img.shields.io/badge/Azure_Monitor-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white)
![Infracost](https://img.shields.io/badge/Infracost-DB44B8?style=for-the-badge&logo=terraform&logoColor=white)

**💻 Scripting**<br>
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white)
![PowerShell](https://img.shields.io/badge/PowerShell-5391FE?style=for-the-badge&logo=powershell&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![YAML](https://img.shields.io/badge/YAML-CB171E?style=for-the-badge&logo=yaml&logoColor=white)

<details>
<summary><b>👨‍💻 Software development background</b></summary>
<br>

![C#](https://img.shields.io/badge/C%23-239120?style=plastic&logo=c-sharp&logoColor=white)
![.NET](https://img.shields.io/badge/.NET-5C2D91?style=plastic&logo=.net&logoColor=white)
![VB.NET](https://img.shields.io/badge/VB.NET-5C2D91?style=plastic&logo=VB.net&logoColor=white)
![Java](https://img.shields.io/badge/Java-ED8B00?style=plastic&logo=openjdk&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-323330?style=plastic&logo=javascript&logoColor=F7DF1E)
![React](https://img.shields.io/badge/React-20232A?style=plastic&logo=react&logoColor=61DAFB)
![C++](https://img.shields.io/badge/C%2B%2B-00599C?style=plastic&logo=c%2B%2B&logoColor=white)
![MSSQL](https://img.shields.io/badge/MSSQL-CC2927?style=plastic&logo=microsoftsqlserver&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=plastic&logo=mysql&logoColor=white)
![PL/SQL](https://img.shields.io/badge/PL/SQL-F80000?style=plastic&logo=oracle&logoColor=white)
![Firebase](https://img.shields.io/badge/Firebase-039BE5?style=plastic&logo=firebase&logoColor=white)
![VS Code](https://img.shields.io/badge/VS_Code-0078D4?style=plastic&logo=visualstudiocode&logoColor=white)

</details>

---

## 🧭 How I Work

```
Business & Functional Domain
        │
        ├── Infrastructure Design ─▶ Landing Zones · IaC · DevSecOps · Migration · Governance · DR · FinOps
        │
        └── Application Design   ─▶ Microservices vs Monolith · API Gateway & Service Mesh · Caching · Event-Driven
```

> I work across the delivery chain — **Pre-Sales → TAM → Enterprise Architecture → Technical Lead** — so designs stay grounded in commercial reality and are actually shippable.

---

## 🌐 Connect

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/harsh4404/)
[![Medium](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@harshagarwal2225/)
[![LeetCode](https://img.shields.io/badge/LeetCode-FFA116?style=for-the-badge&logo=leetcode&logoColor=black)](https://leetcode.com/agarwal1102/)
[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-298D46?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://auth.geeksforgeeks.org/user/agarwal_harsh)
[![Linktree](https://img.shields.io/badge/Linktree-39E09B?style=for-the-badge&logo=linktree&logoColor=white)](https://linktr.ee/agarwal_harsh)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://instagram.com/harshagarwal_1102/)

---

## 📊 GitHub Stats

<p align="center">
  <img height="165" src="https://github-readme-stats.vercel.app/api?username=HarshAgarwal1102&theme=tokyonight&hide_border=true&include_all_commits=true&count_private=true" alt="GitHub stats" />
  <img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=HarshAgarwal1102&theme=tokyonight&hide_border=true&layout=compact" alt="Top languages" />
</p>
<p align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=HarshAgarwal1102&theme=tokyonight&hide_border=true" alt="GitHub streak" />
</p>

## 🏆 GitHub Trophies

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=HarshAgarwal1102&theme=radical&no-frame=true&no-bg=true&margin-w=15&margin-h=15&column=-1" alt="Trophies" />
</p>

## 🎮 Fun

<p align="center">
  <img src="https://github.com/HarshAgarwal1102/HarshAgarwal1102/assets/117922914/61d89383-610c-46c1-a1d8-b0b06e57a9c8" alt="dino" />
</p>

<p align="center"><i>“Automate the boring, govern the critical, and measure everything.”</i></p>
