# -*- coding: utf-8 -*-
"""
Genere le fichier CSV du planning detaille de l'Objectif 1, dans le format
attendu par l'import CSV de GanttProject (en-tetes anglais, dates ISO,
section taches + section ressources separees par deux lignes vides).

Usage :
    python generate_gantt_ganttproject_csv.py

Sortie :
    gantt_objectif1_ganttproject.csv (dans le meme dossier)

Voir le mode d'emploi d'import dans rendu/CST_Objectif1_Furious_Ducks_FINAL.md
(section I.3) et dans todo/01_Objectif1_Reste_A_Faire.md.
"""

import datetime

tasks = [
    (1, 'Cadrage besoin et hypotheses', 1, [], 'CDP', 282),
    (2, 'Redaction cahier technique (sections A-E)', 2, [1], 'CDP;DEVOPS', 1080),
    (3, 'Revue et validation du cahier', 1, [2], 'CDP', 282),
    (4, 'Souscription serveur dedie', 1, [3], 'CDP', 282),
    (5, 'Configuration systeme Linux', 2, [4], 'DEVOPS', 516),
    (6, 'Reseau Docker (zones)', 1, [5], 'DEVOPS', 258),
    (7, 'Achat domaine et configuration DNS', 1, [4], 'CDP', 282),
    (8, 'Deploiement Traefik', 1, [6], 'DEVOPS', 258),
    (9, 'Deploiement Gitea + Postgres', 1, [8], 'DEVOPS', 258),
    (10, 'Deploiement Jenkins', 1, [8], 'DEVOPS', 258),
    (11, 'Deploiement Docker Registry', 1, [8], 'DEVOPS', 258),
    (12, 'Comptes nominatifs et acces', 1, [9, 10, 11], 'DEVOPS', 258),
    (13, 'Tests de connectivite inter-services', 1, [12], 'DEV', 226),
    (14, 'Ecriture du Jenkinsfile declaratif', 2, [13], 'DEV', 452),
    (15, 'Pipeline dev automatise', 1, [14], 'DEVOPS', 258),
    (16, 'Pipeline preprod automatise', 1, [15], 'DEVOPS', 258),
    (17, 'Pipeline prod + validation manuelle', 1, [16], 'DEVOPS', 258),
    (18, 'Deploiement Prometheus + exporters', 1, [13], 'DEVOPS', 258),
    (19, 'Deploiement Grafana + dashboards', 1, [18], 'DEVOPS', 258),
    (20, 'Deploiement Uptime Kuma', 1, [13], 'DEVOPS', 258),
    (21, 'Script de sauvegarde Restic', 1, [13], 'DEVOPS', 258),
    (22, 'Test de restauration isole', 1, [21], 'DEVOPS', 258),
    (23, 'Durcissement securite (secrets scans)', 1, [12], 'DEVOPS', 258),
    (24, 'Redaction procedures BPMN-UML', 1, [17, 22], 'CDP', 282),
    (25, 'Fiche de poste et plan de formation', 1, [3], 'CDP', 282),
    (26, 'Consolidation finale du cahier', 1, [24, 25], 'CDP', 282),
    (27, 'Preparation support de soutenance', 1, [26], 'CDP;DEVOPS', 540),
    (28, 'Revue finale - dossier complet', 1, [27], 'CDP', 282),
    (101, 'J1 - Architecture cible validee', 0, [3], '', 0),
    (102, 'J2 - Pipeline bout en bout demontrable', 0, [17], '', 0),
    (103, 'J3 - Sauvegarde-restauration testees', 0, [22], '', 0),
    (104, 'J4 - Documentation et fiche de poste finalisees', 0, [24, 25], '', 0),
    (105, 'J5 - Dossier complet pret', 0, [28], '', 0),
]


def add_business_days(start, n):
    d = start
    count = 0
    while count < n:
        d += datetime.timedelta(days=1)
        if d.weekday() < 5:
            count += 1
    return d


project_start = datetime.date(2026, 3, 2)  # lundi

begin = {}
end = {}
for tid, name, dur, preds, res, cost in tasks:
    if not preds:
        b = project_start
    else:
        last_pred_end = max(end[p] for p in preds)
        b = last_pred_end if dur == 0 else add_business_days(last_pred_end, 1)
    if dur <= 1:
        e = b
    else:
        e = add_business_days(b, dur - 1)
    begin[tid] = b
    end[tid] = e

lines = []
lines.append("ID,Name,Begin date,End date,Duration,Completion,Cost,Predecessors,Resources,Notes")
for tid, name, dur, preds, res, cost in tasks:
    preds_str = ";".join(str(p) for p in preds)
    lines.append(f"{tid},{name},{begin[tid].isoformat()},{end[tid].isoformat()},{dur},0,{cost},{preds_str},{res},")

lines.append("")
lines.append("")
lines.append("ID,Name,Default role,Standard Rate")
lines.append("1,CDP,Chef de projet,282")
lines.append("2,DEVOPS,Ingenieur DevOps,258")
lines.append("3,DEV,Developpeur,226")

out_path = "gantt_objectif1_ganttproject.csv"
with open(out_path, "w", encoding="utf-8", newline="\r\n") as f:
    f.write("\n".join(lines) + "\n")

print("Fichier ecrit :", out_path)
print("Dernier jour du projet :", end[28].isoformat())
