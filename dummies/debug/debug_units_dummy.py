from bot.plans.tactics import PlanDistributeWorkers
from sc2 import UnitTypeId

from bot.knowledges import KnowledgeBot
from bot.plans import BuildOrder


class DebugUnitsDummy(KnowledgeBot):
    """Dummy bot for creating debug units to test against."""
    def __init__(self):
        super().__init__(type(self).__name__)

    async def create_plan(self) -> BuildOrder:
        return BuildOrder([
            PlanDistributeWorkers(),
        ])

    async def on_step(self, iteration):
        # Hack so that BuildingSolver is finally ready to give positions for the debug buildings.
        if iteration == 1:
            await self.create_debug_buildings()

        await super().on_step(iteration)

    async def create_debug_buildings(self):
        pid = self.player_id
        unit_type = UnitTypeId.LURKERMPBURROWED
        amount = 1

        # Enemy 3rd
        pos = self.knowledge.expansion_zones[-3].center_location

        await self._client.debug_create_unit(
            [[unit_type, amount, pos, pid]])

        # Enemy 4th
        pos = self.knowledge.expansion_zones[-4].center_location

        await self._client.debug_create_unit(
            [[unit_type, amount, pos, pid]])

        # Own natural
        pos = self.knowledge.expansion_zones[1].center_location

        await self._client.debug_create_unit(
            [[unit_type, amount, pos, pid]])

        # Own main
        pos = self.knowledge.expansion_zones[0].center_location

        await self._client.debug_create_unit(
            [[unit_type, amount, pos, pid]])
        await self._client.debug_create_unit(
            [[UnitTypeId.WIDOWMINEBURROWED, amount, pos, pid]])
