from __future__ import annotations

import functools
from typing import List, Dict, Set

from dataclasses import dataclass

from Options import Toggle, OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms
    
# Option Dataclass
@dataclass
class TemplateArchipelagoOptions:
    pass

# Main Class
class TemplateGame(Game):
    name = "Monster Hunter: The Board Game"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.PS4,
        KeymastersKeepGamePlatforms.XONE,
        KeymastersKeepGamePlatforms.SW,
        KeymastersKeepGamePlatforms.PS5,
        KeymastersKeepGamePlatforms.XSX,
    ]

    is_adult_only_or_unrated = False

    options_cls = TemplateArchipelagoOptions
    
    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
    return [
        # game constraint templates will go here
        
    ]