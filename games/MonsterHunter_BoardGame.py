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
    mh_expansions_owned: MH_Board_Game_Expansions_Owned

# Main Class
class MonsterHunterBoardGame(Game):
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
            GameObjectiveTemplate(
                label="Use Arena Quest rules when hunting.",
                data={
                    "ORIGIN": (self.origins, 1),
                    "KEEPSAKE": (self.keepsakes, 1),
                    "BODY_TYPE": (self.body_types, 1),
                },
            ),
            GameObjectiveTemplate(
                label="Use Arena Quest rules when hunting. Hunters start with 1 less potion (min. 1)",
                data={
                    "ORIGIN": (self.origins, 1),
                    "KEEPSAKE": (self.keepsakes, 1),
                    "BODY_TYPE": (self.body_types, 1),
                    "LOAD": (self.equip_loads, 1),
                },
            ),
            GameObjectiveTemplate(
                label="Use Arena Quest rules when hunting. Hunters use only 1 Palico (if applicable)",
                data={
                    "ORIGIN": (self.origins, 1),
                    "KEEPSAKE": (self.keepsakes, 1),
                    "BODY_TYPE": (self.body_types, 1),
                },
            ),
        ]
    
    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        templates: List[GameObjectiveTemplate] = [
            GameObjectiveTemplate(
                label="Successfully Hunt MONSTER",
                data={
                    "MONSTER": (self.monsters, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Successfully Hunt MONSTER using the WEAPON",
                data={
                    "MONSTER": (self.monsters, 1),
                    "WEAPON": (self.weapons, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Successfully Hunt MONSTER on DIFFICULTY Difficulty",
                data={
                    "MONSTER": (self.monsters, 1),
                    "DIFFICULTY": (self.difficulties, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Successfully Hunt MONSTER using the WEAPON on DIFFICULTY Difficulty",
                data={
                    "MONSTER": (self.monsters, 1),
                    "WEAPON": (self.weapons, 1),
                    "DIFFICULTY": (self.difficulties, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Break PARTS part(s) while Hunting MONSTER",
                data={
                    "MONSTER": (self.monsters, 1),
                    "PARTS": (lambda: list(range(1, 3)), 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Break PARTS part(s) while Hunting MONSTER using the WEAPON",
                data={
                    "MONSTER": (self.monsters, 1),
                    "PARTS": (lambda: list(range(1, 3)), 1),
                    "WEAPON": (self.weapons, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Break PARTS part(s) while Hunting MONSTER on DIFFICULTY Difficulty",
                data={
                    "MONSTER": (self.monsters, 1),
                    "PARTS": (lambda: list(range(1, 3)), 1),
                    "DIFFICULTY": (self.difficulties, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Break PARTS part(s) while Hunting MONSTER using the WEAPON on DIFFICULTY Difficulty",
                data={
                    "MONSTER": (self.monsters, 1),
                    "PARTS": (lambda: list(range(1, 3)), 1),
                    "WEAPON": (self.weapons, 1),
                    "DIFFICULTY": (self.difficulties, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
        ]
    
    @property
    def expansions_owned(self) -> Set[str]:
        return self.archipelago_options.monster_hunter_board_game_expansions_owned.value
    
    @property
    def has_expansion_wildspire_wastes(self) -> bool:
        return "Wildspire Wastes" in self.expansions_owned
    
    @property
    def has_expansion_kulu_ya_ku(self) -> bool:
        return "Kulu-Ya-Ku" in self.expansions_owned
    
    @property
    def has_expansion_teostra(self) -> bool:
        return "Teostra" in self.expansions_owned
    
    @property
    def has_expansion_nergigante(self) -> bool:
        return "Nergigante" in self.expansions_owned
    
    @property
    def has_expansion_kushala_daora(self) -> bool:
        return "Kushala Daora" in self.expansions_owned
    
    @property
    def has_expansion_hunters_arsenal(self) -> bool:
        return "Hunters' Arsenal" in self.expansions_owned
    
    @functools.cached_property
    def base_game_monsters(self) -> List[str]:
        return [
            "Great Jagras",
            "Anjanath",
            "Tobi-Kadachi",
            "Rathalos",
            "Azure Rathalos",
        ]
        
    @functools.cached_property
    def wildspire_wastes_monsters(self) -> List[str]:
        return [
            "Barroth",
            "Pukei-Pukei",
            "Jyuratodus",
            "Diablos",
            "Black Diablos",
        ]
    
    @functools.cached_property
    def kulu_ya_ku_monsters(self) -> List[str]:
        return [
            "Kulu-Ya-Ku",
        ]
        
    @functools.cached_property
    def teostra_monsters(self) -> List[str]:
        return [
            "Teostra",
        ]
        
    @functools.cached_property
    def nergigante_monsters(self) -> List[str]:
        return [
            "Nergigante",
        ]
    
    @functools.cached_property
    def kushala_daora_monsters(self) -> List[str]:
        return [
            "Kushala Daora",
        ]
        
    @functools.cached_property
    def base_game_weapons(self) -> List[str]:
        return [
            "Greatsword",
            "Dual Daggers",
            "Sword and Shield",
            "Bow",
        ]
    
    @functools.cached_property
    def wildspire_wastes_weapons(self) -> List[str]:
        return [
            "Switch Axe",
            "Charge Blade",
            "Insect Glaive",
            "Heavy Bowgun",
        ]
    
    @functools.cached_property
    def hunters_arsenal_weapons(self) -> List[str]:
        return [
            "Gunlance",
            "Hammer",
            "Lance",
            "Hunting Horn",
            "Light Bowgun",
            "Longsword",
        ]
    
    @functools.cached_property
    def difficulties_base(self) -> List[str]:
        return [
            "Assigned",
            "Investigation",
            "Tempered Investigation",
        ]
    
    def monsters(self) -> List[str]:
        monsters: List[str] = self.base_game_monsters[:]
        
        if self.has_expansion_wildspire_wastes:
            monsters.extend(self.wildspire_wastes_monsters[:])
        
        if self.has_expansion_kulu_ya_ku:
            monsters.extend(self.kulu_ya_ku_monsters[:])
            
        if self.has_expansion_teostra:
            monsters.extend(self.teostra_monsters[:])
            
        if self.has_expansion_nergigante:
            monsters.extend(self.nergigante_monsters[:])
        
        if self.has_expansion_kushala_daora:
            monsters.extend(self.kushala_daora_monsters[:])
            
        return monsters
    
    def weapons(self) -> List[str]:
        weapons: List[str] = self.base_game_weapons[:]
        
        if self.has_expansion_wildspire_wastes:
            weapons.extend(self.wildspire_wastes_weapons[:])
        
        if self.has_expansion_hunters_arsenal:
            weapons.extend(self.hunters_arsenal_weapons[:])
        
        return weapons
    
    def difficulties(self) -> List[str]:
        difficulties: List[str] = self.difficulties_base[:]
        
        return difficulties
    
    