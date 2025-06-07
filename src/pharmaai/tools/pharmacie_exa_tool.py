# Fichier: custom_tools/pharmacie_exa_tool.py

import os
from typing import Type, Any, Optional, List

from exa_py import Exa # SDK officiel d'Exa
from langchain_core.tools import BaseTool # Classe de base pour les outils Langchain/CrewAI
from pydantic.v1 import BaseModel, Field, PrivateAttr # Pour la validation des arguments et les attributs privés

# 1. Définir le schéma d'entrée (les arguments que l'outil acceptera)
class PharmacieExaSearchSchema(BaseModel):
    query: Optional[str] = Field(
        default=None,
        description="La requête de recherche principale en langage naturel ou par mots-clés pour l'API /search."
    )
    find_similar_url: Optional[str] = Field(
        default=None,
        description="URL d'un document pertinent pour trouver des contenus similaires via l'API /findSimilar. Si fourni, la 'query' peut être utilisée pour affiner les highlights."
    )
    num_results: Optional[int] = Field(
        default=5,
        description="Nombre de résultats de recherche à retourner."
    )
    include_domains: Optional[List[str]] = Field(
        default=None,
        description="Liste de domaines à inclure prioritairement (ex: ['ansm.sante.fr']). Si non fourni ou si la liste est vide et que `use_default_trusted_domains` est True, une liste de domaines de confiance par défaut sera utilisée."
    )
    exclude_domains: Optional[List[str]] = Field(
        default=None,
        description="Liste de domaines à exclure de la recherche."
    )
    start_published_date: Optional[str] = Field(
        default=None,
        description="Date de début de publication (format YYYY-MM-DD) pour filtrer les résultats."
    )
    end_published_date: Optional[str] = Field(
        default=None,
        description="Date de fin de publication (format YYYY-MM-DD) pour filtrer les résultats."
    )
    search_type: Optional[str] = Field(
        default='neural',
        description="Type de recherche pour l'API /search : 'neural' (sémantique) ou 'keyword'."
    )
    category: Optional[str] = Field(
        default=None,
        description="Catégorie de contenu à cibler pour l'API /search (ex: 'government_document', 'research_paper', 'news_article'). Consulter la documentation Exa pour les catégories valides."
    )
    use_highlights: Optional[bool] = Field(
        default=False,
        description="Si True, demande à Exa de retourner des 'highlights' (extraits pertinents) au lieu du texte complet."
    )
    max_chars_content: Optional[int] = Field(
        default=2500,
        description="Nombre maximal de caractères à retourner pour le contenu textuel de chaque résultat si use_highlights est False."
    )
    use_default_trusted_domains: Optional[bool] = Field(
        default=True,
        description="Si True et que include_domains n'est pas fourni ou est vide, utilise la liste interne de domaines de confiance."
    )

# 2. Créer la classe de l'outil en héritant de BaseTool
class PharmacieExaSearchTool(BaseTool):
    name: str = "Recherche Avancée Exa pour la Pharmacie"
    description: str = (
        "Effectue des recherches web avancées via l'API Exa, optimisées pour les besoins pharmaceutiques français. "
        "Permet de rechercher par requête (sémantique ou mot-clé), de trouver des documents similaires à une URL, "
        "et d'appliquer des filtres stricts sur les domaines (avec une priorisation des sites français officiels), "
        "les dates de publication, et les catégories de documents. Peut retourner des extraits (highlights) ou du texte."
    )
    args_schema: Type[BaseModel] = PharmacieExaSearchSchema
    
    exa: Exa = PrivateAttr() # Client Exa, initialisé dans __init__

    default_trusted_domains_list: List[str] = [
        "ansm.sante.fr", "has-sante.fr", "ordre.pharmacien.fr", "vidal.fr",
        "lemoniteurdespharmacies.fr", "thesorimed.fr", "meddispar.fr", "lecrat.fr",
        "www.mesvaccins.net", "www.ameli.fr", "www.revue-prescrire.org",
        "www.santepubliquefrance.fr", "www.ema.europa.eu", "sfpc.eu", # Société Française de Pharmacie Clinique
        "sfpo.com", # Société Française de Pharmacie Oncologique
        # Sites OMEDIT (exemples, à compléter/adapter selon les régions d'intérêt)
        "omedit-grandest.fr", "omedit Normandie", "omedit Bretagne", "omedit Centre-Val de Loire",
        "sante.gouv.fr" # Site du Ministère de la Santé
    ]

    def __init__(self, exa_api_key: Optional[str] = None, **kwargs: Any):
        super().__init__(**kwargs)
        _exa_api_key = exa_api_key or os.environ.get("EXA_API_KEY")
        if not _exa_api_key:
            raise ValueError(
                "Clé API EXA (EXA_API_KEY) non trouvée. Veuillez la définir dans vos variables d'environnement ou la passer à l'outil."
            )
        self.exa = Exa(api_key=_exa_api_key)

    def _run(
        self,
        query: Optional[str] = None,
        find_similar_url: Optional[str] = None,
        num_results: int = 5,
        include_domains: Optional[List[str]] = None,
        exclude_domains: Optional[List[str]] = None,
        start_published_date: Optional[str] = None,
        end_published_date: Optional[str] = None,
        search_type: str = 'neural',
        category: Optional[str] = None,
        use_highlights: bool = False,
        max_chars_content: int = 2500,
        use_default_trusted_domains: bool = True
    ) -> str:
        
        final_include_domains = None
        if include_domains: # Si l'agent fournit une liste, on l'utilise
            final_include_domains = include_domains
        elif use_default_trusted_domains: # Sinon, si use_default est True, on utilise notre liste par défaut
            final_include_domains = self.default_trusted_domains_list
        # Si include_domains est une liste vide explicite ET use_default_trusted_domains est False, alors final_include_domains reste None (pas de filtre).

        contents_options = {}
        if use_highlights:
            highlights_config = {"num_sentences": 5, "highlights_per_url": 1}
            # Pour find_similar, la query des highlights doit être passée explicitement si on veut des highlights pertinents à cette query
            if find_similar_url and query:
                highlights_config["query"] = query
            contents_options["highlights"] = highlights_config
        else:
            contents_options["text"] = {"max_characters": max_chars_content, "include_html_tags": False}
        
        common_params = {
            "num_results": num_results,
            "include_domains": final_include_domains,
            "exclude_domains": exclude_domains,
            "start_published_date": start_published_date,
            "end_published_date": end_published_date,
        }
        common_params = {k: v for k, v in common_params.items() if v is not None} # Enlever les clés avec valeur None

        try:
            if find_similar_url:
                search_response = self.exa.find_similar_and_contents(
                    url=find_similar_url, **common_params, **contents_options
                )
            elif query:
                search_specific_params = {"type": search_type, "category": category}
                search_specific_params = {k: v for k, v in search_specific_params.items() if v is not None}
                search_response = self.exa.search_and_contents(
                    query=query, **common_params, **search_specific_params, **contents_options
                )
            else:
                return "Erreur : La recherche nécessite soit un 'query' (requête de recherche), soit une 'find_similar_url'."

            if not search_response.results:
                return "Aucun résultat pertinent trouvé par Exa Search avec les paramètres spécifiés."

            output_parts = []
            for result in search_response.results:
                content_display = ""
                if use_highlights and result.highlights:
                    content_display = "\n".join(result.highlights)
                elif result.text:
                    content_display = result.text 
                
                result_str = (
                    f"URL: {result.url}\n"
                    f"Title: {result.title or 'N/A'}\n"
                    f"Published Date: {result.published_date or 'N/A'}\n"
                    f"Score: {result.score:.4f}\n" # Le score de pertinence d'Exa
                    f"Contenu: {content_display}...\n---"
                )
                output_parts.append(result_str)
            
            return "\n".join(output_parts)

        except Exception as e:
            # Il serait bon de logger l'erreur complète pour le débogage côté serveur
            # print(f"DEBUG EXA TOOL: Error: {e}, Args: query='{query}', find_similar_url='{find_similar_url}', common_params={common_params}, contents_options={contents_options}")
            return f"Erreur lors de l'appel à l'API Exa : {type(e).__name__} - {e}. Vérifiez les paramètres et votre clé API Exa."