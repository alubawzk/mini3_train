import argparse
from isaaclab.app import AppLauncher

parser = argparse.ArgumentParser()
AppLauncher.add_app_launcher_args(parser)
args_cli = parser.parse_args()

app_launcher = AppLauncher(args_cli)
simulation_app = app_launcher.app

import isaaclab.sim as sim_utils
from isaaclab.assets import Articulation
from robolab.assets.robots.roboparty import MINI3_CFG

sim = sim_utils.SimulationContext(sim_utils.SimulationCfg(dt=0.005))
robot_cfg = MINI3_CFG.replace(prim_path="/World/Robot")
robot = Articulation(robot_cfg)

sim.reset()

print("\nIsaac Lab joint order (lab_dof_names):")
for i, name in enumerate(robot.data.joint_names):
    print(f"  - {name}")

simulation_app.close()
