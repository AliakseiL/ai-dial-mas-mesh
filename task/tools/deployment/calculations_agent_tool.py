from typing import Any

from task.tools.deployment.base_agent_tool import BaseAgentTool


class CalculationsAgentTool(BaseAgentTool):

    # Provide implementations of deployment_name (in core config), name, description and parameters.
    # Don't forget to mark them as @property
    # Parameters:
    #   - prompt: string. Required.
    #   - propagate_history: boolean
    @property
    def deployment_name(self) -> str:
        return "calculations-agent"

    @property
    def name(self) -> str:
        return "calculations-agent"

    @property
    def description(self) -> str:
        return "A tool to perform mathematical calculations and can run Python code for data analysis tasks."

    @property
    def parameters(self) -> dict:
        return {
            "type": "object",
            "properties": {
                "prompt": {
                    "type": "string",
                    "description": "The calculation or data analysis task to perform.",
                },
                "propagate_history": {
                    "type": "boolean",
                    "description": (
                        "Controls context continuity between the current agent and the Calculations Agent:"
                        "true: Includes prior exchanges between these two agents."
                        "false: Starts a fresh interaction without history."
                        "Usage: Only set to true if the current prompt is missing context that exists in the conversation history. History from other agents is never included."),
                },
            },
            "required": ["prompt"],
        }
