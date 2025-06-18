# Fichier: custom_tools/pharmacie_exa_tool.py

from types import NoneType
from typing import Any, Optional, Type
from pydantic import BaseModel, Field
from crewai.tools import BaseTool
from dateutil.parser import parse
import logging

try:
    from exa_py import Exa

    EXA_INSTALLED = True
except ImportError:
    Exa = Any
    EXA_INSTALLED = False


class EXABaseToolSchema(BaseModel):
    search_query: str = Field(
        ..., description="Mandatory search query you want to use to search the internet"
    )
    include_domains: Optional[list[str]] = Field(
        None, description="List of domains to include in the search"
    )


class EXASearchTool(BaseTool):
    model_config = {"arbitrary_types_allowed": True}
    name: str = "EXASearchTool"
    description: str = "Search the internet using Exa"
    args_schema: Type[BaseModel] = EXABaseToolSchema
    client: Optional["Exa"] = None
    content: Optional[bool] = False
    type: Optional[str] = "auto"
    num_results: Optional[int] = 5
    summary_prompt: Optional[str] = None

    def __init__(
        self,
        api_key: str,
        content: Optional[bool] = False,
        type: Optional[str] = "auto",
        num_results: Optional[int] = 5,
        summary_prompt: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(
            **kwargs,
        )
        if not EXA_INSTALLED:
            import click

            if click.confirm(
                "You are missing the 'exa_py' package. Would you like to install it?"
            ):
                import subprocess

                subprocess.run(["uv", "add", "exa_py"], check=True)

            else:
                raise ImportError(
                    "You are missing the 'exa_py' package. Would you like to install it?"
                )
        self.client = Exa(api_key=api_key)
        self.content = content
        self.type = type
        self.num_results = num_results
        self.summary_prompt = summary_prompt

    def _run(
        self,
        search_query: str,
        include_domains: Optional[list[str]] = None,
    ) -> Any:
        if self.client is None:
            raise ValueError("Client not initialized")

        search_params = {
            "type": self.type,
        }

        if include_domains:
            search_params["include_domains"] = include_domains
        if self.num_results:
            search_params["num_results"] = self.num_results
        if self.summary_prompt:
            search_params["summary"] = {
                "query": self.summary_prompt
            }
        if self.content:
            results = self.client.search_and_contents(
                search_query, highlights = True, **search_params
            )
        else:
            results = self.client.search(search_query, **search_params)

        return results