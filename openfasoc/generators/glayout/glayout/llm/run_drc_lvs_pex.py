import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from validate_synthetic_data import run_all_tests, instantiate_convo 
from glayout.flow.pdk.sky130_mapped import sky130_mapped_pdk as sky130 
from pathlib import Path
from typing import Union, Optional 
from gdsfactory.component import Component

parent_path = Path(__file__).parent.resolve()
convo_path = Path("syntax_data/convos")
convo_path = parent_path / convo_path

def run_drc(convo_path: Path):
    for convo in convo_path.iterdir():
        try: 
            component = instantiate_convo(sky130, convo, return_component = True)
            sky130.drc_magic(component, component.name)
        except:
            print(f"Error running DRC on {convo}")
            continue

def run_lvs(component: Component, netlist_path: Union[Path, str]):
    pass
       
if __name__ == "__main__":
    run_drc(convo_path)
    run_drc(convo_path / "FirstOrderSigmaDelta")