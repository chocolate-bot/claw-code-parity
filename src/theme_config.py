"""Theme configuration for Claw Code UI"""

from dataclasses import dataclass
from typing import Literal


@dataclass
class ColorTheme:
    """Color theme configuration for terminal UI"""

    # Primary brand color (logo, headers, accents)
    primary_color: str = "#FFEC8B"  # Light yellow (Khaki1)

    # Secondary color (secondary elements, borders)
    secondary_color: str = "#F0E68C"  # Darker yellow (Khaki)

    # Background colors
    bg_primary: str = "#FAFAD2"  # Light yellow background (LightGoldenrodYellow)
    bg_secondary: str = "#FFFFE0"  # Very light yellow (LightYellow)

    # Text colors
    text_primary: str = "#333333"  # Dark gray for readability
    text_secondary: str = "#666666"  # Medium gray
    text_accent: str = "#DAA520"  # GoldenRod for highlights

    # Status colors
    success: str = "#9ACD32"  # YellowGreen
    warning: str = "#FFD700"  # Gold
    error: str = "#CD5C5C"  # IndianRed
    info: str = "#87CEEB"  # SkyBlue

    # Tool/Agent colors
    tool_color: str = "#BDB76B"  # DarkKhaki
    agent_color: str = "#DAA520"  # GoldenRod
    command_color: str = "#D2691E"  # Chocolate

    # Terminal formatting
    bold: bool = True
    italic: bool = False
    underline: bool = False


# Default light yellow theme
LIGHT_YELLOW_THEME = ColorTheme()

# Alternative themes
class Themes:
    LIGHT_YELLOW = ColorTheme()
    ORIGINAL_CLAUDE = ColorTheme(
        primary_color="#4A9EFF",  # Claude blue
        secondary_color="#2B7FD9",
        bg_primary="#1A1A1A",
        bg_secondary="#2A2A2A",
        text_primary="#E5E5E5",
        text_secondary="#A0A0A0",
        text_accent="#4A9EFF",
        success="#4ADE80",
        warning="#FFD700",
        error="#FF6B6B",
        info="#87CEEB",
        tool_color="#5CADFF",
        agent_color="#7DD3FC",
        command_color="#A78BFA"
    )
    DARK_MODE = ColorTheme(
        primary_color="#FFD700",  # Gold
        secondary_color="#B8860B",  # DarkGoldenRod
        bg_primary="#121212",  # Black
        bg_secondary="#1E1E1E",
        text_primary="#E5E5E5",
        text_secondary="#A0A0A0",
        text_accent="#FFD700",
        success="#00C853",
        warning="#FFD700",
        error="#FF5252",
        info="#64B5F6",
        tool_color="#FFA726",
        agent_color="#FFCC80",
        command_color="#AB47BC"
    )


def get_current_theme(theme_name: str = "light_yellow") -> ColorTheme:
    """Get theme by name"""
    theme_map = {
        "light_yellow": Themes.LIGHT_YELLOW,
        "original_claude": Themes.ORIGINAL_CLAUDE,
        "dark": Themes.DARK_MODE,
    }
    return theme_map.get(theme_name, Themes.LIGHT_YELLOW)


def format_ansi(color: str, text: str, bold: bool = False) -> str:
    """Format text with ANSI color codes (basic implementation)"""
    # This is a simplified version - full ANSI implementation would need proper color codes
    prefix = "\033[1m" if bold else ""
    suffix = "\033[0m"
    return f"{prefix}{text}{suffix}"


if __name__ == "__main__":
    # Test theme
    theme = get_current_theme("light_yellow")
    print(f"Primary color: {theme.primary_color}")
    print(f"Background: {theme.bg_primary}")
    print(f"Success: {theme.success}")
