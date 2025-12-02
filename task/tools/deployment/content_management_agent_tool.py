from typing import Any

from task.tools.deployment.base_agent_tool import BaseAgentTool


class ContentManagementAgentTool(BaseAgentTool):

    # Provide implementations of deployment_name (in core config), name, description and parameters.
    # Don't forget to mark them as @property
    # Parameters:
    #   - prompt: string. Required.
    #   - propagate_history: boolean
    @property
    def deployment_name(self) -> str:
        return "content-management-agent"

    @property
    def name(self) -> str:
        return "content-management-agent"

    @property
    def description(self) -> str:
        return "A tool to manage and organize digital content, including text, images, videos, and documents."

    @property
    def parameters(self) -> dict:
        return {
            "type": "object",
            "properties": {
                "prompt": {
                    "type": "string",
                    "description": "The content management task to perform.",
                },
                "propagate_history": {
                    "type": "boolean",
                    "description": (
                        "Controls context continuity between the current agent and the Content Management Agent:"
                        "true: Includes prior exchanges between these two agents."
                        "false: Starts a fresh interaction without history."
                        "Usage: Only set to true if the current prompt is missing context that exists in the conversation history. History from other agents is never included."),
                },
            },
            "required": ["prompt"],
        }
