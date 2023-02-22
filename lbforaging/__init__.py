from gym.envs.registration import registry, register, make, spec
from itertools import product

sizes = range(5, 20)
players = range(2, 20)
foods = range(1, 10)
coop = [True, False]
partial_obs = [True, False]


register(
    id="Foraging-10x10-3p-3f-v2",
    entry_point="lbforaging.foraging:ForagingEnv",
    kwargs={
        "players": 3,
        "max_player_level": 3,
        "field_size": (10, 10),
        "max_food": 3,
        "sight": 10,
        "max_episode_steps": 50,
    },
)

def grid_registration():
    for s, p, f, c in product(sizes, players, foods, coop):
        for sight in [2, s]: #range(1, s + 1):
            register(
                id="Foraging-grid{4}-{0}x{0}-{1}p-{2}f{3}-v2".format(s, p, f, "-coop" if c else "", "" if sight == s else f"-{sight}s"),
                entry_point="lbforaging.foraging:ForagingEnv",
                kwargs={
                    "players": p,
                    "max_player_level": 3,
                    "field_size": (s, s),
                    "max_food": f,
                    "sight": sight,
                    "max_episode_steps": 50,
                    "force_coop": c,
                    "grid_observation": True,
                },
            )
