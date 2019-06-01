# -*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils.datasimulation import DataSimulation
from utils.argparsers.simulationargparser import SimulationArgumentParser
from algorithms.PDGD.pdgd import PDGD
from algorithms.PDGD.deeppdgd import DeepPDGD
from algorithms.DBGD.tddbgd import TD_DBGD
from algorithms.DBGD.pdbgd import P_DBGD
from algorithms.DBGD.tdmgd import TD_MGD
from algorithms.DBGD.pmgd import P_MGD
from algorithms.baselines.pairwise import Pairwise
from algorithms.DBGD.neural.pdbgd import Neural_P_DBGD
from algorithms.DBGD.pdbgd_wrapper import P_DBGD_Wrapper
from algorithms.DBGD.pmgd_wrapper import P_MGD_Wrapper
from algorithms.DBGD.tdNSGD import TD_NSGD
from algorithms.DBGD.tdNSGD_wrapper import TD_NSGD_Wrapper

description = 'Run script for testing framework.'
parser = SimulationArgumentParser(description=description)

rankers = []

# Baselines
ranker_params = {
  'learning_rate_decay': 0.9999977}
sim_args, other_args = parser.parse_all_args(ranker_params)

run_name = 'SIGIR2019/P-DBGD' 
# rankers.append((run_name, P_DBGD, other_args))

run_name = 'SIGIR2019/P-MGD' 
# rankers.append((run_name, P_MGD, other_args))

ranker_params = {
  'learning_rate_decay': 0.9999977,
  'GRAD_SIZE':60,
  'EXP_SIZE':25,
  'TB_QUEUE_SIZE':10,
  'TB_WINDOW_SIZE':50}
sim_args, other_args = parser.parse_all_args(ranker_params)

run_name = 'SIGIR2019/TD_NSGD' 
# rankers.append((run_name, TD_NSGD, other_args))


# DBGD based algorithms with document space wrapper
ranker_params = {
  'learning_rate_decay': 0.9999977,
  'k_initial': 3,
  'k_increase': False,
  'prev_qeury_len': 10}
sim_args, other_args = parser.parse_all_args(ranker_params)

run_name = 'SIGIR2019/DSGD_P_DBGD' 
rankers.append((run_name, P_DBGD_Wrapper, other_args))

run_name = 'SIGIR2019/DSGD_P_MGD' 
rankers.append((run_name, P_MGD_Wrapper, other_args))



# NSGD with document space wrapper
ranker_params = {
  'learning_rate_decay': 0.9999977,
  'k_initial': 3,
  'k_increase': False,
  'GRAD_SIZE':60,
  'EXP_SIZE':25,
  'TB_QUEUE_SIZE':10,
  'TB_WINDOW_SIZE':50,
  'prev_qeury_len': 10}
sim_args, other_args = parser.parse_all_args(ranker_params)

run_name = 'SIGIR2019/DSGD_TD_NSGD' 
# rankers.append((run_name, TD_NSGD_Wrapper, other_args))



sim = DataSimulation(sim_args)
sim.run(rankers)