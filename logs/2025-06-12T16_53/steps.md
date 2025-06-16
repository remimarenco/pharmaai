---

## Unknown Step

---

## Agent Action

**Thought:**
```
Okay, I will start by searching the ANSM website for information on Levothyrox, focusing on advice and points of vigilance.
```

**Action:** `EXASearchTool`

**Action Input:**
```
{"search_query": "Levothyrox conseils vigilance site:ansm.sante.fr", "start_published_date": null, "end_published_date": "2025-06-12", "include_domains": ["ansm.sante.fr"]}
```

---

## Unknown Step

---

## Agent Action

**Thought:**
```
Based on the search results from the ANSM website, multiple documents discuss Levothyrox, pharmacovigilance, and studies on the medication, but none provide simple readily-digestible advice or highlight specific points of vigilance directed to the patients taking the medication. Therefore, I will broaden the search to the Vidal website, which is more directed towards patient information.
```

**Action:** `EXASearchTool`

**Action Input:**
```
{"search_query": "Levothyrox conseils vigilance site:vidal.fr", "start_published_date": null, "end_published_date": "2025-06-12", "include_domains": ["vidal.fr"]}
```

---

## Unknown Step

---

## Agent Action

**Thought:**
```
Thought: The search on Vidal provided results mostly related to the history and availability surrounding the change in formula a few years ago, but it's outdated, so I will change to a more general search to see if there's a monograph that provides advice and vigilance information.
```

**Action:** `EXASearchTool`

**Action Input:**
```
{"search_query": "Levothyrox monograph conseils vigilance site:vidal.fr", "start_published_date": null, "end_published_date": "2025-06-12", "include_domains": ["vidal.fr"]}
```

---

## Unknown Step

---

## Agent Action

**Thought:**
```
Thought: The search results on Vidal still point towards the older issues with the change in formula, and do not have a specific monograph that provides the advice needed. Therefore, I will search for recommendations related to Hypothyroidism to try to get some answers from Vidal.
```

**Action:** `EXASearchTool`

**Action Input:**
```
{"search_query": "Hypothyro\u00efdie recommandations VIDAL", "start_published_date": null, "end_published_date": "2025-06-12", "include_domains": ["vidal.fr"]}
```

---

## Agent Finish

**Thought:**
```
Thought: I was able to find something here, so now I can use that data to provide the final answer.
```

**Output:**
```
```
Rapport de recherche structuré sur les conseils et points de vigilance concernant le Levothyrox (date de recherche: 2025-06-12):

1. Résumé des points d'information cruciaux:

*   L'ANSM a mené une étude de pharmaco-épidémiologie sur les conséquences du passage à la nouvelle formule du Levothyrox en France. Les résultats n'ont pas montré de toxicité propre de la nouvelle formule, mais ont souligné les difficultés rencontrées par certains patients lors du changement.
*   L'ANSM a également mené des enquêtes de pharmacovigilance sur les spécialités à base de lévothyroxine. Les analyses n'ont pas permis d'identifier de patients à risque ou de proposer d'hypothèses à la survenue des effets indésirables signalés. La surveillance se poursuit.
*   En cas de grossesse ou de désir de grossesse, un dépistage ciblé de l'hypothyroïdie est recommandé (dosage de la TSH). Des adaptations du traitement substitutif peuvent être nécessaires pendant la grossesse.

2. Liste détaillée des faits, données et recommandations extraits:

*   **ANSM - Étude de pharmaco-épidémiologie (2019, mise à jour 2021) :**
    *   L'étude a porté sur plus de 2 millions de patients.
    *   18% des patients ayant initié la nouvelle formule du Levothyrox entre avril et juin 2017 ont opté pour une autre spécialité à la fin de la même année.
    *   La fréquence des dosages de TSH a augmenté de 31% suite au passage à la nouvelle formule.
    *   Les résultats ne mettent pas en évidence d'augmentation spécifique de survenue d'hospitalisations, de décès, d'arrêts de travail d'au moins 7 jours, ni de consommation de médicaments utilisés pour traiter des symptômes somatiques.
    *   Une augmentation de 2% du nombre de consultations médicales, concentrée sur la période d'août à octobre 2017, a été observée.
    *   Une hausse relative de l'utilisation de certains médicaments comme les benzodiazépines suite au passage à la nouvelle formule du Levothyrox est également montrée.
*   **ANSM - Enquêtes nationales de pharmacovigilance (2018, mise à jour 2021) :**
    *   Le pourcentage de patients signalant des effets indésirables avec Levothyrox nouvelle formule est estimé à 1,43%.
    *   Le profil clinique d’effets indésirables rapportés avec Levothyrox nouvelle formule est semblable à celui de Levothyrox ancienne formule, mais avec une fréquence de signalement totalement inattendue.
    *   Une diminution très importante du nombre de signalements s’est amorcée depuis octobre 2017, expliquée par la mise à disposition des alternatives thérapeutiques.
    *   L’analyse des données recueillies dans le cadre de l’enquête étendue aux autres spécialités à base de levothyroxine ne met pas en évidence de signal particulier de pharmacovigilance.
*   **VIDAL - Hypothyroïdie de l'adulte (2025) :**
    *   Pendant la grossesse, la stimulation de la thyroïde est exacerbée et l'activité de la thyroïde augmente d'environ 50%.
    *   Le fœtus est totalement dépendant des hormones thyroïdiennes maternelles pendant le premier trimestre de grossesse.
    *   Conséquences de l'hypothyroïdie avérée pendant la grossesse : fausses-couches, infertilité, HTA gravidique, prématurité, petit poids de naissance, troubles du développement intellectuel.
    *   Dépistage de l'hypothyroïdie en cas de grossesse ou de désir de grossesse : dosage de la TSH en présence de symptômes évocateurs, antécédents personnels de dysthyroïdie, diabète de type 1, maladie auto-immune, radiothérapie cervicale, chirurgie thyroïdienne, traitement par amiodarone ou lithium, antécédent d'accouchement prématuré, de fausses-couches, de troubles de la fertilité, prise en charge en AMP, antécédent familial de dysthyroïdie.
    *   Recommandations en cas de TSH > 2,5 mUI/L chez la femme enceinte : dosage des Ac anti-TPO.
    *   Objectif de TSH pendant la grossesse : entre 0,4 mUI/L et 2,5 mUI/L.
    *   La liothyronine (LT3) est contre-indiquée chez la femme enceinte et l'association LT3-lévothyroxine est déconseillée.
    *   Surveillance de la TSH toutes les 4 à 6 semaines jusqu'à 22 SA, une fois entre 30 et 34 SA, puis en post-partum. Surveillance des Ac anti-TPO même sans traitement.

3. Liste des sources avec titre et URL complète:

*   Titre: Actualité - Levothyrox et médicaments à base de lévothyroxine : Rapport final de l’étude de pharmaco-épidémiologie à partir des données du Système National des Données de Santé (SNDS) - ANSM
    URL: [https://ansm.sante.fr/actualites/levothyrox-et-medicaments-a-base-de-levothyroxine-rapport-final-de-letude-de-pharmaco-epidemiologie-a-partir-des-donnees-du-systeme-national-des-donnees-de-sante-snds](https://ansm.sante.fr/actualites/levothyrox-et-medicaments-a-base-de-levothyroxine-rapport-final-de-letude-de-pharmaco-epidemiologie-a-partir-des-donnees-du-systeme-national-des-donnees-de-sante-snds)
*   Titre: Actualité - L’ANSM publie les résultats des enquêtes nationales de pharmacovigilance sur les spécialités à base de lévothyroxine - Communiqué - ANSM
    URL: [https://ansm.sante.fr/actualites/lansm-publie-les-resultats-des-enquetes-nationales-de-pharmacovigilance-sur-les-specialites-a-base-de-levothyroxine-communique](https://ansm.sante.fr/actualites/lansm-publie-les-resultats-des-enquetes-nationales-de-pharmacovigilance-sur-les-specialites-a-base-de-levothyroxine-communique)
*   Titre: Recommandations Hypothyroïdie de l'adulte - VIDAL
    URL: [https://www.vidal.fr/maladies/recommandations/hypothyroidie-de-l-adulte-1482.html](https://www.vidal.fr/maladies/recommandations/hypothyroidie-de-l-adulte-1482.html)
```
```

**Text:**
```
Thought: I was able to find something here, so now I can use that data to provide the final answer.
Final Answer:```
Rapport de recherche structuré sur les conseils et points de vigilance concernant le Levothyrox (date de recherche: 2025-06-12):

1. Résumé des points d'information cruciaux:

*   L'ANSM a mené une étude de pharmaco-épidémiologie sur les conséquences du passage à la nouvelle formule du Levothyrox en France. Les résultats n'ont pas montré de toxicité propre de la nouvelle formule, mais ont souligné les difficultés rencontrées par certains patients lors du changement.
*   L'ANSM a également mené des enquêtes de pharmacovigilance sur les spécialités à base de lévothyroxine. Les analyses n'ont pas permis d'identifier de patients à risque ou de proposer d'hypothèses à la survenue des effets indésirables signalés. La surveillance se poursuit.
*   En cas de grossesse ou de désir de grossesse, un dépistage ciblé de l'hypothyroïdie est recommandé (dosage de la TSH). Des adaptations du traitement substitutif peuvent être nécessaires pendant la grossesse.

2. Liste détaillée des faits, données et recommandations extraits:

*   **ANSM - Étude de pharmaco-épidémiologie (2019, mise à jour 2021) :**
    *   L'étude a porté sur plus de 2 millions de patients.
    *   18% des patients ayant initié la nouvelle formule du Levothyrox entre avril et juin 2017 ont opté pour une autre spécialité à la fin de la même année.
    *   La fréquence des dosages de TSH a augmenté de 31% suite au passage à la nouvelle formule.
    *   Les résultats ne mettent pas en évidence d'augmentation spécifique de survenue d'hospitalisations, de décès, d'arrêts de travail d'au moins 7 jours, ni de consommation de médicaments utilisés pour traiter des symptômes somatiques.
    *   Une augmentation de 2% du nombre de consultations médicales, concentrée sur la période d'août à octobre 2017, a été observée.
    *   Une hausse relative de l'utilisation de certains médicaments comme les benzodiazépines suite au passage à la nouvelle formule du Levothyrox est également montrée.
*   **ANSM - Enquêtes nationales de pharmacovigilance (2018, mise à jour 2021) :**
    *   Le pourcentage de patients signalant des effets indésirables avec Levothyrox nouvelle formule est estimé à 1,43%.
    *   Le profil clinique d’effets indésirables rapportés avec Levothyrox nouvelle formule est semblable à celui de Levothyrox ancienne formule, mais avec une fréquence de signalement totalement inattendue.
    *   Une diminution très importante du nombre de signalements s’est amorcée depuis octobre 2017, expliquée par la mise à disposition des alternatives thérapeutiques.
    *   L’analyse des données recueillies dans le cadre de l’enquête étendue aux autres spécialités à base de levothyroxine ne met pas en évidence de signal particulier de pharmacovigilance.
*   **VIDAL - Hypothyroïdie de l'adulte (2025) :**
    *   Pendant la grossesse, la stimulation de la thyroïde est exacerbée et l'activité de la thyroïde augmente d'environ 50%.
    *   Le fœtus est totalement dépendant des hormones thyroïdiennes maternelles pendant le premier trimestre de grossesse.
    *   Conséquences de l'hypothyroïdie avérée pendant la grossesse : fausses-couches, infertilité, HTA gravidique, prématurité, petit poids de naissance, troubles du développement intellectuel.
    *   Dépistage de l'hypothyroïdie en cas de grossesse ou de désir de grossesse : dosage de la TSH en présence de symptômes évocateurs, antécédents personnels de dysthyroïdie, diabète de type 1, maladie auto-immune, radiothérapie cervicale, chirurgie thyroïdienne, traitement par amiodarone ou lithium, antécédent d'accouchement prématuré, de fausses-couches, de troubles de la fertilité, prise en charge en AMP, antécédent familial de dysthyroïdie.
    *   Recommandations en cas de TSH > 2,5 mUI/L chez la femme enceinte : dosage des Ac anti-TPO.
    *   Objectif de TSH pendant la grossesse : entre 0,4 mUI/L et 2,5 mUI/L.
    *   La liothyronine (LT3) est contre-indiquée chez la femme enceinte et l'association LT3-lévothyroxine est déconseillée.
    *   Surveillance de la TSH toutes les 4 à 6 semaines jusqu'à 22 SA, une fois entre 30 et 34 SA, puis en post-partum. Surveillance des Ac anti-TPO même sans traitement.

3. Liste des sources avec titre et URL complète:

*   Titre: Actualité - Levothyrox et médicaments à base de lévothyroxine : Rapport final de l’étude de pharmaco-épidémiologie à partir des données du Système National des Données de Santé (SNDS) - ANSM
    URL: [https://ansm.sante.fr/actualites/levothyrox-et-medicaments-a-base-de-levothyroxine-rapport-final-de-letude-de-pharmaco-epidemiologie-a-partir-des-donnees-du-systeme-national-des-donnees-de-sante-snds](https://ansm.sante.fr/actualites/levothyrox-et-medicaments-a-base-de-levothyroxine-rapport-final-de-letude-de-pharmaco-epidemiologie-a-partir-des-donnees-du-systeme-national-des-donnees-de-sante-snds)
*   Titre: Actualité - L’ANSM publie les résultats des enquêtes nationales de pharmacovigilance sur les spécialités à base de lévothyroxine - Communiqué - ANSM
    URL: [https://ansm.sante.fr/actualites/lansm-publie-les-resultats-des-enquetes-nationales-de-pharmacovigilance-sur-les-specialites-a-base-de-levothyroxine-communique](https://ansm.sante.fr/actualites/lansm-publie-les-resultats-des-enquetes-nationales-de-pharmacovigilance-sur-les-specialites-a-base-de-levothyroxine-communique)
*   Titre: Recommandations Hypothyroïdie de l'adulte - VIDAL
    URL: [https://www.vidal.fr/maladies/recommandations/hypothyroidie-de-l-adulte-1482.html](https://www.vidal.fr/maladies/recommandations/hypothyroidie-de-l-adulte-1482.html)
```
```

---

## Agent Finish

**Thought:**
```
I now can give a great answer
```

**Output:**
```
TITRE: Levothyrox : Conseils et points de vigilance à l'officine
POINTS_CLES: - Surveillance de la TSH chez les patients sous Levothyrox, particulièrement lors d'un changement de formule. - Importance du dépistage de l'hypothyroïdie chez la femme enceinte ou ayant un projet de grossesse. - Suivi rigoureux de la TSH pendant la grossesse avec adaptation posologique si nécessaire.
SECTION: Levothyrox et nouvelle formule CONTENU: Une étude de pharmaco-épidémiologie de l'ANSM n'a pas mis en évidence de toxicité propre de la nouvelle formule du Levothyrox, mais a souligné des difficultés rencontrées par certains patients (ANSM - Étude de pharmaco-épidémiologie (2019, mise à jour 2021) : [https://ansm.sante.fr/actualites/levothyrox-et-medicaments-a-base-de-levothyroxine-rapport-final-de-letude-de-pharmaco-epidemiologie-a-partir-des-donnees-du-systeme-national-des-donnees-de-sante-snds](https://ansm.sante.fr/actualites/levothyrox-et-medicaments-a-base-de-levothyroxine-rapport-final-de-letude-de-pharmaco-epidemiologie-a-partir-des-donnees-du-systeme-national-des-donnees-de-sante-snds)). Les enquêtes de pharmacovigilance n'ont pas identifié de patients à risque particulier (ANSM - Enquêtes nationales de pharmacovigilance (2018, mise à jour 2021) : [https://ansm.sante.fr/actualites/lansm-publie-les-resultats-des-enquetes-nationales-de-pharmacovigilance-sur-les-specialites-a-base-de-levothyroxine-communique](https://ansm.sante.fr/actualites/lansm-publie-les-resultats-des-enquetes-nationales-de-pharmacovigilance-sur-les-specialites-a-base-de-levothyroxine-communique)).
SOUS_SECTION: Impact du changement de formule POINTS: - Augmentation des dosages de TSH suite au passage à la nouvelle formule (ANSM - Étude de pharmaco-épidémiologie (2019, mise à jour 2021) : [https://ansm.sante.fr/actualites/levothyrox-et-medicaments-a-base-de-levothyroxine-rapport-final-de-letude-de-pharmaco-epidemiologie-a-partir-des-donnees-du-systeme-national-des-donnees-de-sante-snds](https://ansm.sante.fr/actualites/levothyrox-et-medicaments-a-base-de-levothyroxine-rapport-final-de-letude-de-pharmaco-epidemiologie-a-partir-des-donnees-du-systeme-national-des-donnees-de-sante-snds)). - Augmentation des consultations médicales et de l'utilisation de benzodiazépines (ANSM - Étude de pharmaco-épidémiologie (2019, mise à jour 2021) : [https://ansm.sante.fr/actualites/levothyrox-et-medicaments-a-base-de-levothyroxine-rapport-final-de-letude-de-pharmaco-epidemiologie-a-partir-des-donnees-du-systeme-national-des-donnees-de-sante-snds](https://ansm.sante.fr/actualites/levothyrox-et-medicaments-a-base-de-levothyroxine-rapport-final-de-letude-de-pharmaco-epidemiologie-a-partir-des-donnees-du-systeme-national-des-donnees-de-sante-snds)). - Profil d'effets indésirables similaire à l'ancienne formule, mais fréquence de signalement inattendue (ANSM - Enquêtes nationales de pharmacovigilance (2018, mise à jour 2021) : [https://ansm.sante.fr/actualites/lansm-publie-les-resultats-des-enquetes-nationales-de-pharmacovigilance-sur-les-specialites-a-base-de-levothyroxine-communique](https://ansm.sante.fr/actualites/lansm-publie-les-resultats-des-enquetes-nationales-de-pharmacovigilance-sur-les-specialites-a-base-de-levothyroxine-communique)).
SECTION: Hypothyroïdie et Grossesse CONTENU: Un dépistage ciblé de l'hypothyroïdie est recommandé en cas de grossesse ou de désir de grossesse (VIDAL - Hypothyroïdie de l'adulte (2025) : [https://www.vidal.fr/maladies/recommandations/hypothyroidie-de-l-adulte-1482.html](https://www.vidal.fr/maladies/recommandations/hypothyroidie-de-l-adulte-1482.html)). La surveillance de la TSH est essentielle pendant toute la grossesse avec un objectif entre 0,4 et 2,5 mUI/L (VIDAL - Hypothyroïdie de l'adulte (2025) : [https://www.vidal.fr/maladies/recommandations/hypothyroidie-de-l-adulte-1482.html](https://www.vidal.fr/maladies/recommandations/hypothyroidie-de-l-adulte-1482.html)). La liothyronine (LT3) est contre-indiquée pendant la grossesse (VIDAL - Hypothyroïdie de l'adulte (2025) : [https://www.vidal.fr/maladies/recommandations/hypothyroidie-de-l-adulte-1482.html](https://www.vidal.fr/maladies/recommandations/hypothyroidie-de-l-adulte-1482.html)).
SOURCES: - [https://ansm.sante.fr/actualites/levothyrox-et-medicaments-a-base-de-levothyroxine-rapport-final-de-letude-de-pharmaco-epidemiologie-a-partir-des-donnees-du-systeme-national-des-donnees-de-sante-snds](https://ansm.sante.fr/actualites/levothyrox-et-medicaments-a-base-de-levothyroxine-rapport-final-de-letude-de-pharmaco-epidemiologie-a-partir-des-donnees-du-systeme-national-des-donnees-de-sante-snds) - [https://ansm.sante.fr/actualites/lansm-publie-les-resultats-des-enquetes-nationales-de-pharmacovigilance-sur-les-specialites-a-base-de-levothyroxine-communique](https://ansm.sante.fr/actualites/lansm-publie-les-resultats-des-enquetes-nationales-de-pharmacovigilance-sur-les-specialites-a-base-de-levothyroxine-communique) - [https://www.vidal.fr/maladies/recommandations/hypothyroidie-de-l-adulte-1482.html](https://www.vidal.fr/maladies/recommandations/hypothyroidie-de-l-adulte-1482.html)
```

**Text:**
```
I now can give a great answer
Final Answer:
TITRE: Levothyrox : Conseils et points de vigilance à l'officine
POINTS_CLES: - Surveillance de la TSH chez les patients sous Levothyrox, particulièrement lors d'un changement de formule. - Importance du dépistage de l'hypothyroïdie chez la femme enceinte ou ayant un projet de grossesse. - Suivi rigoureux de la TSH pendant la grossesse avec adaptation posologique si nécessaire.
SECTION: Levothyrox et nouvelle formule CONTENU: Une étude de pharmaco-épidémiologie de l'ANSM n'a pas mis en évidence de toxicité propre de la nouvelle formule du Levothyrox, mais a souligné des difficultés rencontrées par certains patients (ANSM - Étude de pharmaco-épidémiologie (2019, mise à jour 2021) : [https://ansm.sante.fr/actualites/levothyrox-et-medicaments-a-base-de-levothyroxine-rapport-final-de-letude-de-pharmaco-epidemiologie-a-partir-des-donnees-du-systeme-national-des-donnees-de-sante-snds](https://ansm.sante.fr/actualites/levothyrox-et-medicaments-a-base-de-levothyroxine-rapport-final-de-letude-de-pharmaco-epidemiologie-a-partir-des-donnees-du-systeme-national-des-donnees-de-sante-snds)). Les enquêtes de pharmacovigilance n'ont pas identifié de patients à risque particulier (ANSM - Enquêtes nationales de pharmacovigilance (2018, mise à jour 2021) : [https://ansm.sante.fr/actualites/lansm-publie-les-resultats-des-enquetes-nationales-de-pharmacovigilance-sur-les-specialites-a-base-de-levothyroxine-communique](https://ansm.sante.fr/actualites/lansm-publie-les-resultats-des-enquetes-nationales-de-pharmacovigilance-sur-les-specialites-a-base-de-levothyroxine-communique)).
SOUS_SECTION: Impact du changement de formule POINTS: - Augmentation des dosages de TSH suite au passage à la nouvelle formule (ANSM - Étude de pharmaco-épidémiologie (2019, mise à jour 2021) : [https://ansm.sante.fr/actualites/levothyrox-et-medicaments-a-base-de-levothyroxine-rapport-final-de-letude-de-pharmaco-epidemiologie-a-partir-des-donnees-du-systeme-national-des-donnees-de-sante-snds](https://ansm.sante.fr/actualites/levothyrox-et-medicaments-a-base-de-levothyroxine-rapport-final-de-letude-de-pharmaco-epidemiologie-a-partir-des-donnees-du-systeme-national-des-donnees-de-sante-snds)). - Augmentation des consultations médicales et de l'utilisation de benzodiazépines (ANSM - Étude de pharmaco-épidémiologie (2019, mise à jour 2021) : [https://ansm.sante.fr/actualites/levothyrox-et-medicaments-a-base-de-levothyroxine-rapport-final-de-letude-de-pharmaco-epidemiologie-a-partir-des-donnees-du-systeme-national-des-donnees-de-sante-snds](https://ansm.sante.fr/actualites/levothyrox-et-medicaments-a-base-de-levothyroxine-rapport-final-de-letude-de-pharmaco-epidemiologie-a-partir-des-donnees-du-systeme-national-des-donnees-de-sante-snds)). - Profil d'effets indésirables similaire à l'ancienne formule, mais fréquence de signalement inattendue (ANSM - Enquêtes nationales de pharmacovigilance (2018, mise à jour 2021) : [https://ansm.sante.fr/actualites/lansm-publie-les-resultats-des-enquetes-nationales-de-pharmacovigilance-sur-les-specialites-a-base-de-levothyroxine-communique](https://ansm.sante.fr/actualites/lansm-publie-les-resultats-des-enquetes-nationales-de-pharmacovigilance-sur-les-specialites-a-base-de-levothyroxine-communique)).
SECTION: Hypothyroïdie et Grossesse CONTENU: Un dépistage ciblé de l'hypothyroïdie est recommandé en cas de grossesse ou de désir de grossesse (VIDAL - Hypothyroïdie de l'adulte (2025) : [https://www.vidal.fr/maladies/recommandations/hypothyroidie-de-l-adulte-1482.html](https://www.vidal.fr/maladies/recommandations/hypothyroidie-de-l-adulte-1482.html)). La surveillance de la TSH est essentielle pendant toute la grossesse avec un objectif entre 0,4 et 2,5 mUI/L (VIDAL - Hypothyroïdie de l'adulte (2025) : [https://www.vidal.fr/maladies/recommandations/hypothyroidie-de-l-adulte-1482.html](https://www.vidal.fr/maladies/recommandations/hypothyroidie-de-l-adulte-1482.html)). La liothyronine (LT3) est contre-indiquée pendant la grossesse (VIDAL - Hypothyroïdie de l'adulte (2025) : [https://www.vidal.fr/maladies/recommandations/hypothyroidie-de-l-adulte-1482.html](https://www.vidal.fr/maladies/recommandations/hypothyroidie-de-l-adulte-1482.html)).
SOURCES: - [https://ansm.sante.fr/actualites/levothyrox-et-medicaments-a-base-de-levothyroxine-rapport-final-de-letude-de-pharmaco-epidemiologie-a-partir-des-donnees-du-systeme-national-des-donnees-de-sante-snds](https://ansm.sante.fr/actualites/levothyrox-et-medicaments-a-base-de-levothyroxine-rapport-final-de-letude-de-pharmaco-epidemiologie-a-partir-des-donnees-du-systeme-national-des-donnees-de-sante-snds) - [https://ansm.sante.fr/actualites/lansm-publie-les-resultats-des-enquetes-nationales-de-pharmacovigilance-sur-les-specialites-a-base-de-levothyroxine-communique](https://ansm.sante.fr/actualites/lansm-publie-les-resultats-des-enquetes-nationales-de-pharmacovigilance-sur-les-specialites-a-base-de-levothyroxine-communique) - [https://www.vidal.fr/maladies/recommandations/hypothyroidie-de-l-adulte-1482.html](https://www.vidal.fr/maladies/recommandations/hypothyroidie-de-l-adulte-1482.html)
```

---

## Agent Finish

**Thought:**
```
I can now give a great answer.
```

**Output:**
```
# Levothyrox : Conseils et points de vigilance à l'officine

> #### Points Clés à Retenir
> * Surveillance de la TSH chez les patients sous Levothyrox, particulièrement lors d'un changement de formule.
> * Importance du dépistage de l'hypothyroïdie chez la femme enceinte ou ayant un projet de grossesse.
> * Suivi rigoureux de la TSH pendant la grossesse avec adaptation posologique si nécessaire.

## Levothyrox et nouvelle formule

Une étude de pharmaco-épidémiologie de l'ANSM n'a pas mis en évidence de toxicité propre de la nouvelle formule du Levothyrox. Cependant, cette étude a souligné les difficultés rencontrées par certains patients. Les enquêtes de pharmacovigilance n'ont quant à elles pas identifié de patients à risque particulier.

### Impact du changement de formule

*   Augmentation des dosages de TSH suite au passage à la nouvelle formule.
*   Augmentation des consultations médicales et de l'utilisation de benzodiazépines.
*   Profil d'effets indésirables similaire à l'ancienne formule, mais fréquence de signalement inattendue.

## Hypothyroïdie et Grossesse

Un dépistage ciblé de l'hypothyroïdie est recommandé en cas de grossesse ou de désir de grossesse. La surveillance de la TSH est essentielle pendant toute la grossesse, avec un objectif entre 0,4 et 2,5 mUI/L. Il est important de noter que la liothyronine (LT3) est contre-indiquée pendant la grossesse.

## Sources

*   [Levothyrox et médicaments à base de levothyroxine : rapport final de l'étude de pharmaco-épidémiologie à partir des données du système national des données de santé (SNDS)](https://ansm.sante.fr/actualites/levothyrox-et-medicaments-a-base-de-levothyroxine-rapport-final-de-letude-de-pharmaco-epidemiologie-a-partir-des-donnees-du-systeme-national-des-donnees-de-sante-snds)
*   [L'ANSM publie les résultats des enquêtes nationales de pharmacovigilance sur les spécialités à base de levothyroxine - Communiqué](https://ansm.sante.fr/actualites/lansm-publie-les-resultats-des-enquetes-nationales-de-pharmacovigilance-sur-les-specialites-a-base-de-levothyroxine-communique)
*   [Hypothyroïdie de l'adulte](https://www.vidal.fr/maladies/recommandations/hypothyroidie-de-l-adulte-1482.html)
```

**Text:**
```
I can now give a great answer.
Final Answer:
# Levothyrox : Conseils et points de vigilance à l'officine

> #### Points Clés à Retenir
> * Surveillance de la TSH chez les patients sous Levothyrox, particulièrement lors d'un changement de formule.
> * Importance du dépistage de l'hypothyroïdie chez la femme enceinte ou ayant un projet de grossesse.
> * Suivi rigoureux de la TSH pendant la grossesse avec adaptation posologique si nécessaire.

## Levothyrox et nouvelle formule

Une étude de pharmaco-épidémiologie de l'ANSM n'a pas mis en évidence de toxicité propre de la nouvelle formule du Levothyrox. Cependant, cette étude a souligné les difficultés rencontrées par certains patients. Les enquêtes de pharmacovigilance n'ont quant à elles pas identifié de patients à risque particulier.

### Impact du changement de formule

*   Augmentation des dosages de TSH suite au passage à la nouvelle formule.
*   Augmentation des consultations médicales et de l'utilisation de benzodiazépines.
*   Profil d'effets indésirables similaire à l'ancienne formule, mais fréquence de signalement inattendue.

## Hypothyroïdie et Grossesse

Un dépistage ciblé de l'hypothyroïdie est recommandé en cas de grossesse ou de désir de grossesse. La surveillance de la TSH est essentielle pendant toute la grossesse, avec un objectif entre 0,4 et 2,5 mUI/L. Il est important de noter que la liothyronine (LT3) est contre-indiquée pendant la grossesse.

## Sources

*   [Levothyrox et médicaments à base de levothyroxine : rapport final de l'étude de pharmaco-épidémiologie à partir des données du système national des données de santé (SNDS)](https://ansm.sante.fr/actualites/levothyrox-et-medicaments-a-base-de-levothyroxine-rapport-final-de-letude-de-pharmaco-epidemiologie-a-partir-des-donnees-du-systeme-national-des-donnees-de-sante-snds)
*   [L'ANSM publie les résultats des enquêtes nationales de pharmacovigilance sur les spécialités à base de levothyroxine - Communiqué](https://ansm.sante.fr/actualites/lansm-publie-les-resultats-des-enquetes-nationales-de-pharmacovigilance-sur-les-specialites-a-base-de-levothyroxine-communique)
*   [Hypothyroïdie de l'adulte](https://www.vidal.fr/maladies/recommandations/hypothyroidie-de-l-adulte-1482.html)
```

