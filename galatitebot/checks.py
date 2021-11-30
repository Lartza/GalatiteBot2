from tanjun import abc as tanjun_abc

import config


async def role_check(ctx: tanjun_abc.Context) -> bool:
    result = any(x in config.ADMIN_ROLES for x in ctx.member.role_ids)

    return result
