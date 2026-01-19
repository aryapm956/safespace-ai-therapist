"""
backend/tools.py

SAFE FALLBACK VERSION
This version avoids runtime errors if Ollama or Twilio
are not installed on the system.
"""

# -----------------------------
# MedGemma (Ollama) Tool
# -----------------------------

def query_medgemma(prompt: str) -> str:
    """
    Placeholder MedGemma response.
    Used when Ollama is not installed or configured.
    """

    system_style_response = (
        "I can sense how difficult this might feel for you. "
        "Many people experience similar emotions in situations like this, "
        "and it doesn’t mean there’s anything wrong with you. "
        "What sometimes helps is taking a moment to reflect on what triggered these feelings. "
        "You’ve already shown strength by reaching out and talking about this. "
        "Would you like to tell me more about what’s been weighing on your mind?"
    )

    return system_style_response


# -----------------------------
# Emergency Call Tool (Twilio)
# -----------------------------

def call_emergency():
    """
    Dummy emergency function.
    Prevents crashes if Twilio is not configured.
    """

    return {
        "status": "disabled",
        "message": "Emergency calling is not enabled in this demo version."
    }
