# Objectif n°1 - Diagrammes infrastructure et procédures (BPMN)

## 1) Diagramme d'infrastructure complet (workflow)

```mermaid
flowchart LR
    Internet[Internet] --> ReverseProxy["Traefik ReverseProxy 443"]
    ReverseProxy --> Jenkins["Jenkins 8080 interne"]
    ReverseProxy --> Gitea["Gitea 3000 interne"]
    ReverseProxy --> Registry["DockerRegistry 5000 interne"]
    ReverseProxy --> Grafana["Grafana 3000 interne"]
    ReverseProxy --> AppDev["AppDev"]
    ReverseProxy --> AppPreprod["AppPreprod"]
    ReverseProxy --> AppProd["AppProd"]

    Developer[Developer] -->|"push/pull"| Gitea
    Gitea -->|"webhook"| Jenkins
    Jenkins -->|"build/test/push image"| Registry
    Jenkins -->|"deploy auto"| AppDev
    Jenkins -->|"promote auto"| AppPreprod
    Jenkins -->|"approval + deploy"| AppProd

    Prometheus["Prometheus 9090 interne"] --> Grafana
    Jenkins --> Prometheus
    Gitea --> Prometheus
    Registry --> Prometheus
    AppDev --> Prometheus
    AppPreprod --> Prometheus
    AppProd --> Prometheus

    Restic["Restic Backup"] --> BackupStore["BackupStorage distant"]
    Jenkins --> Restic
    Gitea --> Restic
    Registry --> Restic
    Prometheus --> Restic
```



## 2) Procédure de déploiement dev/preprod/prod

```mermaid
flowchart TD
    devCommit[Commit feature] --> prOpen[PullRequest vers develop]
    prOpen --> ciTrigger[Jenkins pipeline trigger]
    ciTrigger --> lintTests[Lint + tests unitaires]
    lintTests --> buildImage[Build image Docker]
    buildImage --> pushRegistry[Push image registry]
    pushRegistry --> deployDev[Deploy automatique dev]
    deployDev --> smokeDev[Smoke tests dev]
    smokeDev --> deployPreprod[Deploy automatique preprod]
    deployPreprod --> smokePreprod[Smoke tests preprod]
    smokePreprod --> prodApproval[Validation manuelle release]
    prodApproval --> deployProd[Deploy prod]
    deployProd --> smokeProd[Smoke test prod]
    smokeProd --> closeRelease[Release validée]
```



## 3) Procédure de sauvegarde automatisée

```mermaid
flowchart TD
    schedStart[Planification quotidienne] --> freezeCheck[Check état services]
    freezeCheck --> snapshotVolumes[Snapshot volumes critiques]
    snapshotVolumes --> encryptArchive[Chiffrement archive]
    encryptArchive --> uploadRemote[Upload stockage distant]
    uploadRemote --> verifyIntegrity[Contrôle intégrité backup]
    verifyIntegrity --> reportBackup[Rapport succès/échec]
    reportBackup --> alertOnFail[Alerting si échec]
```



## 4) Procédure de restauration (dev/preprod/prod)

```mermaid
flowchart TD
    incidentOpen[Incident ou perte de données] --> qualifyImpact[Qualifier impact]
    qualifyImpact --> chooseRestorePoint[Choisir point de restauration]
    chooseRestorePoint --> restoreIsolated[Restaurer sur environnement isolé]
    restoreIsolated --> runValidation[Tests de validation]
    runValidation --> decisionGo[Validation GO]
    decisionGo --> switchTraffic[Basculer trafic ou redeployer]
    switchTraffic --> postChecks[Contrôles post-restauration]
    postChecks --> incidentClose[Clôture incident + REX]
```



## 5) Procédure de gestion d'incident critique

```mermaid
flowchart TD
    alertRaised[Alerte monitoring] --> triageIncident[Triage et criticité]
    triageIncident --> assignOwner[Affectation responsable]
    assignOwner --> mitigateNow[Mesure conservatoire immédiate]
    mitigateNow --> rollbackOrFix[Rollback ou correctif]
    rollbackOrFix --> validateService[Validation service rétabli]
    validateService --> commsClient[Communication parties prenantes]
    commsClient --> postMortem[PostMortem + actions préventives]
```



## 6) Table flux/ports/protocoles (à insérer dans le cahier)


| Source        | Destination        | Port      | Protocole     | Usage                     |
| ------------- | ------------------ | --------- | ------------- | ------------------------- |
| Internet      | Reverse proxy      | 443       | HTTPS         | Accès externe outils/apps |
| Reverse proxy | Jenkins            | 8080      | HTTP interne  | UI/API Jenkins            |
| Reverse proxy | Gitea              | 3000      | HTTP interne  | UI/API SCM                |
| Jenkins       | Registry           | 5000      | HTTPS interne | Push/Pull images          |
| Jenkins       | Environnements app | 22/443    | SSH/HTTPS     | Déploiement               |
| Prometheus    | Services monitorés | variables | HTTP metrics  | Collecte métriques        |
| Services      | Backup distant     | 443       | HTTPS         | Sauvegardes externalisées |


